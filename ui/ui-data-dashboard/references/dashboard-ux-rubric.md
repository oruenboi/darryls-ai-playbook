# Data Dashboard UX Rubric

Use this rubric for data-heavy screens.

## Tables and Filters
- Column priority reflects user tasks.
- Sorting and filters are visible and reversible.
- Filter state persistence is defined.

## Editing and Auditability
- Inline edits support save, cancel, and validation feedback.
- Status indicators combine text and icon where critical.
- Audit logs capture who, what, and when.

## Density and Performance
- Density settings maintain readability.
- Skeleton states match final layout shape.
- Pagination versus infinite scroll is justified by task model.

## Numerical and decision clarity

Align comparable numbers consistently; use tabular numerals where they aid scanning. Keep currencies, units, dates, time zones, and sign conventions explicit. Distinguish zero, unavailable, pending, and estimated values. Check whether a summary describes all records, the filtered set, or selected items; make that scope visible when ambiguity would affect decisions.

Status needs text or another independent accessible meaning, not color alone. Preserve customer/record identity and critical values when narrowing a table; deliberate horizontal scrolling can be better than hiding decision-critical columns. Verify that menus and row actions remain reachable, including with keyboard input.

Distinguish no records from no matching results and from a failed request. Preserve active filters and a clear reset path. Skeletons are useful for known layouts, but loading feedback should match the actual operation rather than a blanket visual rule.

Keep task controls and shared components consistent; avoid entrance choreography or display typography that slows routine scanning. Retain evidence, uncertainty, and human approval when AI suggestions appear. A simplification request does not authorize combining suggested and approved states.

Local adaptation, 2026-10-03. See [source attribution](impeccable-attribution.md).
