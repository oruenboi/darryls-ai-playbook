# 2. Marketing Department

## Step 1 — Web Data Collection

```text
You are helping the Marketing team collect public competitor intelligence.

Review public web information from a competitor, including:
- homepage
- product or service pages
- pricing page, if available
- blog or resources page
- case studies
- landing pages
- social proof, testimonials, or customer logos

Collect the information into this format:

{
  "source_url": "",
  "source_title": "",
  "competitor_name": "",
  "positioning_statement": "",
  "target_audience": [],
  "main_messages": [],
  "offers_or_ctas": [],
  "content_themes": [],
  "proof_points": [],
  "pricing_or_packaging_notes": [],
  "raw_notes": ""
}

Do not invent facts. If information is unavailable, use null or an empty array.
```

## Step 2 — Extraction

```text
Convert the pasted public competitor research into a structured marketing intelligence record.

Extract:
- competitor name
- positioning
- target audience
- key messages
- emotional hooks
- calls to action
- content themes
- proof points
- pricing signals
- confidence level

Return valid JSON only.
```

## Step 3 — Department Analysis

```text
Analyse this competitor record for Marketing.

Identify:
- strongest positioning theme
- likely target segment
- repeated messaging patterns
- content gaps we could exploit
- differentiation opportunities
- campaign ideas inspired by the research

Do not copy the competitor's wording. Focus on strategic insight.
```

## Step 4 — Insight Brief

```text
Create a competitor marketing brief.

Use this structure:

## Competitor Snapshot
Short summary of who they target and how they position themselves.

## Messaging Themes
List the main themes found.

## What They Emphasise
Summarise their strongest claims or proof points.

## Gaps and Opportunities
Identify where our marketing could differentiate.

## Recommended Campaign Idea
Suggest one practical campaign, content, or landing-page idea.

## Next Action
Recommend what Marketing should do next.
```

## Step 5 — App/Plugin Action

```text
Create a competitor intelligence record.

Fields:
- competitor_name
- source_url
- target_audience
- main_messages
- content_themes
- differentiation_opportunities
- recommended_campaign_idea
- priority
- status

Set status to "Ready for marketing review".
```

---

