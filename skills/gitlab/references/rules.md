# Rules and Triggers

## Rules gotchas

- Do not mix `rules:` with `only:`/`except:` on the same job. Prefer `rules`; `only`/`except` are older keywords and not the active direction of the product.
- First matching rule wins. Put the most specific conditions before broader ones.
- Missing `when:` defaults to `on_success`. Example: a rule with only `if: $CI_COMMIT_TAG` still creates the job on tags when prior rules do not match first.
- `rules: []` means the job is never created — different from omitting `rules` entirely.
- Add a final `- when: never` (or an explicit never rule) when unmatched conditions must not fall through into an unintended job.

### Tag-only job example

```yaml
publish:
  script: echo "tag release"
  rules:
    - if: $CI_COMMIT_TAG
    - when: never
```

## Pipeline triggers

- `CI_PIPELINE_SOURCE` varies by how the pipeline started, including values such as `push`, `merge_request_event`, `schedule`, `api`, and `trigger` (exact set is version/product dependent — confirm against current predefined variables docs when branching on rare sources).
- Merge request pipelines need MR-oriented rules (commonly `if: $CI_PIPELINE_SOURCE == "merge_request_event"` and/or `$CI_MERGE_REQUEST_IID`) — branch-only rules will not cover MR detached pipelines.
- Detached MR pipelines test the source branch tip; merged-result pipelines test the merge result when that feature is enabled. Choose rules and test expectations deliberately.

## Debug checklist

1. Print effective `CI_PIPELINE_SOURCE`, branch/tag, and MR IIDs in a diagnostic job when selection is unclear.
2. Walk `rules` top-to-bottom; stop at the first match.
3. Confirm whether the pipeline type is branch, tag, MR detached, or merged result before changing scripts.
