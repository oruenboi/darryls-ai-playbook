# 3. HR Department

## Step 1 — Web Data Collection

```text
You are helping the HR team collect public talent-market research.

Review public job postings or career pages for a target role, including:
- job title
- employer
- location
- responsibilities
- required skills
- qualifications
- benefits
- salary range, if available
- working arrangement

Collect the information into this format:

{
  "source_url": "",
  "source_title": "",
  "employer_name": "",
  "job_title": "",
  "location": "",
  "work_arrangement": "",
  "responsibilities": [],
  "required_skills": [],
  "qualifications": [],
  "tools_or_technologies": [],
  "benefits": [],
  "salary_range": "",
  "raw_notes": ""
}

Do not invent facts. If information is unavailable, use null or an empty array.
```

## Step 2 — Extraction

```text
Convert the pasted public job posting or career-page research into a structured HR talent-market record.

Extract:
- job title
- employer
- location
- work arrangement
- key responsibilities
- required skills
- preferred skills
- tools or systems mentioned
- benefits
- salary signals
- seniority level
- confidence level

Return valid JSON only.
```

## Step 3 — Department Analysis

```text
Analyse this talent-market record for HR.

Identify:
- common role expectations
- must-have skills
- nice-to-have skills
- compensation or benefits signals
- hiring competitiveness
- implications for our own job description
- gaps in our current hiring approach

Keep the analysis practical for a hiring manager.
```

## Step 4 — Insight Brief

```text
Create an HR talent-market brief.

Use this structure:

## Role Snapshot
Summarise the role and market expectations.

## Skills in Demand
List the most important skills and tools.

## Benefits and Work Arrangement Signals
Summarise what competitors are offering.

## Hiring Implications
Explain what this means for our own hiring.

## Recommended Job Description Improvements
Suggest practical changes.

## Next Action
Recommend what HR should do next.
```

## Step 5 — App/Plugin Action

```text
Create a talent-market research record.

Fields:
- job_title
- employer_name
- source_url
- required_skills
- benefits
- salary_range
- work_arrangement
- hiring_competitiveness
- recommended_jd_changes
- status

Set status to "Ready for HR review".
```

---

