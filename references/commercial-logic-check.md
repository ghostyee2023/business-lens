# Commercial Logic Check

Use this check before scoring. A complete commercial story is not evidence, but a missing link exposes where validation must start.

## Logic Chain

```text
user
-> repeated or costly job
-> current workaround and cost of doing nothing
-> better outcome
-> buyer and budget hypothesis
-> payment and switching reason
-> reachable first users
-> delivery mechanism and unit effort
-> repeatability
-> defensibility or compounding asset
```

## Required Distinctions

- **User**: experiences the workflow or result.
- **Buyer**: can authorize payment.
- **Budget owner**: controls the spending category; may differ from buyer.
- **Value created**: time, money, risk, quality, speed, or confidence improved.
- **Value captured**: how the provider is paid or benefits economically.
- **Acquisition path**: the concrete route to the first 10 users, not "do marketing".
- **Delivery model**: how value is produced per customer and how effort changes with scale.

## Kill Gates

Record each as `true` or `false`. Do not use `unknown` to force `proceed`.

1. `repeated_or_costly_pain`: the pain recurs or has material one-time cost.
2. `identifiable_buyer`: a plausible payer or budget owner can be named.
3. `reachable_first_users`: a specific route to initial users exists.
4. `plausible_value_capture`: there is a credible payment or economic-benefit mechanism.
5. `testable_within_short_cycle`: the fatal assumption can be tested without building the full product.

All five must be `true` for `proceed`.

## Strong Signals

- The user already spends money, labor, delay, or risk on a worse workaround.
- The pain affects revenue, compliance, reputation, churn, or a deadline.
- A buyer can describe where the budget comes from.
- The first version can be delivered manually and charged for.
- The job occurs in a repeated workflow.
- The team already has permissioned access to a narrow first-user channel.

## Failure Smells

- Users say it is useful, but no one owns the budget.
- "Saves time" is asserted without showing whose valuable time or what outcome changes.
- Value appears only after major behavior change, integration, trust, or data accumulation.
- The product is a generic AI wrapper around a free good-enough workflow.
- Distribution is described as an audience type, not a reachable channel.
- Delivery requires growing human effort per customer without pricing for it.
- A famous company or adjacent product is treated as proof of this demand.
