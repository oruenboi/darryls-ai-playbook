# 8. Customer Success Department

## Step 1 — Web Data Collection

```text
You are helping the Customer Success team collect public voice-of-customer research.

Review public web information such as:
- customer reviews
- testimonials
- community discussions
- help centre articles
- product comparison pages
- public complaints
- app marketplace reviews
- case studies

Collect the information into this format:

{
  "source_url": "",
  "source_title": "",
  "company_or_product": "",
  "customer_segment": "",
  "positive_themes": [],
  "negative_themes": [],
  "feature_requests": [],
  "support_or_service_issues": [],
  "onboarding_or_adoption_signals": [],
  "retention_risk_signals": [],
  "raw_notes": ""
}

Do not invent facts. If information is unavailable, use null or an empty array.
```

## Step 2 — Extraction

```text
Convert the pasted public customer feedback or review research into a structured customer-success insight record.

Extract:
- company or product
- customer segment
- positive themes
- negative themes
- feature requests
- support issues
- onboarding issues
- retention risk signals
- opportunity signals
- confidence level

Return valid JSON only.
```

## Step 3 — Department Analysis

```text
Analyse this customer feedback record for Customer Success.

Identify:
- recurring customer pain points
- adoption barriers
- support improvement opportunities
- retention risk signals
- upsell or expansion signals
- onboarding improvements
- recommended customer-success action

Focus on practical service improvements.
```

## Step 4 — Insight Brief

```text
Create a Customer Success insight brief.

Use this structure:

## Customer Feedback Snapshot
Summarise the main feedback themes.

## Positive Signals
List what customers seem to value.

## Pain Points
List complaints, frustrations, or adoption barriers.

## Retention Risks
Highlight issues that could cause churn.

## Recommended CS Action
Suggest a practical support, onboarding, or retention action.

## Next Action
State what the CS team should do next.
```

## Step 5 — App/Plugin Action

```text
Create a customer-success insight record.

Fields:
- company_or_product
- source_url
- customer_segment
- positive_themes
- negative_themes
- retention_risk_signals
- recommended_cs_action
- priority
- status

Set status to "Ready for CS review".
```

---

