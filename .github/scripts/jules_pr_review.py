#!/usr/bin/env python3
import json
import os
import subprocess
import time
import urllib.error
import urllib.request

JULES_API = "https://jules.googleapis.com/v1alpha"
GITHUB_API = "https://api.github.com"

# States where Jules has produced a review we can extract
REVIEWABLE_STATES = {
    "COMPLETED",
    "AWAITING_USER_FEEDBACK",
    "AWAITING_PLAN_APPROVAL",
    "PAUSED",
}
FINAL_STATES = REVIEWABLE_STATES | {"FAILED"}
MAX_DIFF_CHARS = 300_000
MAX_COMMENT_CHARS = 60_000
POLL_SECONDS = 15
MAX_POLLS = 100  # 25 minutes total


def log(msg):
    print(f"[jules-review] {msg}", flush=True)


def request(method, url, headers=None, body=None):
    data = None
    if body is not None:
        data = json.dumps(body).encode("utf-8")

    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers=headers or {},
    )

    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            raw = resp.read()
            content_type = resp.headers.get("content-type", "")
            text = raw.decode("utf-8", errors="replace")
            if "application/json" in content_type:
                return json.loads(text) if text else {}
            return text
    except urllib.error.HTTPError as exc:
        msg = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"{method} {url} failed: {exc.code} {msg}") from exc


def github_headers(accept="application/vnd.github+json"):
    return {
        "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
        "Accept": accept,
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "jules-pr-review-action",
    }


def jules_headers():
    return {
        "X-Goog-Api-Key": os.environ["JULES_API_KEY"],
        "Content-Type": "application/json",
        "User-Agent": "jules-pr-review-action",
    }


def git_config_value(key):
    result = subprocess.run(
        ["git", "config", "--get", key],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode == 0 and result.stdout.strip():
        return result.stdout.strip()
    return None


def ensure_git_config(key, value):
    if git_config_value(key):
        return
    subprocess.run(
        ["git", "config", key, value],
        check=True,
        capture_output=True,
    )


def get_pr_diff(owner, repo, pr_number):
    url = f"{GITHUB_API}/repos/{owner}/{repo}/pulls/{pr_number}"
    return request("GET", url, github_headers("application/vnd.github.v3.diff"))


def create_diff_branch(pr_number, diff_text):
    """Create a temporary branch with the full diff file for Jules to read."""
    # Save current commit
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        check=True
    )
    original_commit = result.stdout.strip()
    log(f"Current commit: {original_commit}")
    
    branch_name = f"temp/pr-{pr_number}-diff-{int(time.time())}"
    file_name = f"pr-{pr_number}-full.diff"
    
    log(f"Writing full diff to {file_name} ({len(diff_text):,} chars)...")
    with open(file_name, "w") as f:
        f.write(diff_text)

    ensure_git_config("user.name", "github-actions[bot]")
    ensure_git_config(
        "user.email",
        "41898282+github-actions[bot]@users.noreply.github.com",
    )

    log(f"Creating branch {branch_name}...")
    subprocess.run(["git", "checkout", "-b", branch_name], check=True, capture_output=True)
    subprocess.run(["git", "add", file_name], check=True, capture_output=True)
    subprocess.run(
        ["git", "commit", "-m", f"Add full diff for PR #{pr_number}"],
        check=True,
        capture_output=True
    )
    subprocess.run(["git", "push", "origin", branch_name], check=True, capture_output=True)
    
    # Switch back to original commit
    subprocess.run(["git", "checkout", original_commit], check=True, capture_output=True)
    log(f"Switched back to {original_commit}")
    log(f"Full diff branch created: {branch_name}")
    
    return branch_name


def delete_diff_branch(branch_name):
    """Delete the temporary diff branch."""
    try:
        subprocess.run(
            ["git", "push", "origin", "--delete", branch_name],
            check=True,
            capture_output=True,
            text=True
        )
        log(f"Deleted diff branch: {branch_name}")
    except subprocess.CalledProcessError as e:
        log(f"Failed to delete diff branch: {e.stderr}")


def create_jules_session(owner, repo, diff_text, diff_branch=None):
    pr_number = os.environ["PR_NUMBER"]
    title = os.environ.get("PR_TITLE", "")
    base_ref = os.environ["BASE_REF"]
    head_sha = os.environ["HEAD_SHA"]
    pr_url = os.environ["PR_URL"]

    truncated = len(diff_text) > MAX_DIFF_CHARS
    diff_for_prompt = diff_text[:MAX_DIFF_CHARS]

    # Build conditional block for full diff recovery
    full_diff_block = ""
    if truncated and diff_branch:
        file_name = f"pr-{pr_number}-full.diff"
        full_diff_block = f"""

## ⚠️ Full Diff Recovery (IMPORTANT)
The diff above was truncated to {MAX_DIFF_CHARS:,} characters. The complete diff ({len(diff_text):,} chars) is available in the repository.

To review the full diff, run:
```bash
git fetch origin {diff_branch}
git show {diff_branch}:{file_name}
```

Review the COMPLETE diff, not just the truncated excerpt above.
"""

    prompt = f"""You are a senior staff reviewer performing a canonical Skill Review for the `omni-skills` repository.

## Context
- Target Repo: {owner}/{repo}
- PR: #{pr_number} — {title}
- Base: {base_ref} → Head: {head_sha}
- URL: {pr_url}
- Diff fully provided: {not truncated}
{full_diff_block}
## Instructions & Reference Standards
Perform a complete Skill Review by referencing the canonical repository docs:

1. **Review Standards & Three-Lens Quality Audit**:
   Read and follow `docs/review-guide.md` (Procedure, Decision Rubric, and 3-lens review: `code-review-and-quality`, `writing-for-agents`, `darwin-skill`).

2. **Quality Gates 1–9 Verification**:
   Verify the diff against Gates 1–9 defined in `docs/refactor-guide.md`.

3. **Output Report Format**:
   You MUST format your final response strictly using the templates in `docs/pull-request-review-template.md`:
   - Use **Template A (Request changes)** if there are any blocking Required findings.
   - Use **Template B (Approve)** if there are NO Required findings.

<diff>
{diff_for_prompt}
</diff>
"""

    payload = {
        "prompt": prompt,
        "title": f"Review PR #{pr_number}: {title}"[:120],
        "sourceContext": {
            "source": f"sources/github/{owner}/{repo}",
            "githubRepoContext": {
                "startingBranch": base_ref,
            },
        },
        "requirePlanApproval": False,
    }

    return request("POST", f"{JULES_API}/sessions", jules_headers(), payload)


def get_jules_session(session_name):
    return request("GET", f"{JULES_API}/{session_name}", jules_headers())


def get_jules_activities(session_name):
    return request("GET", f"{JULES_API}/{session_name}/activities", jules_headers())


def pause_jules_session(session_name):
    """Pause the Jules session."""
    log(f"Pausing session {session_name}...")
    try:
        request("POST", f"{JULES_API}/{session_name}:pause", jules_headers(), {})
        log("Session paused.")
    except Exception as e:
        log(f"Pause failed (non-fatal): {e}")


def archive_jules_session(session_name):
    """Archive the Jules session to stop it from continuing to run."""
    log(f"Archiving session {session_name}...")
    try:
        request("POST", f"{JULES_API}/{session_name}:archive", jules_headers(), {})
        log("Session archived.")
    except Exception as e:
        log(f"Archive failed (non-fatal): {e}")


REVIEW_MARKER = "<!-- jules-pr-review -->"


def extract_review_from_activities(activities_response):
    activities = activities_response.get("activities", [])
    messages = []

    for activity in activities:
        agent = activity.get("agentMessaged") or {}
        text = agent.get("agentMessage")
        if text:
            messages.append(text.strip())

    if not messages:
        return None

    return messages[-1]


def has_complete_review(activities_response):
    """Check if activities contain a complete review (has the marker or key sections)."""
    activities = activities_response.get("activities", [])

    for activity in activities:
        agent = activity.get("agentMessaged") or {}
        text = agent.get("agentMessage") or ""

        # Check for review marker
        if REVIEW_MARKER in text:
            return True

        # Check for key review sections (heuristic)
        # Simple keyword matching - review should have these concepts
        text_lower = text.lower()
        has_summary = "summary" in text_lower
        has_blocking = "blocking" in text_lower or "issues" in text_lower
        has_recommendation = "recommendation" in text_lower or "verdict" in text_lower

        # If it has at least summary + one other section, likely complete
        if has_summary and (has_blocking or has_recommendation):
            return True

    return False


def post_pr_comment(owner, repo, pr_number, body):
    marker = "<!-- jules-pr-review -->"
    body = body.strip()
    if len(body) > MAX_COMMENT_CHARS:
        body = body[:MAX_COMMENT_CHARS] + "\n\n_Review truncated because it exceeded GitHub comment size limits._"

    comment = f"""{marker}
## Jules PR Review

{body}

---
_Reviewed by Jules via GitHub Actions._
"""

    url = f"{GITHUB_API}/repos/{owner}/{repo}/issues/{pr_number}/comments"
    return request("POST", url, github_headers(), {"body": comment})


def fail_pr_comment(owner, repo, pr_number, message):
    body = f"""<!-- jules-pr-review -->
## Jules PR Review failed

{message}

---
_The Jules review workflow could not complete._
"""
    url = f"{GITHUB_API}/repos/{owner}/{repo}/issues/{pr_number}/comments"
    request("POST", url, github_headers(), {"body": body})


def main():
    owner, repo = os.environ["GITHUB_REPOSITORY"].split("/", 1)
    pr_number = os.environ["PR_NUMBER"]

    log(f"Fetching diff for PR #{pr_number}...")
    diff_text = get_pr_diff(owner, repo, pr_number)
    if not diff_text.strip():
        log("No diff found, posting comment and exiting.")
        post_pr_comment(owner, repo, pr_number, "No diff was found for this pull request.")
        return

    log(f"Diff size: {len(diff_text):,} chars")
    
    # Generate full diff branch if truncated
    diff_branch = None
    if len(diff_text) > MAX_DIFF_CHARS:
        log("Diff truncated, creating full diff branch...")
        diff_branch = create_diff_branch(pr_number, diff_text)
    
    try:
        log("Creating Jules session...")
        session = create_jules_session(owner, repo, diff_text, diff_branch)
        session_name = session["name"]
        session_url = session.get("url", "")
        initial_state = session.get("state", "UNKNOWN")

        log(f"Session created: {session_name}")
        log(f"State: {initial_state}")
        if session_url:
            log(f"URL: {session_url}")

        final_session = session
        state = session.get("state", "UNKNOWN")
        early_exit = False
        for poll_num in range(1, MAX_POLLS + 1):
            time.sleep(POLL_SECONDS)
            final_session = get_jules_session(session_name)
            state = final_session.get("state", "UNKNOWN")

            if poll_num % 4 == 1 or state in FINAL_STATES:
                log(f"Poll {poll_num}/{MAX_POLLS}: state={state}")

            if state in FINAL_STATES:
                log(f"Session reached final state: {state}")
                # Even in final state, check if review is already complete
                try:
                    activities = get_jules_activities(session_name)
                    if has_complete_review(activities):
                        log("Review detected in activities — pausing and archiving session")
                        pause_jules_session(session_name)
                        archive_jules_session(session_name)
                        early_exit = True
                except Exception as e:
                    log(f"Could not check activities: {e}")
                break

            # Early exit: if IN_PROGRESS and review already complete, archive session
            if state == "IN_PROGRESS":
                try:
                    activities = get_jules_activities(session_name)
                    if has_complete_review(activities):
                        log("Review detected in activities during IN_PROGRESS — pausing and archiving session")
                        pause_jules_session(session_name)
                        archive_jules_session(session_name)
                        early_exit = True
                        break
                except Exception as e:
                    log(f"Could not check activities: {e}")

        if not early_exit and state not in FINAL_STATES:
            log(f"Timed out after {MAX_POLLS * POLL_SECONDS}s")
            fail_pr_comment(owner, repo, pr_number, f"Timed out waiting for Jules session after {MAX_POLLS * POLL_SECONDS // 60} minutes.\n\nLast state: `{final_session.get('state')}`\n\nSession: {session_url}")
            raise SystemExit(1)

        state = final_session.get("state")
        log(f"Fetching activities for session...")
        activities = get_jules_activities(session_name)
        activity_count = len(activities.get("activities", []))
        log(f"Found {activity_count} activities")

        if not early_exit and state not in REVIEWABLE_STATES:
            reason = json.dumps(final_session, indent=2, ensure_ascii=False)
            fail_pr_comment(
                owner,
                repo,
                pr_number,
                f"Jules session ended with non-reviewable state `{state}`.\n\nSession: {session_url}\n\n```json\n{reason[:4000]}\n```",
            )
            raise SystemExit(1)

        review = extract_review_from_activities(activities)
        if review is None:
            review = "Jules completed, but no review message was found in session activities."
        
        if session_url:
            review += f"\n\nJules session: {session_url}"

        log(f"Posting review comment ({len(review):,} chars)...")
        post_pr_comment(owner, repo, pr_number, review)
        log("Done!")
        
    finally:
        # Cleanup diff branch
        if diff_branch:
            log(f"Cleaning up diff branch: {diff_branch}")
            delete_diff_branch(diff_branch)


if __name__ == "__main__":
    main()
