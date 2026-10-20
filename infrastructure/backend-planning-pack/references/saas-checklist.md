# SaaS Backend Planning Checklist

Load this when the request is for a SaaS backend, multi-tenant product, B2B platform, or subscription-backed service.

## Focus areas

- Tenancy model
  - Single-tenant, pooled multi-tenant, or hybrid
  - Data isolation boundary
  - Tenant-aware access control
  - Tenant-level configuration and feature flags

- Identity and access
  - User, workspace, organisation, and admin roles
  - SSO, SCIM, MFA, and invitation flows when relevant
  - Session strategy and token revocation needs

- API and contract design
  - Public versus internal APIs
  - Versioning and deprecation policy
  - Rate limits, quotas, and abuse controls
  - Idempotency requirements for write operations

- Billing-adjacent concerns
  - Entitlements and plan enforcement
  - Usage metering boundaries
  - Subscription state changes and grace periods
  - Audit trail for plan-impacting operations

- Data and lifecycle
  - Tenant deletion and retention policy
  - Backup and restore expectations
  - Data export and portability needs
  - Region or residency constraints

- Reliability and operations
  - Noisy-neighbor controls
  - Per-tenant observability or support tooling
  - Incident handling for tenant-scoped versus global outages
  - Rollout segmentation by tenant or cohort

## Useful prompts to answer in the planning pack

- What is the tenancy boundary for auth, data, caching, and jobs?
- Which operations require strong consistency versus eventual consistency?
- Which limits are global, per tenant, per user, or per API key?
- How will support or operations staff safely impersonate or inspect tenant state?
- What are the migration and backfill implications when the tenancy model changes?
