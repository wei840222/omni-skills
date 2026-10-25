"""Predeclared routing metrics; importing this module reads no experiment outputs."""
from collections import defaultdict
import math
import random

RUBRIC_VERSION = "harness-public-pilot-v1.1"


def _identities(values):
    if not isinstance(values, (list, tuple, set, frozenset)) or any(not isinstance(x, str) or not x for x in values):
        raise ValueError("Skill identities must be nonempty strings in a sequence")
    return frozenset(values)


def best_set_score(prediction, acceptable_sets):
    predicted = _identities(prediction)
    if not isinstance(acceptable_sets, list) or not acceptable_sets:
        raise ValueError("At least one complete acceptable set is required")
    scores = []
    for values in acceptable_sets:
        target = _identities(values)
        if not predicted and not target:
            precision = recall = f1 = 1.0
        elif not predicted or not target:
            precision = recall = f1 = 0.0
        else:
            overlap = len(predicted & target)
            precision, recall = overlap / len(predicted), overlap / len(target)
            f1 = 2 * overlap / (len(predicted) + len(target))
        scores.append({"f1": f1, "precision": precision, "recall": recall,
                       "exact": float(predicted == target), "target": sorted(target)})
    return sorted(scores, key=lambda x: (-x["f1"], -x["exact"], -x["precision"], -x["recall"], x["target"]))[0]


def _mean(values):
    values = list(values)
    return sum(values) / len(values) if values else None


def _family_mean(rows, field):
    groups = defaultdict(list)
    for row in rows:
        groups[row["family_id"]].append(row[field])
    return {key: _mean(values) for key, values in sorted(groups.items())}


def _prediction(value, require_status):
    if not isinstance(value, dict):
        if require_status:
            raise ValueError("Real run predictions require explicit terminal status")
        return _identities(value), "completed", True, False
    status = value.get("status")
    if status not in {"completed", "skipped-empty-pool", "unavailable", "timeout", "error"}:
        raise ValueError("Unknown prediction terminal status")
    skills = _identities(value.get("skills"))
    if status == "skipped-empty-pool" and (skills or type(value.get("candidate_count")) is not int or value["candidate_count"] != 0):
        raise ValueError("An empty-pool skip requires an empty selection and candidate_count=0")
    return skills, status, status in {"completed", "skipped-empty-pool"}, True


def evaluate(cases, annotations, predictions, candidates=None, split=None, *, require_status=True):
    """Require explicit terminal output for every selected case, including failures.

    Predictions map ids to {status, skills}; a valid skipped-empty-pool additionally
    declares candidate_count=0. Unit fixtures may opt into legacy name lists with
    require_status=False; those summaries are never sufficient for adoption.
    Candidates map ids to name sequences. Taxonomy/splits/labels are not model input.
    """
    case_ids = [case["id"] for case in cases]
    annotation_ids = [entry["id"] for entry in annotations]
    if len(set(case_ids)) != len(case_ids) or len(set(annotation_ids)) != len(annotation_ids) or set(case_ids) != set(annotation_ids):
        raise ValueError("Cases and annotations must match one-to-one")
    selected = [entry for entry in annotations if split is None or entry["split"] == split]
    expected = {entry["id"] for entry in selected}
    if not selected or set(predictions) != expected or candidates is not None and set(candidates) != expected:
        raise ValueError("Outputs must match every selected case exactly")
    if type(require_status) is not bool:
        raise ValueError("Explicit status enforcement must be boolean")
    rows, uncertainty, all_rows, candidate_rows, no_skill = [], [], [], [], []
    statuses = {status: 0 for status in ["completed", "skipped-empty-pool", "unavailable", "timeout", "error"]}
    failures, implicit_statuses = [], []
    for annotation in selected:
        case_id, family = annotation["id"], annotation["family_id"]
        if type(annotation.get("uncertain")) is not bool:
            raise ValueError("Annotation uncertainty must be explicit")
        predicted, status, successful, explicit = _prediction(predictions[case_id], require_status)
        statuses[status] += 1
        if not successful:
            failures.append(case_id)
        if not explicit:
            implicit_statuses.append(case_id)
        score = best_set_score(predicted, annotation["acceptable_sets"])
        if not successful:
            score.update({field: 0.0 for field in ["f1", "precision", "recall", "exact"]})
        row = {"id": case_id, "family_id": family, **score}
        if candidates is not None:
            pool = _identities(candidates[case_id])
            if status == "skipped-empty-pool" and pool:
                raise ValueError("Skipped empty pool contradicts supplied candidates")
        if annotation["uncertain"]:
            uncertainty.append(case_id)
            all_rows.append({"family_id": family, "lower": 0.0, "upper": float(successful)})
            continue
        rows.append(row)
        all_rows.append({"family_id": family, "lower": score["exact"], "upper": score["exact"]})
        targets = [_identities(target) for target in annotation["acceptable_sets"]]
        if annotation["type"] == "no-skill":
            if targets != [frozenset()]:
                raise ValueError("No-skill cases must have exactly one empty acceptable set")
            no_skill.append({"id": case_id, "fp": bool(predicted), "failed": not successful,
                             "correct_empty": successful and not predicted})
        if candidates is not None and all(targets):
            pool = _identities(candidates[case_id])
            candidate_rows.append({"family_id": family,
                                   "any_relevant": float(bool(pool & frozenset().union(*targets))),
                                   "complete_set": float(any(target <= pool for target in targets))})
    fields = ["f1", "precision", "recall", "exact"]
    family_scores = {field: _family_mean(rows, field) for field in fields}
    return {
        "rubric_version": RUBRIC_VERSION,
        "family_macro": {field: _mean(family_scores[field].values()) for field in fields},
        "case_mean": {field: _mean(row[field] for row in rows) for field in fields},
        "family_scores": family_scores,
        "coverage": {"resolved_cases": len(rows), "total_cases": len(selected),
                     "resolved_fraction": len(rows) / len(selected),
                     "resolved_families": len(family_scores["f1"]),
                     "total_families": len({entry["family_id"] for entry in selected}),
                     "uncertain_ids": sorted(uncertainty),
                     "successful_resolved_cases": sum(row["id"] not in failures for row in rows)},
        "reliability": {"complete": True, "explicit_statuses": not implicit_statuses,
                        "case_ids": sorted(expected), "total_cases": len(selected),
                        "failure_count": len(failures), "failure_ids": sorted(failures),
                        "successful_cases": len(selected) - len(failures),
                        "successful_fraction": (len(selected) - len(failures)) / len(selected),
                        "status_counts": statuses, "implicit_status_ids": sorted(implicit_statuses)},
        "binary_success_bounds": {
            "case": {bound: _mean(row[bound] for row in all_rows) for bound in ["lower", "upper"]},
            "family": {bound: _mean(_family_mean(all_rows, bound).values()) for bound in ["lower", "upper"]},
        },
        "candidate_coverage": {field: _mean(_family_mean(candidate_rows, field).values()) if candidates is not None else None
                               for field in ["any_relevant", "complete_set"]},
        "no_skill_false_positive": {"count": sum(row["fp"] for row in no_skill),
                                    "total": len(no_skill), "rate": _mean(float(row["fp"]) for row in no_skill),
                                    "ids": sorted(row["id"] for row in no_skill if row["fp"]),
                                    "correct_empty_count": sum(row["correct_empty"] for row in no_skill),
                                    "failure_count": sum(row["failed"] for row in no_skill),
                                    "failure_ids": sorted(row["id"] for row in no_skill if row["failed"])},
    }


def _quantile(ordered, probability):
    position = (len(ordered) - 1) * probability
    lower = math.floor(position)
    fraction = position - lower
    return ordered[lower] * (1 - fraction) + ordered[min(lower + 1, len(ordered) - 1)] * fraction


def empirical_p95(values):
    """Linear-interpolation p95; sample provenance comes from the frozen contract.

    The adoption latency gate uses selector original_service_ms, retaining that
    observation on cache reuse. Cache-read wall time is a separate measurement.
    """
    values = list(values)
    if not values or any(type(value) not in (int, float) or not math.isfinite(value) or value < 0 for value in values):
        raise ValueError("p95 requires finite nonnegative observed samples")
    return _quantile(sorted(values), 0.95)


def paired_family_bootstrap(baseline, variant, replicates=10000, seed=20261025, confidence=0.95):
    if not baseline or set(baseline) != set(variant) or type(replicates) is not int or replicates < 2 or not 0 < confidence < 1:
        raise ValueError("Matched families and a valid bootstrap specification are required")
    if any(not math.isfinite(value) for value in [*baseline.values(), *variant.values()]):
        raise ValueError("Scores must be finite")
    deltas = [variant[key] - baseline[key] for key in sorted(baseline)]
    rng = random.Random(seed)
    draws = sorted(_mean(rng.choices(deltas, k=len(deltas))) for _ in range(replicates))
    tail = (1 - confidence) / 2
    return {"delta": _mean(deltas), "lower": _quantile(draws, tail), "upper": _quantile(draws, 1 - tail),
            "families": len(deltas), "replicates": replicates, "seed": seed, "confidence": confidence}


def adoption_decision(*, delta, ci_lower, baseline_no_skill_fp_ids, variant_no_skill_fp_ids,
                      baseline_latency_p95, variant_latency_p95, baseline_cost_p95, variant_cost_p95,
                      budget_ok, hard_timeout_ok, baseline_reliability, variant_reliability):
    """Latency is original selector-service p95; cost is Jev selector input cost.

    Both variants use the same declared input-token unit price. Shared frozen
    query costs, reconstructed pipeline timings and actual new spend are reported
    separately. Missing verified original observations are insufficient evidence.
    """
    measures = [delta, ci_lower, baseline_latency_p95, variant_latency_p95, baseline_cost_p95, variant_cost_p95]
    if any(type(value) not in (int, float) or not math.isfinite(value) for value in measures):
        raise ValueError("Adoption requires finite observed measurements")
    if min(baseline_latency_p95, variant_latency_p95, baseline_cost_p95, variant_cost_p95) < 0:
        raise ValueError("Latency and cost cannot be negative")
    def reliable(summary):
        if not isinstance(summary, dict):
            return False
        ids = summary.get("case_ids")
        return (summary.get("complete") is True and summary.get("explicit_statuses") is True
                and isinstance(ids, list) and bool(ids) and all(isinstance(value, str) and value for value in ids)
                and len(ids) == len(set(ids)) and type(summary.get("failure_count")) is int
                and summary["failure_count"] == 0)

    baseline_ready, variant_ready = reliable(baseline_reliability), reliable(variant_reliability)
    checks = {
        "baseline_complete_and_reliable": baseline_ready,
        "variant_complete_and_reliable": variant_ready,
        "comparable_case_ids": baseline_ready and variant_ready and set(baseline_reliability["case_ids"]) == set(variant_reliability["case_ids"]),
        "minimum_improvement": delta >= 0.03,
        "positive_interval_lower": ci_lower > 0,
        "no_new_no_skill_false_positives": not (set(variant_no_skill_fp_ids) - set(baseline_no_skill_fp_ids)),
        "latency_p95": variant_latency_p95 <= 1.25 * baseline_latency_p95,
        "cost_p95": variant_cost_p95 <= 1.25 * baseline_cost_p95,
        "budget": budget_ok is True,
        "hard_timeout": hard_timeout_ok is True,
    }
    sufficient = baseline_ready and variant_ready and checks["comparable_case_ids"]
    return {"adopt": all(checks.values()), "decision": "adopt-challenger" if all(checks.values()) else "keep-baseline",
            "evidence_status": "sufficient" if sufficient else "insufficient", "checks": checks}
