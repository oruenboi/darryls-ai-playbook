# 1. Sales Department

## Step 1 — Web Data Collection

```text
You are helping the Sales team collect public web research for lead qualification.

Find or review public web information about a potential B2B customer, including:
- company website
- About page
- Services or products page
- case studies
- news or press page
- leadership page, if available

Collect the information into this format:

{
  "source_url": "",
  "source_title": "",
  "company_name": "",
  "industry": "",
  "location": "",
  "company_size_signal": "",
  "products_or_services": [],
  "target_customers": [],
  "growth_signals": [],
  "pain_point_signals": [],
  "technology_or_process_signals": [],
  "raw_notes": ""
}

Do not invent facts. If information is unavailable, use null or an empty array.
```

## Step 2 — Extraction

```text
Convert the pasted public web research into a clean sales lead profile.

Extract:
- company name
- industry
- target customers
- likely business model
- growth signals
- possible pain points
- possible buying triggers
- relevant decision-maker clues
- confidence level

Return valid JSON only.
```

## Step 3 — Department Analysis

```text
Analyse this lead profile for Sales.

Score the company from 1 to 5 on:
- fit with our offering
- urgency of potential need
- ability to pay
- ease of outreach
- strategic value

Then recommend one of:
- High-priority lead
- Nurture lead
- Low-priority lead
- Not enough information

Explain the reasoning briefly and list the top three outreach angles.
```

## Step 4 — Insight Brief

```text
Create a sales qualification brief.

Use this structure:

## Lead Summary
Who the company is and what they appear to do.

## Why This Company May Be Relevant
List the clearest buying signals.

## Possible Pain Points
List plausible issues based only on the collected evidence.

## Recommended Outreach Angle
Suggest a practical first-message angle.

## Missing Information
List what a salesperson should verify.

## Next Action
Recommend the next sales step.
```

## Step 5 — App/Plugin Action

```text
Create a lead research record using the extracted sales profile.

Fields:
- company_name
- industry
- source_url
- lead_score
- priority
- outreach_angle
- missing_information
- recommended_next_action
- status

Set status to "Ready for sales review".
```

---

