# AI Trust Review Checklist

Use this checklist when AI outputs appear in UI.

## Confidence and Explainability
- Confidence is shown with clear wording and no false precision.
- Numerical confidence has a documented source and task-relevant calibration; model self-ratings are not presented as verified probabilities. Where calibration is unavailable, use evidence and verification states rather than fabricated scores.
- Explanations are available at summary and deep-detail levels.
- Limitations are visible near critical AI actions.

## Human Control
- Users can approve, reject, and edit before finalization.
- Manual checkpoints exist for high-impact decisions.
- Override actions are clearly logged.

## Feedback and Audit
- Structured feedback supports correct, incorrect, and partial outcomes.
- Feedback submission is low friction.
- Audit trail captures decision ownership and timestamps.
