# 7. Legal and Compliance Department

## Step 1 — Web Data Collection

```text
You are helping the Legal and Compliance team collect public regulatory or policy intelligence.

Review public web information such as:
- regulator updates
- enforcement notices
- consultation papers
- policy updates
- terms of service
- privacy policies
- compliance guidance
- industry notices

Collect the information into this format:

{
  "source_url": "",
  "source_title": "",
  "issuing_body_or_company": "",
  "document_type": "",
  "publication_date": "",
  "affected_sector": "",
  "key_obligations_or_changes": [],
  "risk_topics": [],
  "deadlines_or_effective_dates": [],
  "penalties_or_consequences": [],
  "uncertainties": [],
  "raw_notes": ""
}

Do not invent facts. If information is unavailable, use null or an empty array.
```

## Step 2 — Extraction

```text
Convert the pasted public regulatory, legal, policy, or compliance content into a structured compliance intelligence record.

Extract:
- issuing body or company
- document type
- publication date
- affected sector
- key obligations or changes
- risk topics
- deadlines or effective dates
- penalties or consequences
- uncertainties
- confidence level

Return valid JSON only.
```

## Step 3 — Department Analysis

```text
Analyse this compliance intelligence record.

Assess:
- relevance to our organisation
- affected departments
- legal or compliance risk level
- urgency
- required business actions
- whether external legal advice may be needed
- missing information to verify

Do not provide legal advice. Provide a practical compliance triage summary.
```

## Step 4 — Insight Brief

```text
Create a legal/compliance watch brief.

Use this structure:

## Source Summary
Summarise the public update or document.

## Why It Matters
Explain the possible business relevance.

## Potential Obligations or Risks
List obligations, restrictions, deadlines, or risk areas.

## Affected Departments
Identify which teams should review this.

## Recommended Action
Give a practical compliance next step.

## Legal Review Needed?
State whether legal or senior compliance review is recommended.
```

## Step 5 — App/Plugin Action

```text
Create a compliance watch record.

Fields:
- source_title
- issuing_body_or_company
- source_url
- document_type
- publication_date
- affected_sector
- risk_level
- affected_departments
- recommended_action
- legal_review_needed
- status

Set status to "Ready for compliance review".
```

---

