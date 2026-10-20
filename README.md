# Accountant AI Playbook

Practical skills, workflows, and best practices for accountants and corporate service providers building AI-enabled practices.

This repository is intended for a closed practitioner community. It focuses on reusable Codex skills, review checklists, templates, and operating patterns that help professionals deliver accounting, compliance, corporate secretarial, and client advisory work with stronger AI support.

## Official Skill Repositories

- [OpenAI Skills](https://github.com/openai/skills)
- [Anthropic Skills](https://github.com/anthropics/skills)

## External Skills Disclaimer

Skills from external repositories should be treated like third-party code. Review the instructions, scripts, dependencies, and requested permissions before installing or running them. Do not use external skills with client data, credentials, or confidential practice information unless the source is trusted, the skill has been reviewed, and the data handling risk is acceptable for your firm.

## Catalog

Categories organise the catalog; existing folder paths remain unchanged.

### Accounting

- [Bank-to-books bookkeeping](bookkeeping-agent-bank2books/)
- [DBS-to-Xero bank import conversion](dbs-xero-csv/)

### Compliance & Corporate Services

- [Singapore AML/CTF screening](sg-aml-ctf-screening-tool/)
- [Singapore corporate secretarial workflows](sg-corpsec-private/)
- [Singapore KYC, CDD and EDD](sg-kyc-cdd-edd/)

### Infrastructure & Integrations

- [Agent Infrastructure Operator](agent-infrastructure-operator/) — inspect, diagnose and verify local or hosted agent infrastructure, with narrow permissions, user-facing evidence and rollback. Includes platform-check references and an operator-report template. Structural validation passed; live infrastructure behaviour has not been tested as part of this publication.

### Practice Productivity

- [Document-to-Markdown conversion](document-to-md/)
- [Skill orchestration planning](skill-orchestration-planner/)

### Learning & Research

- [AI visibility audits](ai-visibility-audit/)
- [Web research-to-action prompt steps](web-research-to-action-department-prompt-steps/)
- [Assessment submission coaching plugin](plugins/assessment-submission-coach-plugin/)

## Plugin Packages

- `plugins/assessment-submission-coach-plugin`: Agentic AI Foundations assessment submission coaching plugin with Appendix A templates.

Install local plugins from their plugin folder, not from the repository root. For this package, select `plugins/assessment-submission-coach-plugin` so Codex can find `.codex-plugin/plugin.json`.

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

Do not commit client-identifiable information, credentials, local environment files, or unpublished regulatory source material unless the community has explicit rights to share it.
