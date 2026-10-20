# 4. Finance Department

## Step 1 — Web Data Collection

```text
You are helping the Finance team collect public vendor and pricing research.

Review public web information about a vendor, SaaS tool, or service provider, including:
- pricing page
- product page
- plan tiers
- usage limits
- implementation fees, if available
- support terms
- billing frequency
- cancellation or contract notes

Collect the information into this format:

{
  "source_url": "",
  "source_title": "",
  "vendor_name": "",
  "product_or_service": "",
  "pricing_model": "",
  "plan_tiers": [],
  "published_prices": [],
  "usage_limits": [],
  "contract_terms": [],
  "support_or_service_notes": [],
  "hidden_cost_signals": [],
  "raw_notes": ""
}

Do not invent facts. If information is unavailable, use null or an empty array.
```

## Step 2 — Extraction

```text
Convert the pasted public vendor or pricing research into a structured finance review record.

Extract:
- vendor name
- product or service
- pricing model
- published prices
- plan tiers
- usage limits
- contract terms
- potential hidden costs
- implementation or migration notes
- support level
- confidence level

Return valid JSON only.
```

## Step 3 — Department Analysis

```text
Analyse this vendor pricing record for Finance.

Assess:
- cost transparency
- likely total cost drivers
- budget risk
- billing complexity
- value-for-money signals
- contract or lock-in risk
- missing information required before approval

Recommend one of:
- Worth shortlisting
- Needs more information
- High cost risk
- Not suitable based on available data
```

## Step 4 — Insight Brief

```text
Create a finance vendor-pricing brief.

Use this structure:

## Vendor Snapshot
Summarise the vendor and product/service.

## Pricing Summary
Explain the public pricing model and known cost points.

## Cost Risks
List possible hidden costs, lock-in risks, or usage-based risks.

## Budget Considerations
Explain what Finance should verify before approval.

## Recommendation
Give a practical recommendation.

## Next Action
State what information should be requested from the vendor.
```

## Step 5 — App/Plugin Action

```text
Create a vendor pricing review record.

Fields:
- vendor_name
- product_or_service
- source_url
- pricing_model
- published_prices
- cost_risks
- missing_information
- recommendation
- status

Set status to "Ready for finance review".
```

---

