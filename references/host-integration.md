# Host Integration

Use this reference only when Business Lens runs inside a project, knowledge base, or operating system with its own routing and capabilities.

## Capability Hooks

Map host tools by function, not by vendor name:

- **Narrow internal search**: retrieve only relevant product, customer, prior-opportunity, delivery, and sales evidence. Do not scan the whole host by default.
- **Confidence scoring**: label factual claims in saved artifacts when the host requires it. Do not convert the six commercial scores into factual-confidence labels.
- **Strategic advisor**: invoke only when the user explicitly requests that advisor or the host's routing rules require it. Keep the advisor's judgment as inference unless backed by evidence.
- **Execution routing**: consider only valid `proceed` decisions, or a `reshape` after its new direction has been re-evaluated. Respect the host's opportunity-card or project-card gate before development, selling, delivery, or external commitments.
- **Downstream forge**: pass only validated records with `maker_forge_ready: true`.

## Read and Write Boundary

- Read narrowly from approved strategic context, products, customer scenes, prior opportunities, and delivery evidence.
- Do not let internal filenames, customer identities, or private collection metadata leak into external output.
- Do not write unless the user or host workflow authorizes saving.
- Save the record where the host declares opportunity or project assets belong; never invent a new root path.

## Decision Integrity

Host evidence may change scores or gates, but host routing must not bypass the `business-opportunity/v1` invariants. If host policy conflicts with this skill, follow the stricter safety or evidence rule and surface the conflict.
