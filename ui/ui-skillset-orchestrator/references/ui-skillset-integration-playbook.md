# UI Skillset Integration Playbook

## Layered Model
1. Foundations
2. UX and Information Architecture
3. Design Systems and Component Architecture
4. Frontend Implementation
5. Data and Dashboard UI
6. AI-Aware UI
7. Asset Generation and Visual Automation
8. Tooling and Workflow
9. Performance and Optimisation
10. Strategic UI Architecture

## Scope-based routes

| Request | Primary owner | Conditional handoff |
| --- | --- | --- |
| Audit a screen without edits | Foundations | UX for flow problems; dashboard or AI specialist for domain risks |
| Fix alignment, type, or spacing | Foundations + implementation | System owner only for a shared component/token issue |
| New flow or onboarding | UX | System and implementation; foundations for visual verification |
| New marketing page | UX + foundations + implementation | Assets only if the brief needs them |
| Data workbench | Dashboard + implementation | AI trust when suggestions/approvals are present |
| Slow interaction | Performance | Implementation for the measured bottleneck |
| Native Windows screen | Native-platform review | Optional installed WinUI skills or project guidance, not web styling rules |
| Portfolio or shared-theme change | Strategic architecture + design system | Relevant product specialists |

Use only applicable routes. Existing functioning flows and token contracts are inputs, not deliverables to regenerate.

## Surface purpose

- Task-focused: familiar controls, useful density, predictable state, correction and recovery.
- Persuasive: a clear offer, distinctive but appropriate presentation, supported evidence, a next action.
- Reading: navigation, reading order, comfortable text, information retrieval.
- Experiential: the work itself, with unobtrusive navigation and accessible alternatives.

A product may contain all four. A dashboard and its public landing page need different priorities. Preserve the user's chosen direction during refinement; ask only when missing information materially changes the result.

## Feedback Loops
- UX feedback updates IA and interaction design.
- Implementation constraints update component standards.
- Performance findings update architecture and dependency policy.
- Strategic shifts update layer priorities and roadmap.

## Ownership and handoff

Foundations owns visual judgment and baseline usability; UX owns task structure and copy; systems owns reusable contracts; implementation owns behavior; tooling owns verification handoffs. Domain specialists retain their constraints. Keep detailed rules with their owner rather than copying whole checklists across skills.

Pass a target/revision, intent, preserved constraints, issue evidence, owner, and acceptance check. Recheck stale findings before applying them. Do not make one specialist invoke the orchestrator recursively.

Local adaptation, 2026-10-03. See [source attribution](impeccable-attribution.md).
