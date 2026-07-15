# Evidence Ladder

Classify every material claim before using it in a commercial decision.

## Evidence Types

| Type | Meaning | Decision use |
| --- | --- | --- |
| `observed_or_reported` | Direct observation, source-supported statement, customer report, or behavioral record | Supports a score in proportion to specificity and sample quality |
| `host_internal` | Approved internal product, customer, delivery, sales, or performance evidence from the host | Useful when provenance is retained and privacy rules are respected |
| `external_current` | Current market, competitor, policy, price, or channel evidence from a cited external source | Use for time-sensitive claims; cite source and date |
| `analogy` | A similar case, company, workflow, or product | Generates hypotheses and risks; never proves demand |
| `inference` | Reasoned conclusion derived from evidence | State the derivation; do not present as observed fact |
| `assumption` | Necessary but unverified proposition | Candidate for the fatal assumption or validation test |
| `contradiction` | Evidence that weakens or conflicts with the opportunity story | Show before scoring and explain how it affects the decision |

## Evidence Record

Use this shape in `business-opportunity/v1`:

```json
{
  "type": "observed_or_reported",
  "claim": "Three target users currently spend two hours weekly compiling the report.",
  "source": "Customer interviews, 2026-07-10"
}
```

Keep `source` specific enough to audit without exposing protected customer data in public output.

## Rules

- Prefer behavior over stated preference and repeated behavior over one-off anecdotes.
- Treat host/internal evidence as context, not universal market truth.
- Treat current external evidence as perishable; include date or retrieval context.
- Never let an analogy raise demand or buyer above what direct evidence supports.
- Keep contradiction records even when the final decision is `proceed`.
- If a key claim has no support, classify it as `assumption` and lower the relevant score.
