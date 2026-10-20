# Performance Budget Template

Use this template to define and enforce UI performance targets.

## Core Targets
- Largest Contentful Paint (LCP): [target]
- Interaction to Next Paint (INP): [target]
- Cumulative Layout Shift (CLS): [target]
- Time to Interactive (TTI): [target]

## Bundle Budgets
- Initial JS total: [target KB]
- Route-level chunk cap: [target KB]
- Third-party script cap: [target KB]

## Guardrails
- Require baseline and post-change measurements.
- Block merges that exceed agreed thresholds.
- Track trend over time, not single-run noise.

## Visual-work cost checks

Measure against representative devices, content, cache/network conditions, and the same build settings. Separate laboratory results from field observations; do not infer faster interaction from a screenshot or a smaller source file. Select current relevant metrics from the project's measurement tools; retain TTI only for legacy comparisons rather than making it a universal gate.

Inspect font loading, image dimensions/sources, layout shifts, and effects that cause paint or layout work. Do not lazy-load the critical first-view image by default. Add memoization, dependency changes, or complex animation machinery only for a demonstrated need.

Motion should help users understand state, remain interruptible, and respect reduced-motion preferences. Avoid adding effects solely to demonstrate polish. Recheck feedback and focus when reducing motion; removing animation must not remove the state change itself.

Local adaptation, 2026-10-03. See [source attribution](impeccable-attribution.md).
