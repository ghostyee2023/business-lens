# Upstream Contract

Use this reference when Business Lens receives an opportunity from `idea-spark`.

## Accepted Input

The preferred upstream schema is `idea-opportunity/v1`. Require:

- `id`, `name`, `user`, `scene`, `pain`, and `current_workaround`
- separate `source_support`, `inferences`, and `uncertainties`
- `status: verified` with all upstream validation checks true for a formal handoff

If the record is still `candidate`, analyze it only as a provisional opportunity and do not imply that source support has been verified.

## Field Mapping

| Upstream | Business decision |
| --- | --- |
| `schema_version` | `upstream_schema` |
| `id` | `upstream_id` |
| `name`, `user`, `scene`, `pain`, `current_workaround` | preserve, then refine only with explicit reasoning |
| `buyer` | buyer hypothesis; never treat as confirmed automatically |
| `source_support` | evidence items typed `observed_or_reported` |
| `inferences` | evidence items typed `inference` |
| `uncertainties` | candidate assumptions or fatal-assumption inputs |
| `why_now` | input to timing score, not proof of urgency |

For a direct user idea without an upstream record, use:

```json
{
  "upstream_schema": "manual-input/v1",
  "upstream_id": "manual:<stable-local-id>"
}
```

## Ownership Boundary

Business Lens owns buyer/budget analysis, value capture, acquisition, delivery, pricing hypothesis, commercial scores, kill gates, decision, and validation design. Do not rewrite unsupported upstream claims as facts merely to complete the business record.

Preserve the upstream identifier so a later decision can be traced to the source opportunity.
