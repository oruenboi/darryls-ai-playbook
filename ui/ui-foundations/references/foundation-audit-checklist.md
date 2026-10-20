# Foundation Audit Checklist

Use this checklist for reviews or scoped refinements, not permission to redesign. Resolve the screen, audience, primary task, existing visual system, and supported environments. Preserve useful existing choices; unfamiliarity or a popular design pattern alone is not a defect.

## Visual
- Follow the project's spacing scale. Group related labels and controls; separate distinct tasks. Check optical alignment as well as equal CSS values.
- Verify typography hierarchy is consistent across headings and body.
- Verify primary action is visually dominant on each screen.
- Test real headings, long names, numbers, and text expansion: wrapping, truncation, line height, and prose measure must fit their role. Dense tables need not use article typography.
- Determine whether prominent content explains this product and supports the user's task. Repeated generic cards may hide structure, but cards, system fonts, neutral colors, and eyebrow labels are valid when purposeful.
- Keep claims, units, citations, and domain terminology accurate. Do not invent metrics, testimonials, or feature promises to make the design convincing.
- Distinguish measured issues (clipping, missing names, poor contrast) from judgments (weak hierarchy, interchangeable composition). Support judgments with the visible element, the competing signal, and its effect on the task.

## Interaction
- Verify all interactive elements have default, hover, focus, and disabled states.
- Verify error and success feedback appears near the source of action.
- Verify loading and empty states are explicit and actionable.
- Walk arrival, primary action, pending/result, and recovery paths where implemented. A polished screenshot does not establish that controls work.
- Check whether motion explains change and remains optional where needed. Do not add animation just to signal effort.

## Accessibility
- Verify contrast meets WCAG targets for text and controls.
- Verify keyboard tab order is logical and focus is visible.
- Verify semantic HTML is used for landmarks and forms.
- Test focus, zoom/text scaling, and reduced motion where supported. Verify applicable standards before asserting numerical compliance; tool scores and screenshots do not certify accessibility.

## Responsive
- Verify core workflows work at mobile, tablet, and desktop widths.
- Verify touch targets are large enough and not tightly packed.
- Verify layouts reflow without unintended page overflow. A deliberately scrollable wide data table can be appropriate if users can reach all columns and controls.
- Batch representative wide and narrow views, including the longest realistic content and changed interaction states. Viewport emulation is not a touch-device test; label what was actually exercised.

## Report and stopping point

Lead with blocked tasks, misleading state, inaccessible controls, or data risk; then flow and system drift; then cosmetic improvements. Give each finding a specific target, evidence, impact, suggested repair, and verification step. Retain strengths worth preserving. Do not pad the report with arbitrary aesthetic violations or scores.

When editing is authorized, repair a coherent batch and confirm the affected checks. Avoid indefinite cosmetic iteration. If the browser or app cannot run, use source or current screenshots and mark interaction/visual uncertainty explicitly; do not install a runtime to complete a checklist.

Local adaptation, 2026-10-03. See [source attribution](impeccable-attribution.md).
