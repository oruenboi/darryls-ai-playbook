# Event-Driven Backend Planning Checklist

Load this when the request involves queues, streams, workers, schedulers, webhooks, ETL pipelines, or integration-heavy backends.

## Focus areas

- Event and job model
  - Command versus event boundaries
  - Event schema ownership
  - Delivery guarantees and ordering assumptions
  - Retryability and idempotency keys

- Failure handling
  - Retry policy and backoff
  - Poison-message strategy
  - Dead-letter queue ownership and replay process
  - Timeout and cancellation behavior

- Operational safety
  - Duplicate delivery handling
  - Partial failure and compensation flow
  - Backpressure controls
  - Concurrency limits and worker saturation behavior

- Integration design
  - Webhook signature verification
  - Provider retry semantics
  - Contract versioning and schema drift handling
  - Circuit breakers or dependency isolation

- Observability
  - Trace correlation across async hops
  - Queue depth, lag, and age metrics
  - Replay and reprocessing audit trail
  - Operator runbooks for stuck or failing jobs

- Data consistency
  - Outbox or inbox pattern use
  - Exactly-once expectations versus practical at-least-once handling
  - Deduplication window and storage
  - Recovery from missed events or delayed downstream consumers

## Useful prompts to answer in the planning pack

- What guarantees does each async path actually provide?
- Which components own retries, deduplication, and replay?
- How will operators detect silent stalls, lag growth, or schema breakage?
- Which workflows need compensation logic instead of simple retry?
