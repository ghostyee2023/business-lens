---
name: business-lens
description: "Evaluate the commercial logic of a product opportunity, service concept, customer pain, or candidate MVP and produce an evidence-bounded proceed, reshape, park, or reject decision. Use when the user asks whether an idea is a real business opportunity, who would buy, where budget comes from, how customers can be reached, what business model fits, what assumption could kill it, or what must be tested before building. Accept raw opportunities or idea-opportunity/v1 records from idea-spark; hand only maker-forge-ready business-opportunity/v1 records to maker-forge."
---

# 商机透镜 Business Lens

Version: v0.2.0

## Core Rule

Judge commercial logic, not idea beauty. Separate evidence from inference and assumptions. Never use an analogy, score, or polished narrative as proof of demand.

Require a coherent path through:

```text
repeated or costly pain
-> identifiable buyer and budget hypothesis
-> value created and captured
-> reachable first users
-> repeatable delivery
-> falsifiable short-cycle test
```

`proceed` means "ready for validation or an experimental MVP", not "commercially validated".

## Positioning

```text
idea-spark
-> idea-opportunity/v1
-> business-lens
-> business-opportunity/v1
-> maker-forge
```

- Route raw materials, books, notes, or broad opportunity discovery to `idea-spark`.
- Use Business Lens for commercial judgment.
- Route to `maker-forge` only when `maker_forge_ready: true`.

## Intake

For an `idea-opportunity/v1` record, read `references/upstream-contract.md` and preserve `upstream_id`. Treat its buyer as a hypothesis, not a fact.

For an unstructured idea, normalize at least: name, user, scene, pain, current workaround, and unknowns. Infer cautiously and mark assumptions. Do not block on every missing field; block only when a missing commercial choice would materially change the judgment.

## Workflow

1. Build the commercial logic chain.
   Read `references/commercial-logic-check.md`. Distinguish user, buyer, budget owner, payment reason, acquisition path, and delivery model.

2. Classify evidence.
   Read `references/evidence-ladder.md`. Record contradictions explicitly. Use current external research only when requested or necessary for a time-sensitive claim.

3. Score with anchors.
   Read `references/business-scorecard.md`. Score demand, buyer, distribution, delivery, defensibility, and timing from 1 to 5. Do not average blindly or let strong dimensions rescue a failed gate.

4. Choose the smallest plausible business model.
   Read `references/business-model-patterns.md`. Prefer a manual or service-assisted test before premature SaaS.

5. Apply kill gates and design the test.
   Read `references/assumption-tests.md`. Identify one fatal assumption and one test with a real ask, pass/fail thresholds, and deadline.

6. Decide.
   Use `proceed`, `reshape`, `park`, or `reject` according to `references/commercial-decision-contract.md`.

7. Present or save.
   Use `references/output-template.md` for user-facing output. For saved or reusable handoffs, copy `assets/business-decision-card.template.md`, fill every required field, and run `scripts/validate_business_decision.py`.

## Decision Guardrails

- Use `proceed` only when all five kill gates pass and demand, buyer, distribution, and delivery are each at least 3.
- Use `reshape` when pain may be real but user, buyer, wedge, channel, model, or delivery must change. Always include `reshape_direction`.
- Use `park` when timing, access, evidence, or testability is currently too weak.
- Use `reject` when the opportunity lacks repeated/costly pain, an identifiable buyer, plausible value capture, or a credible reason to switch.
- Set `maker_forge_ready: true` only for a structurally complete `proceed` record. A clear `reshape` must be re-evaluated after reshaping before handoff.

## Host Integration

When operating inside a knowledge base or project host, read `references/host-integration.md`. Host tools may add internal evidence, confidence labels, or routing, but must not silently change the commercial decision rules.

## Boundaries

- Do not provide financial, legal, or investment advice.
- Do not claim market validation without direct behavioral evidence.
- Do not browse by default; browse when requested or when a current claim materially affects the decision.
- Do not expose private paths, internal project names, customer details, or source metadata in customer-facing output.
- Do not write files unless the user asks to save, land, or generate an artifact.

## References

- `references/upstream-contract.md`: read for `idea-spark` intake and provenance.
- `references/commercial-logic-check.md`: read for the core logic chain and kill gates.
- `references/evidence-ladder.md`: read to classify support, assumptions, and contradictions.
- `references/business-scorecard.md`: read for anchored scoring and decision constraints.
- `references/business-model-patterns.md`: read to select the smallest plausible model.
- `references/assumption-tests.md`: read to design falsifiable validation.
- `references/commercial-decision-contract.md`: read for `business-opportunity/v1` fields and invariants.
- `references/output-template.md`: read for normal user-facing outputs.
- `references/host-integration.md`: read only when running inside a host project or knowledge base.
- `assets/business-decision-card.template.md`: copy for saved decision artifacts.
- `scripts/validate_business_decision.py`: run against saved JSON or handoff records.
