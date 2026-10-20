---
name: backend-planning-pack
description: generate or refine a backend architecture and planning document pack for a backend, api, service, worker, integration, database-backed system, or platform component. use when the user asks for a technical design doc, architecture plan, solution outline, backend planning pack, or critique of an existing backend design. support both generic templates and context-specific packs for saas, internal tools, automations, compliance-sensitive systems, and multi-service backends. adapt the pack to the user's stack, scale, integrations, security, and delivery constraints. when the user asks for standards, best practices, vendor-specific patterns, or other authoritative guidance, pull from official documentation on the web and ground recommendations in those sources.
---

# Backend Planning Pack

Generate a backend planning document pack in markdown at a depth appropriate to the system's size, risk, and delivery stage. Default to a single master document with clear headings that the user can copy into their docs tool.

## Workflow

1. Identify the requested mode.
   - **Generic pack**: the user wants a reusable, industry-style planning pack.
   - **Context-specific pack**: the user gives a system type, stack, scale, compliance needs, integrations, or constraints.
   - **Review or refine**: the user already has a draft or architecture direction and wants it improved.

2. Select the output depth.
   - **Lean**: use for a small service, worker, integration, spike, or early design. Cover only the decisions needed to implement and operate it safely.
   - **Standard**: use by default for a production backend. Cover the relevant baseline template sections with moderate detail.
   - **Full**: use for regulated, high-scale, high-risk, multi-service, or migration-heavy systems. Use the complete baseline and expand evidence, failure handling, and operational detail.
   - Honour an explicit depth or length requested by the user. Otherwise state the selected depth in the assumptions.

3. Gather the minimum context from the user's request.
   - Expected users or consuming systems
   - Core backend responsibilities
   - Stack or platform choices, if provided
   - Performance, reliability, and security expectations
   - Integrations, data sensitivity, and deployment constraints

4. Decide whether to ask clarifying questions.
   - Ask only when a missing answer would materially change the architecture.
   - Ask at most three targeted questions.
   - If the user gave partial context, proceed with explicit assumptions instead of blocking.
   - If the request is for a reusable template, do not ask questions unless the user asks for a specialised version.

5. Decide how much external research is needed.
   - If the user asks for best practices, standards, official guidance, or vendor-specific patterns, use web search.
   - Prefer official documentation over blogs, forums, and marketing pages.
   - If facts may have changed, confirm them on the web before writing.
   - Keep research bounded to claims that materially affect architecture, constraints, or operational decisions.

6. Produce the planning pack.
   - Use the template in `references/template.md` as the baseline structure.
   - Pull in `references/saas-checklist.md` for SaaS and multi-tenant systems.
   - Pull in `references/event-driven-checklist.md` for event-driven, worker-heavy, queue-based, or integration-heavy systems.
   - Tailor sections, examples, and wording to the user's context.
   - Keep the selected depth complete enough to be operational, not just aspirational.

7. Add a concise decision layer.
   - Highlight major trade-offs.
   - Call out missing information or assumptions.
   - Recommend immediate next actions when helpful.

## Official documentation rule

When external grounding is needed, search the web and prioritise official documentation from standards bodies, cloud vendors, framework maintainers, or protocol owners. Use the source list in `references/official-doc-sources.md`.

Apply these rules:
- Prefer the most authoritative source available.
- Prefer normative or product documentation over commentary.
- Cite the official source for claims about standards, platform features, limits, or recommended practices.
- If official documentation is unavailable for a niche topic, state that clearly and then use the best reputable source available.

## Scope guardrails

Use this skill for planning, design, review, and architecture-pack generation. Do not use it for:
- routine feature implementation
- debugging application code
- low-level code optimisation requests
- frontend-only planning
- project management plans that do not require backend architecture detail

## Output requirements

Always produce a single markdown document unless the user asks for another format.

### Default structure

Use the baseline template from `references/template.md`. In **full** mode, keep the section order unless there is a strong reason to change it. In **lean** and **standard** modes, omit or combine sections that do not affect a decision, requirement, risk, or operational responsibility; do not emit empty headings.

### Output depth

- **Lean**: summarise scope, requirements, proposed design, core data and API decisions, security, failure handling, testing, delivery, and open questions. Prefer a compact decision-oriented document.
- **Standard**: cover every relevant baseline area, but combine closely related sections where that improves readability.
- **Full**: use the complete baseline structure and expand traceability, alternatives, measurable non-functional requirements, threat handling, recovery, rollout, and ownership.
- Increase depth when uncertainty or risk demands it, even if the component itself is small. Explain the reason briefly.

### Adaptation rules

- For **generic use**, keep examples neutral and reusable.
- For **SaaS backends**, emphasise tenancy, auth, billing-adjacent concerns, API versioning, and observability.
- For **internal automation systems**, emphasise integrations, scheduling, idempotency, retries, auditability, and operator runbooks.
- For **compliance-sensitive systems**, strengthen security, threat modelling, access control, retention, incident response, and approval gates.
- For **event-driven or worker-heavy systems**, expand async processing, ordering, retries, dead-letter handling, and recovery procedures.
- For **platform or integration layers**, expand contract ownership, versioning, backpressure, dependency isolation, and operational boundaries.

### Writing standards

- Be specific rather than academic.
- State assumptions near the top.
- Separate facts from recommendations.
- Make trade-offs explicit.
- Avoid filler sections with no operational value.
- If the user gave little context, write a high-quality generic pack and label assumptions.
- Prefer tables for requirement inventories, risks, decisions, and rollout stages when they improve scanability.
- Include concrete defaults when the user did not specify one, but label them as recommendations rather than requirements.

## Final quality gate

Before returning the pack, verify that:
- non-functional requirements are measurable or explicitly marked as unresolved
- assumptions, facts, and recommendations are distinguishable
- major decisions, risks, and open questions have an owner or a proposed owner when ownership matters
- critical failure, rollback, and recovery paths are addressed
- security and data-lifecycle obligations match the system's sensitivity
- tests trace to the important requirements, migrations, and recovery procedures
- empty or purely ceremonial sections have been removed

## Research guidance

When browsing, look for the minimum official material needed to strengthen the pack. Common examples:
- API design standards and OpenAPI guidance
- Cloud architecture guidance such as reliability, security, and operational excellence frameworks
- Security and threat-modelling guidance
- SLO or reliability guidance
- Database or queue design documentation
- Vendor documentation for managed services the user mentions

Do not overwhelm the output with citations. Use citations where they materially support standards, constraints, or recommended practices.

## Sourcing and citation contract

When research was used:
- Distinguish sourced facts from your recommendations.
- Link sources inline or in a short `Sources` section at the end.
- Cite only the claims that benefit from verification such as limits, semantics, standards, security guidance, and managed-service behavior.

When research was not used:
- Do not fabricate citations.
- Say that the plan is based on general engineering judgment if that distinction matters.

## Response pattern

Follow this pattern unless the user asks for something else:

1. Title
2. Short context summary or assumptions
3. Backend planning pack at the selected depth
4. Key trade-offs and immediate next steps
5. Optional: sources, only when research was used

## If the user asks for a template only

Return a clean, reusable version of the template from `references/template.md` with minimal commentary.

## If the user asks for critique or review

Keep the original structure where practical. Identify gaps in:
- scope
- non-functional requirements
- data design
- security and threat handling
- reliability and recovery
- deployment and rollback
- observability
- risks and decision records

Provide a revised version when the user requests one or when the revision is reasonably bounded and materially more useful than findings alone. Otherwise provide prioritised, actionable changes without duplicating the entire document.
