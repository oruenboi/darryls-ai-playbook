# 10. Admin / Executive Office

## Step 1 — Web Data Collection

```text
You are helping the Admin or Executive Office team collect public business research.

Review public web information about a company, vendor, partner, event, industry body, or business opportunity, including:
- organisation website
- About page
- leadership page
- services page
- news or press page
- event page
- public contact information
- partnership or membership information

Collect the information into this format:

{
  "source_url": "",
  "source_title": "",
  "organisation_name": "",
  "organisation_type": "",
  "key_people": [],
  "services_or_activities": [],
  "business_relevance": "",
  "event_or_partnership_notes": [],
  "contact_or_follow_up_details": [],
  "risk_or_reputation_signals": [],
  "raw_notes": ""
}

Do not invent facts. If information is unavailable, use null or an empty array.
```

## Step 2 — Extraction

```text
Convert the pasted public business research into a structured executive-office research record.

Extract:
- organisation name
- organisation type
- key people
- services or activities
- business relevance
- partnership or event notes
- contact or follow-up details
- risk or reputation signals
- confidence level

Return valid JSON only.
```

## Step 3 — Department Analysis

```text
Analyse this business research record for the Executive Office.

Assess:
- strategic relevance
- relationship opportunity
- reputational considerations
- follow-up value
- whether leadership attention is required
- missing information
- recommended next action

Keep the output concise and decision-oriented.
```

## Step 4 — Insight Brief

```text
Create an executive research brief.

Use this structure:

## Organisation Snapshot
Summarise who the organisation is.

## Strategic Relevance
Explain why it may matter.

## Opportunity or Risk
List potential relationship, partnership, event, or reputational points.

## Recommended Follow-Up
Suggest a practical next step.

## Leadership Attention Needed?
State whether this should be escalated.

## Next Action
Give one clear action item.
```

## Step 5 — App/Plugin Action

```text
Create an executive research record.

Fields:
- organisation_name
- source_url
- organisation_type
- strategic_relevance
- opportunity_or_risk
- recommended_follow_up
- leadership_attention_needed
- status

Set status to "Ready for executive review".
```

---

