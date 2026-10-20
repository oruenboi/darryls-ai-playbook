---
name: ui-performance-optimisation
description: Improve real and perceived UI performance through loading strategy, optimistic interactions, lazy loading, and bundle controls. Use when performance bottlenecks, slow UX perception, or scalability regressions need structured remediation.
---

# UI Performance Optimisation

## Objective
Deliver responsive experiences under real-world constraints while preventing performance regressions.

## Workflow
1. Identify user-critical paths and baseline current performance.
2. Improve perceived speed with immediate feedback and skeleton patterns.
3. Apply optimistic UI where rollback and conflict handling are reliable.
4. Introduce lazy loading and route/component code splitting.
5. Reduce bundle pressure and avoid unnecessary dependencies.
6. Validate outcomes with repeatable measurement and regression checks.

## Optimization Rules
- Prioritize above-the-fold rendering on key screens.
- Avoid layout shift during load and update phases.
- Make pending and rollback states explicit.
- Split heavy features behind clear loading boundaries.
- Track performance impact of every major dependency change.

## Deliverable Format
- Bottleneck report with likely root causes.
- Remediation plan ranked by impact and complexity.
- Expected metric movement and validation method.
- Regression guardrails for future releases.

## Layer Position
Layer 9 (Performance and Optimisation). Apply continuously across all previous layers.
## Resources
- Read `references/performance-budget-template.md` to define measurable performance targets.
- Run `scripts/web_perf_snapshot.py` to summarize baseline and candidate Lighthouse metric deltas.
- This helper reads existing report files; it does not run Lighthouse or measure a website. Times are reported in milliseconds and CLS is unitless. Missing metrics remain unavailable; TTI is a legacy comparison where present, not a universal gate.
