---
name: ui-ai-aware-design
description: Design trustworthy AI-enabled interfaces with confidence signaling, explainability, approval controls, and feedback capture. Use when a UI presents AI outputs, supports human review, or requires auditable human-in-the-loop decision workflows.
---

# UI AI Aware Design

## Objective
Embed AI into interface workflows without sacrificing trust, control, or accountability.

## Workflow
1. Define where AI assists versus where humans decide.
2. Design confidence indicators that communicate uncertainty clearly.
3. Add explainability surfaces with progressive disclosure.
4. Implement approve, reject, and edit-before-approve controls.
5. Support batch review with prioritization for low-confidence items.
6. Capture structured user feedback and preserve review context.
7. Ensure auditability for overrides and final decisions.

## Trust Rules
- Avoid false precision and overconfident visual cues.
- Show numerical confidence only when its source, meaning and calibration are established for the task. Model self-confidence is not a calibrated probability; do not invent percentages. Otherwise communicate evidence, missing checks and uncertainty in words.
- Separate AI suggestion state from confirmed system state.
- Keep ownership boundaries explicit at every decision point.
- Surface limitations and model uncertainty in plain language.
- Optimize for correction and override speed, not blind acceptance.
- Visual polish or simplification must preserve evidence access, uncertainty, approval ownership, and override controls. Do not merge AI suggestions with confirmed records or conceal consequential actions to make a screen look cleaner.

## Deliverable Format
- Human-in-the-loop process diagram.
- Confidence and explainability specification.
- Approval and override interaction model.
- Feedback schema for model improvement loops.
- Audit requirements and retention notes.

## Layer Position
Layer 6 (AI-Aware UI). Apply on top of stable data and workflow patterns.
## Resources
- Read `references/ai-trust-review-checklist.md` when validating confidence, explainability, and human-override safety.
