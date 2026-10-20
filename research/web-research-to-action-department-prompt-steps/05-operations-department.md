# 5. Operations Department

## Step 1 — Web Data Collection

```text
You are helping the Operations team collect public supplier or service-provider research.

Review public web information about a supplier, logistics provider, outsourcing partner, or operational service provider, including:
- services page
- locations served
- service levels
- industries served
- customer examples
- certifications
- support channels
- implementation process

Collect the information into this format:

{
  "source_url": "",
  "source_title": "",
  "supplier_name": "",
  "service_category": "",
  "locations_served": [],
  "services_offered": [],
  "industries_served": [],
  "service_level_signals": [],
  "certifications_or_standards": [],
  "implementation_notes": [],
  "operational_risk_signals": [],
  "raw_notes": ""
}

Do not invent facts. If information is unavailable, use null or an empty array.
```

## Step 2 — Extraction

```text
Convert the pasted public supplier research into a structured operations review record.

Extract:
- supplier name
- service category
- services offered
- locations served
- industries served
- operational capabilities
- service-level signals
- certifications or standards
- implementation considerations
- operational risk flags
- confidence level

Return valid JSON only.
```

## Step 3 — Department Analysis

```text
Analyse this supplier record for Operations.

Assess:
- operational fit
- service coverage
- reliability signals
- implementation complexity
- dependency risk
- scalability
- missing information required before shortlisting

Recommend one of:
- Shortlist
- Monitor
- Needs more information
- Not suitable based on available data
```

## Step 4 — Insight Brief

```text
Create an operations supplier brief.

Use this structure:

## Supplier Snapshot
Summarise the supplier and its services.

## Operational Fit
Explain where the supplier may fit our operations.

## Strengths
List positive capability or coverage signals.

## Risks and Unknowns
List operational risks and missing information.

## Recommendation
Give a practical shortlisting recommendation.

## Next Action
State what Operations should verify next.
```

## Step 5 — App/Plugin Action

```text
Create a supplier review record.

Fields:
- supplier_name
- service_category
- source_url
- services_offered
- locations_served
- operational_fit
- risk_flags
- missing_information
- recommendation
- status

Set status to "Ready for operations review".
```

---

