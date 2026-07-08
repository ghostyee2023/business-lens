---
name: business-lens
description: "Evaluate the business logic of a product opportunity, small product idea, service concept, customer pain, market opening, or candidate MVP. Use when the user asks whether an idea is a real business opportunity, whether the commercial logic works, who would pay, how it could acquire customers, what business model fits, what assumptions must be tested, or whether to proceed, pause, or reshape. For raw materials and idea generation use idea-spark first; for 3-hour MVP design use maker-forge after business-lens."
---

# 商机透镜 Business Lens

Version: v0.1.0

## Core Rule

Judge commercial logic, not idea beauty.

Always separate:

- customer pain
- buyer and budget
- value created
- value captured
- acquisition path
- delivery cost
- competitive pressure
- unverified assumptions
- next validation move

Do not claim an idea is a business only because it is useful, interesting, technically buildable, or similar to another case. A business opportunity needs a reachable buyer, a painful enough job, a plausible payment path, and a repeatable way to deliver value.

## Positioning

Business Lens is the commercial judgment layer:

```text
idea-spark
-> candidate opportunities
-> business-lens
-> commercial logic and go/no-go judgment
-> maker-forge
-> 3-hour MVP
```

Use `maker-forge` directly if the user only wants a lightweight MVP plan. Use Business Lens when the user asks "值不值得做", "有没有商机", "商业逻辑通不通", "怎么赚钱", "谁会买", "能不能成为产品/生意".

## Operating Modes

Use lite mode by default:

1. Rewrite the opportunity in one sentence.
2. Identify user, buyer, budget owner, and urgent job.
3. Evaluate commercial logic with `references/commercial-logic-check.md`.
4. Score the opportunity with `references/business-scorecard.md`.
5. List the top assumptions and validation tests.
6. Decide: proceed, reshape, park, or reject.
7. If proceed or reshape, hand off to `maker-forge`.

Use full mode when the user asks for a formal business judgment, workshop output, customer plan, pricing plan, or saved artifact.

## Workflow

1. Clarify only the commercial unknowns.
   If missing, infer cautiously and mark assumptions. Prioritize: buyer, budget, frequency, current workaround, acquisition path.

2. Run the commercial logic check.
   Read `references/commercial-logic-check.md`.

3. Score the opportunity.
   Read `references/business-scorecard.md`. Score demand, monetization, distribution, delivery, defensibility, and timing.

4. Stress-test the business model.
   Read `references/business-model-patterns.md` and choose the smallest plausible model: paid template, service-assisted MVP, subscription, one-off tool, workshop, plugin, marketplace wedge, lead generation, internal productivity product, or data product.

5. Identify fatal assumptions.
   Read `references/assumption-tests.md`. A good output must say what would make the idea false.

6. Output the decision.
   Use `references/output-template.md`.

## Decision Labels

- `proceed`: commercial logic is coherent enough for a first validation.
- `reshape`: real pain exists, but user, buyer, model, or wedge must change.
- `park`: interesting, but timing, access, or validation path is weak.
- `reject`: no clear buyer, repeated pain, switching reason, or value capture.

Do not use `proceed` unless the next validation action is concrete.

## Handoff To Maker Forge

When handing off, include:

```text
name:
user:
buyer:
scene:
pain:
current workaround:
commercial logic:
business model:
pricing hypothesis:
acquisition path:
fatal assumption:
first validation test:
```

## Boundaries

- Do not provide financial, legal, or investment advice. This is business-model reasoning, not professional advice.
- Do not browse or cite current market facts unless the user asks for market research or the claim depends on current data.
- Do not overfit to famous startup cases. Use cases as analogy, not proof.
- Do not write files unless the user asks to save, land, or generate an artifact.
- Do not expose private paths, internal project names, customer details, or source collection metadata.

## References

- `references/commercial-logic-check.md`: use for the core business logic chain.
- `references/business-scorecard.md`: use for structured scoring and decision labels.
- `references/business-model-patterns.md`: use to select the smallest plausible business model.
- `references/assumption-tests.md`: use to define fatal assumptions and validation tests.
- `references/output-template.md`: use for normal user-facing outputs.
