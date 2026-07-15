# Business Scorecard

Score each dimension from 1 to 5 and add one evidence-bounded reason. Use 2 and 4 only when the opportunity clearly falls between adjacent anchors.

| Dimension | 1 | 3 | 5 |
| --- | --- | --- | --- |
| `demand` | Rare, vague, low-cost pain; no meaningful workaround | Recurring or costly pain is plausible but supported mainly by reports or limited observations | Repeated costly behavior is directly observed; users already pay or make meaningful sacrifices |
| `buyer` | No identifiable payer or budget path | Plausible buyer and budget hypothesis, not yet behaviorally confirmed | Named buyer class controls a fitting budget and has shown buying behavior |
| `distribution` | First users cannot be specifically reached | One concrete first-user channel exists but access or conversion is untested | Permissioned or proven channel can reach qualified buyers repeatedly |
| `delivery` | Value needs a large build, integration, dataset, or unpriced human effort | Manual/service-assisted delivery can test value with manageable effort | Narrow value can be delivered quickly and repeatably with improving unit effort |
| `defensibility` | Generic feature with free substitutes and no compounding asset | Workflow fit, trust, templates, or data may create some stickiness | Repeated usage compounds proprietary workflow, data, trust, distribution, or switching cost |
| `timing` | No trigger; adoption depends on behavior or infrastructure not ready | A plausible trigger exists, but urgency is uneven or unverified | External or workflow change creates urgent adoption pressure now |

## Decision Constraints

Do not calculate a simple average as the decision.

- `proceed`: all kill gates are true; demand, buyer, distribution, and delivery are each at least 3; a complete short-cycle test exists.
- `reshape`: pain may be real, but at least one of user, buyer, wedge, channel, model, or delivery needs a named change.
- `park`: evidence, access, timing, or testability is too weak now, but a future trigger could change the judgment.
- `reject`: core pain, buyer, switching reason, or value capture is incoherent or contradicted.

Defensibility and timing inform priority, but neither rescues a failed buyer, distribution, or delivery path.

## Score Integrity

- Score what current evidence supports, not the upside story.
- A high score is not a confidence label.
- Record contrary evidence before assigning a score.
- If evidence is missing, prefer 1 or 2 and state what would raise it.
