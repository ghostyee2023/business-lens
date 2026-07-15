#!/usr/bin/env python3
"""Validate business-opportunity/v1 JSON records with no third-party dependencies."""

from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "business-opportunity/v1"
DECISIONS = {"proceed", "reshape", "park", "reject"}
EVIDENCE_TYPES = {
    "observed_or_reported",
    "host_internal",
    "external_current",
    "analogy",
    "inference",
    "assumption",
    "contradiction",
}
SCORE_FIELDS = {
    "demand",
    "buyer",
    "distribution",
    "delivery",
    "defensibility",
    "timing",
}
PROCEED_SCORE_FIELDS = {"demand", "buyer", "distribution", "delivery"}
GATE_FIELDS = {
    "repeated_or_costly_pain",
    "identifiable_buyer",
    "reachable_first_users",
    "plausible_value_capture",
    "testable_within_short_cycle",
}
TEST_FIELDS = {
    "user_group",
    "real_ask",
    "signal",
    "pass_threshold",
    "fail_threshold",
    "deadline",
}
TEXT_FIELDS = {
    "id",
    "upstream_schema",
    "upstream_id",
    "name",
    "user",
    "buyer",
    "budget_hypothesis",
    "scene",
    "pain",
    "current_workaround",
    "value_created",
    "value_captured",
    "acquisition_path",
    "delivery_model",
    "business_model",
    "pricing_hypothesis",
    "fatal_assumption",
    "decision_reason",
}


def is_non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def normalize_records(payload: Any) -> tuple[list[Any], list[str]]:
    if isinstance(payload, list):
        records = payload
    elif isinstance(payload, dict) and "records" in payload:
        records = payload["records"]
        if not isinstance(records, list):
            return [], ["$.records must be an array"]
    elif isinstance(payload, dict):
        records = [payload]
    else:
        return [], ["$ must be an object, an array, or an object with a records array"]

    if not records:
        return [], ["$ contains no business decision records"]
    return records, []


def validate_record(record: Any, index: int) -> list[str]:
    path = f"$[{index}]"
    errors: list[str] = []

    if not isinstance(record, dict):
        return [f"{path} must be an object"]

    if record.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"{path}.schema_version must equal {SCHEMA_VERSION!r}")

    for field in sorted(TEXT_FIELDS):
        if not is_non_empty_string(record.get(field)):
            errors.append(f"{path}.{field} must be a non-empty string")

    evidence = record.get("evidence")
    if not isinstance(evidence, list) or not evidence:
        errors.append(f"{path}.evidence must be a non-empty array")
    else:
        for evidence_index, item in enumerate(evidence):
            item_path = f"{path}.evidence[{evidence_index}]"
            if not isinstance(item, dict):
                errors.append(f"{item_path} must be an object")
                continue
            if item.get("type") not in EVIDENCE_TYPES:
                errors.append(
                    f"{item_path}.type must be one of {sorted(EVIDENCE_TYPES)}"
                )
            for field in ("claim", "source"):
                if not is_non_empty_string(item.get(field)):
                    errors.append(f"{item_path}.{field} must be a non-empty string")

    scores = record.get("scores")
    if not isinstance(scores, dict):
        errors.append(f"{path}.scores must be an object")
    else:
        for field in sorted(SCORE_FIELDS):
            value = scores.get(field)
            if isinstance(value, bool) or not isinstance(value, int) or not 1 <= value <= 5:
                errors.append(f"{path}.scores.{field} must be an integer from 1 to 5")

    gates = record.get("kill_gates")
    if not isinstance(gates, dict):
        errors.append(f"{path}.kill_gates must be an object")
    else:
        for field in sorted(GATE_FIELDS):
            if not isinstance(gates.get(field), bool):
                errors.append(f"{path}.kill_gates.{field} must be a boolean")

    validation_test = record.get("validation_test")
    if not isinstance(validation_test, dict):
        errors.append(f"{path}.validation_test must be an object")
    else:
        for field in sorted(TEST_FIELDS):
            if not is_non_empty_string(validation_test.get(field)):
                errors.append(
                    f"{path}.validation_test.{field} must be a non-empty string"
                )

    decision = record.get("decision")
    if decision not in DECISIONS:
        errors.append(f"{path}.decision must be one of {sorted(DECISIONS)}")

    reshape_direction = record.get("reshape_direction")
    if not isinstance(reshape_direction, str):
        errors.append(f"{path}.reshape_direction must be a string")
    elif decision == "reshape" and not reshape_direction.strip():
        errors.append(f"{path}.reshape_direction is required for reshape")
    elif decision in {"proceed", "park", "reject"} and reshape_direction.strip():
        errors.append(f"{path}.reshape_direction must be empty unless decision is reshape")

    maker_ready = record.get("maker_forge_ready")
    if not isinstance(maker_ready, bool):
        errors.append(f"{path}.maker_forge_ready must be a boolean")
    elif maker_ready != (decision == "proceed"):
        errors.append(
            f"{path}.maker_forge_ready must be true if and only if decision is proceed"
        )

    if decision == "proceed":
        if isinstance(gates, dict):
            failed_gates = [field for field in sorted(GATE_FIELDS) if gates.get(field) is not True]
            if failed_gates:
                errors.append(
                    f"{path} proceed requires every kill gate true; failed: {', '.join(failed_gates)}"
                )
        if isinstance(scores, dict):
            low_scores = [
                field
                for field in sorted(PROCEED_SCORE_FIELDS)
                if not isinstance(scores.get(field), bool)
                and isinstance(scores.get(field), int)
                and scores[field] < 3
            ]
            if low_scores:
                errors.append(
                    f"{path} proceed requires demand, buyer, distribution, and delivery >= 3; low: {', '.join(low_scores)}"
                )

    return errors


def validate_payload(payload: Any) -> list[str]:
    records, errors = normalize_records(payload)
    if errors:
        return errors

    seen_ids: dict[str, int] = {}
    for index, record in enumerate(records):
        errors.extend(validate_record(record, index))
        if isinstance(record, dict) and is_non_empty_string(record.get("id")):
            record_id = record["id"].strip()
            if record_id in seen_ids:
                errors.append(
                    f"$[{index}].id duplicates $[{seen_ids[record_id]}].id: {record_id!r}"
                )
            else:
                seen_ids[record_id] = index
    return errors


def valid_fixture() -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "id": "business-report-concierge",
        "upstream_schema": "idea-opportunity/v1",
        "upstream_id": "opportunity-report-concierge",
        "name": "Weekly report concierge",
        "user": "Small agency account leads",
        "buyer": "Agency owner",
        "budget_hypothesis": "Client delivery operations budget",
        "scene": "Weekly client reporting",
        "pain": "Account leads spend hours compiling inconsistent reports",
        "current_workaround": "Manual spreadsheet and slide assembly",
        "value_created": "Faster and more consistent client reporting",
        "value_captured": "Paid per-report pilot followed by a monthly service",
        "acquisition_path": "Direct outreach to ten existing agency contacts",
        "delivery_model": "Manual concierge using the client's existing exports",
        "business_model": "Service-assisted MVP",
        "pricing_hypothesis": "Three paid pilot reports at a fixed fee",
        "evidence": [
            {
                "type": "observed_or_reported",
                "claim": "Three account leads report weekly manual compilation",
                "source": "Discovery notes, 2026-07-15",
            }
        ],
        "scores": {
            "demand": 3,
            "buyer": 3,
            "distribution": 3,
            "delivery": 4,
            "defensibility": 2,
            "timing": 3,
        },
        "kill_gates": {field: True for field in GATE_FIELDS},
        "fatal_assumption": "Agency owners will pay for a manual reporting pilot",
        "validation_test": {
            "user_group": "Ten small agency owners",
            "real_ask": "Buy one fixed-fee report using real client data",
            "signal": "Paid pilot and delivery of usable source data",
            "pass_threshold": "At least 2 paid pilots from 10 qualified asks",
            "fail_threshold": "Zero paid pilots after 10 qualified asks",
            "deadline": "2026-07-29",
        },
        "decision": "proceed",
        "decision_reason": "All gates pass and a paid manual test can falsify willingness to pay",
        "reshape_direction": "",
        "maker_forge_ready": True,
    }


def run_self_test() -> int:
    cases: list[tuple[str, Any, bool]] = []
    valid = valid_fixture()
    cases.append(("valid record", valid, True))

    invalid_proceed = copy.deepcopy(valid)
    invalid_proceed["kill_gates"]["reachable_first_users"] = False
    invalid_proceed["scores"]["buyer"] = 2
    cases.append(("invalid proceed", invalid_proceed, False))
    cases.append(("empty records", {"records": []}, False))
    cases.append(("duplicate ids", [valid, copy.deepcopy(valid)], False))

    failed = False
    for name, payload, should_pass in cases:
        errors = validate_payload(payload)
        passed = not errors
        if passed != should_pass:
            failed = True
            print(f"SELF-TEST FAIL: {name}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"SELF-TEST PASS: {name}")
    return 1 if failed else 0


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8-sig") as handle:
        return json.load(handle)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate business-opportunity/v1 JSON records."
    )
    parser.add_argument("paths", nargs="*", type=Path, help="JSON file(s) to validate")
    parser.add_argument("--self-test", action="store_true", help="Run built-in regression cases")
    args = parser.parse_args()

    if args.self_test:
        return run_self_test()
    if not args.paths:
        parser.error("provide at least one JSON path or use --self-test")

    failed = False
    for path in args.paths:
        try:
            payload = load_json(path)
        except (OSError, json.JSONDecodeError) as exc:
            failed = True
            print(f"FAIL {path}: {exc}")
            continue

        errors = validate_payload(payload)
        if errors:
            failed = True
            print(f"FAIL {path}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"PASS {path}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
