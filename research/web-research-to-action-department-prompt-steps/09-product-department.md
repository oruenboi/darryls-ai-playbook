# 9. Product Department

## Step 1 — Web Data Collection

```text
You are helping the Product team collect public product intelligence.

Review public web information such as:
- competitor feature pages
- changelogs
- release notes
- documentation
- integration pages
- product comparison pages
- customer-request forums
- roadmap pages, if available

Collect the information into this format:

{
  "source_url": "",
  "source_title": "",
  "company_or_product": "",
  "feature_area": "",
  "features_identified": [],
  "integrations": [],
  "workflow_or_use_case": "",
  "user_segment": "",
  "differentiation_signals": [],
  "product_gap_signals": [],
  "raw_notes": ""
}

Do not invent facts. If information is unavailable, use null or an empty array.
```

## Step 2 — Extraction

```text
Convert the pasted public product research into a structured product intelligence record.

Extract:
- company or product
- feature area
- features identified
- integrations
- workflow or use case
- user segment
- differentiation signals
- product gap signals
- customer value proposition
- confidence level

Return valid JSON only.
```

## Step 3 — Department Analysis

```text
Analyse this product intelligence record.

Identify:
- relevant feature trends
- possible product gaps
- competitor strengths
- potential differentiation opportunities
- integration opportunities
- user problems being addressed
- whether this should influence roadmap discussions

Keep the analysis practical for a product manager.
```

## Step 4 — Insight Brief

```text
Create a product intelligence brief.

Use this structure:

## Product Snapshot
Summarise the feature, workflow, or product area.

## What Competitors or Alternatives Offer
List relevant features and capabilities.

## User Value
Explain what user problem this appears to solve.

## Gap or Opportunity
Identify possible roadmap or differentiation opportunities.

## Recommendation
Suggest whether this should be explored, ignored, or monitored.

## Next Action
State what Product should do next.
```

## Step 5 — App/Plugin Action

```text
Create a product intelligence record.

Fields:
- company_or_product
- source_url
- feature_area
- features_identified
- integrations
- product_gap_signals
- differentiation_opportunities
- recommendation
- status

Set status to "Ready for product review".
```

---

