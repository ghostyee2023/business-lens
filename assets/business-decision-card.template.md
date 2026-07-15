---
title: Business decision card
schema_version: business-opportunity/v1
status: draft
---

# Business Decision Card

Fill the JSON record below, save it as a `.json` handoff when machine validation is required, and run `scripts/validate_business_decision.py`.

```json
{
  "schema_version": "business-opportunity/v1",
  "id": "",
  "upstream_schema": "manual-input/v1",
  "upstream_id": "",
  "name": "",
  "user": "",
  "buyer": "",
  "budget_hypothesis": "",
  "scene": "",
  "pain": "",
  "current_workaround": "",
  "value_created": "",
  "value_captured": "",
  "acquisition_path": "",
  "delivery_model": "",
  "business_model": "",
  "pricing_hypothesis": "",
  "evidence": [],
  "scores": {
    "demand": 1,
    "buyer": 1,
    "distribution": 1,
    "delivery": 1,
    "defensibility": 1,
    "timing": 1
  },
  "kill_gates": {
    "repeated_or_costly_pain": false,
    "identifiable_buyer": false,
    "reachable_first_users": false,
    "plausible_value_capture": false,
    "testable_within_short_cycle": false
  },
  "fatal_assumption": "",
  "validation_test": {
    "user_group": "",
    "real_ask": "",
    "signal": "",
    "pass_threshold": "",
    "fail_threshold": "",
    "deadline": ""
  },
  "decision": "park",
  "decision_reason": "",
  "reshape_direction": "",
  "maker_forge_ready": false
}
```
