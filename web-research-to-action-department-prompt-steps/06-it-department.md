# 6. IT Department

## Step 1 — Web Data Collection

```text
You are helping the IT team collect public software and security research.

Review public web information about a software tool, SaaS platform, or technology vendor, including:
- product page
- integrations page
- API documentation
- security page
- privacy page
- compliance page
- support documentation
- status page, if available

Collect the information into this format:

{
  "source_url": "",
  "source_title": "",
  "vendor_name": "",
  "tool_name": "",
  "core_functionality": [],
  "integrations": [],
  "api_or_automation_support": "",
  "security_features": [],
  "compliance_claims": [],
  "data_privacy_notes": [],
  "support_or_sla_notes": [],
  "technical_risk_signals": [],
  "raw_notes": ""
}

Do not invent facts. If information is unavailable, use null or an empty array.
```

## Step 2 — Extraction

```text
Convert the pasted public software or security research into a structured IT review record.

Extract:
- vendor name
- tool name
- core functionality
- integrations
- API or automation support
- authentication options
- security features
- compliance claims
- data privacy notes
- support or SLA notes
- technical risk flags
- confidence level

Return valid JSON only.
```

## Step 3 — Department Analysis

```text
Analyse this software vendor record for IT.

Assess:
- integration fit
- security posture based on public information
- data privacy considerations
- administration complexity
- automation potential
- support maturity
- missing technical information

Recommend one of:
- Technically promising
- Needs security review
- Needs more information
- Not suitable based on available data
```

## Step 4 — Insight Brief

```text
Create an IT software review brief.

Use this structure:

## Tool Snapshot
Summarise the tool and what it does.

## Integration and Automation Fit
Explain available integrations, API, or automation signals.

## Security and Privacy Notes
Summarise public security, compliance, and privacy information.

## Technical Risks
List risks, unknowns, and items needing IT review.

## Recommendation
Give a practical IT recommendation.

## Next Action
State what technical information should be requested or verified.
```

## Step 5 — App/Plugin Action

```text
Create a software review record.

Fields:
- vendor_name
- tool_name
- source_url
- integrations
- security_features
- compliance_claims
- technical_risk_flags
- recommendation
- status

Set status to "Ready for IT review".
```

---

