# Web Research-to-Action Copilot  
## Department Prompt Steps for Hands-On Labs

**Workshop flow:**  
Public web data → structured dataset → department analysis → insight brief → app/plugin action

**Important class instruction:**  
Use only public information. Do not use confidential company, client, employee, or customer data during the lab.

---

## Universal Lab Flow

Each department should follow these five steps:

1. **Collect public web data**  
   Gather relevant information from public websites, public pages, public documents, or public listings.

2. **Extract structured data**  
   Convert messy web notes into clean JSON.

3. **Analyse for department relevance**  
   Assess risks, opportunities, priority, and recommended action.

4. **Generate an insight brief**  
   Produce a concise department-ready summary.

5. **Prepare app/plugin action payload**  
   Create the structured record that would be saved into the workshop app or exposed through plugin-style tools.

---

---

# Universal Orchestration Prompt

Use this after completing the department-specific steps.

```text
You are the workflow orchestrator for a Web Research-to-Action Copilot.

Run the following workflow:

1. Take the raw public web research.
2. Use the extraction skill to convert it into structured JSON.
3. Use the department analysis skill to classify relevance, risks, opportunities, and recommended action.
4. Use the insight brief skill to produce a short department-ready brief.
5. Prepare an app/plugin action payload to create a research record.

Return the final output in this format:

{
  "source_summary": {
    "source_url": "",
    "source_title": "",
    "organisation_or_subject": ""
  },
  "structured_data": {},
  "department_analysis": {},
  "insight_brief": "",
  "plugin_action": {
    "tool_name": "",
    "payload": {}
  },
  "status": "Ready for human review"
}

Do not invent facts. Clearly mark missing or uncertain information.
```

---

# Universal Codex App-Building Prompt

```text
Build a simple Web Research Intelligence Tracker.

Use React, TypeScript, and a minimal Express backend.

The app should allow users to:
- create a new research record
- enter source URL, source title, department, and raw notes
- run a mock extraction function
- run a mock department analysis function
- generate a short insight brief
- view all research records in a table
- filter records by department
- update record status

Use in-memory storage for the workshop version.

Departments should include:
- Sales
- Marketing
- HR
- Finance
- Operations
- IT
- Legal/Compliance
- Customer Success
- Product
- Executive Office

Keep the code simple and readable for learners.

Include:
- frontend form
- record table
- detail view
- mock AI orchestration functions
- backend API routes
- README with setup and run instructions
```

---

# Universal Plugin / Tool Prompt

```text
Create an MCP-style tool layer for the Web Research Intelligence Tracker.

Expose these tools:

1. create_research_record
2. list_research_records
3. get_research_record
4. update_research_status
5. classify_research_record
6. generate_insight_brief

Each tool should have a clear description, input schema, and simple implementation using the app's existing data store.

Use mock data and in-memory storage for the workshop version.

The tools should support records with these fields:
- id
- department
- source_url
- source_title
- organisation_or_subject
- raw_notes
- structured_data
- analysis
- insight_brief
- status
- created_at
- updated_at

Keep the implementation beginner-friendly and include comments explaining each tool.
```

---

# Facilitator Notes

## Recommended delivery sequence

1. Ask each group to pick a department.
2. Ask each group to choose one public web source.
3. Run Step 1 manually.
4. Paste the collected notes into Step 2.
5. Use Step 3 to perform department-specific analysis.
6. Use Step 4 to create a brief.
7. Use Step 5 to create the app/plugin payload.
8. Use the universal orchestration prompt to show the end-to-end workflow.
9. Use the Codex app prompt to scaffold the workshop app.
10. Use the plugin/tool prompt to expose the workflow as callable actions.

## Suggested capstone demo

Each group should demonstrate:

1. The public web source they used.
2. The structured data extracted.
3. The department analysis.
4. The generated insight brief.
5. The app/plugin payload.
6. How this could become a reusable departmental AI workflow.

## Teaching message

The point of the lab is not just to generate text.

The point is to show how public web information can become:

- structured data,
- repeatable skills,
- orchestrated workflows,
- app records,
- and plugin-enabled business actions.

