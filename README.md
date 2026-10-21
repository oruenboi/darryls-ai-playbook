# Darryl's AI Playbook

Practical AI skills, workflows and playbooks curated by Darryl Wong.

This repository is intended for a closed practitioner community. It focuses on reusable Codex skills, review checklists, templates, and operating patterns that help professionals deliver accounting, compliance, corporate secretarial, and client advisory work with stronger AI support.

## Official Skill Repositories

- [OpenAI Skills](https://github.com/openai/skills)
- [Anthropic Skills](https://github.com/anthropics/skills)

## External Skills Disclaimer

Skills from external repositories should be treated like third-party code. Review the instructions, scripts, dependencies, and requested permissions before installing or running them. Do not use external skills with client data, credentials, or confidential practice information unless the source is trusted, the skill has been reviewed, and the data handling risk is acceptable for your firm.

## Catalog

Skills and workflows are grouped into broad subject folders.
Choose a category by the job the skill supports, not by its author or model provider.

Folder paths have changed: links or installation commands using the previous root-level paths must include the category now. Skill names and invocation names are unchanged. Select the individual skill folder containing `SKILL.md`, not its category folder.

### Accounting

- [Bank-to-books bookkeeping](accounting/bookkeeping-agent-bank2books/)
- [DBS-to-Xero bank import conversion](accounting/dbs-xero-csv/)

### Compliance & Corporate Services

- [Singapore AML/CTF screening](compliance/sg-aml-ctf-screening-tool/)
- [Singapore corporate secretarial workflows](compliance/sg-corpsec-private/)
- [Singapore KYC, CDD and EDD](compliance/sg-kyc-cdd-edd/)

### Infrastructure & Integrations

- [Agent Infrastructure Operator](infrastructure/agent-infrastructure-operator/) — inspect, diagnose and verify local or hosted agent infrastructure, with narrow permissions, user-facing evidence and rollback. Includes platform-check references and an operator-report template. Structural validation passed; live infrastructure behaviour has not been tested as part of this publication.
- [Xero Client API Access](infrastructure/xero-client-api-access/) — connect and verify explicitly selected client organisations. Includes a Windows-only Python 3.11+ PKCE helper, user-bound encrypted token storage, a synthetic configuration example and 10 passing synthetic tests. No live Xero connection was tested for this publication; recheck current provider scopes, limits and terms before use.
- [Backend Planning Pack](infrastructure/backend-planning-pack/) — optional advanced skill for planning integrations, internal tools and services. Includes a planning template and SaaS/event-driven checklists; it produces plans, not a deployed backend.

### Practice Productivity

- [Document-to-Markdown conversion](productivity/document-to-md/)
- [Skill orchestration planning](productivity/skill-orchestration-planner/)

### Learning & Research

- [AI visibility audits](research/ai-visibility-audit/)
- [Web research-to-action prompt steps](research/web-research-to-action-department-prompt-steps/)

### UI & User Experience

[Browse the UI collection](ui/) for client portals, internal workbenches and AI review interfaces.

- **Start here:** [UI Skillset Orchestrator](ui/ui-skillset-orchestrator/) selects the smallest relevant set; it does not require all skills for every task.
- **Core:** [Foundations](ui/ui-foundations/), [UX & information architecture](ui/ui-ux-information-architecture/), [Frontend implementation](ui/ui-frontend-implementation/), [Data dashboards](ui/ui-data-dashboard/), [AI-aware design](ui/ui-ai-aware-design/).
- **Advanced / optional:** [Design systems](ui/ui-design-system-architecture/), [Asset automation](ui/ui-asset-visual-automation/), [Tooling workflow](ui/ui-tooling-workflow/), [Performance](ui/ui-performance-optimisation/), [Strategic architecture](ui/ui-strategic-architecture/).

## Usage Principles

- Treat AI outputs as draft work until reviewed by a qualified professional.
- Keep client data confidential and avoid committing live client files.
- Prefer repeatable workflows over one-off prompts.
- Include clear inputs, expected outputs, review steps, and escalation points in every shared skill.
- Maintain human approval checkpoints for filings, financial statements, compliance conclusions, and client-facing advice.

## Contributing

New skills should include:

- `SKILL.md` with trigger conditions and workflow instructions
- `assets/` for reusable templates or examples
- `references/` for supporting guidance
- `scripts/` for tested automation helpers, where relevant

Add each skill to the most relevant catalog category with a short purpose and any platform restrictions. Include all resources needed by its instructions, distinguish synthetic tests from live verification, and keep client configuration and credentials outside shared skill packages.

Do not commit client-identifiable information, credentials, local environment files, or unpublished regulatory source material unless the community has explicit rights to share it.
