# Commercial Decision Contract

Use `business-opportunity/v1` for saved decisions and handoffs. The schema records the judgment and its evidence boundary; it does not certify market demand.

## Record Shape

```json
{
  "schema_version": "business-opportunity/v1",
  "id": "business-short-id",
  "upstream_schema": "idea-opportunity/v1",
  "upstream_id": "opportunity-short-id",
  "name": "Opportunity name",
  "user": "Narrow user group",
  "buyer": "Payer or budget owner hypothesis",
  "budget_hypothesis": "Existing budget, replacement spend, or unknown",
  "scene": "Repeated or costly scene",
  "pain": "Problem and consequence",
  "current_workaround": "What happens today and at what cost",
  "value_created": "Outcome improved for the user or buyer",
  "value_captured": "How economic value can return to the provider",
  "acquisition_path": "Specific route to the first 10 qualified users",
  "delivery_model": "How value is delivered and unit effort behaves",
  "business_model": "Smallest plausible commercial model",
  "pricing_hypothesis": "Price, range, or basis to test",
  "evidence": [
    {
      "type": "observed_or_reported",
      "claim": "Auditable claim",
      "source": "Source and date"
    }
  ],
  "scores": {
    "demand": 3,
    "buyer": 3,
    "distribution": 3,
    "delivery": 3,
    "defensibility": 2,
    "timing": 3
  },
  "kill_gates": {
    "repeated_or_costly_pain": true,
    "identifiable_buyer": true,
    "reachable_first_users": true,
    "plausible_value_capture": true,
    "testable_within_short_cycle": true
  },
  "fatal_assumption": "Falsifiable sentence that could overturn the decision",
  "validation_test": {
    "user_group": "Narrow target group",
    "real_ask": "Money, data, time, workflow change, or commitment requested",
    "signal": "Observable behavior",
    "pass_threshold": "Precommitted minimum supporting result",
    "fail_threshold": "Precommitted result that changes the decision",
    "deadline": "YYYY-MM-DD or fixed short window"
  },
  "decision": "proceed",
  "decision_reason": "Why this label follows from evidence, scores, and gates",
  "reshape_direction": "",
  "maker_forge_ready": true
}
```

## Invariants

- Use exactly `schema_version: business-opportunity/v1`.
- Keep `id` unique within a decision set and keep `upstream_id` stable.
- Use only evidence types defined in `evidence-ladder.md`.
- Score all six dimensions with integers from 1 to 5.
- Set all five kill gates to booleans.
- Use only `proceed`, `reshape`, `park`, or `reject`.
- Require non-empty `reshape_direction` only for `reshape`; leave it empty otherwise.
- Require a complete validation test for every decision, including the evidence that could reopen a parked or rejected idea.
- For `proceed`, require all kill gates true and demand, buyer, distribution, and delivery at least 3.
- Set `maker_forge_ready: true` if and only if the decision is a valid `proceed` record.
- Never interpret `proceed` or `maker_forge_ready` as proof of commercial validation.

## Handoff

Pass the full record to `maker-forge`; do not reduce it to a prose summary. Maker Forge must preserve:

- `id`, `upstream_id`, and schema provenance
- buyer, business model, pricing hypothesis, and acquisition path
- fatal assumption and complete validation test
- evidence/assumption separation

Before saving or handing off JSON, run:

```bash
python scripts/validate_business_decision.py decision.json
```
