# Official Documentation Sources

Use these source types first when the user asks for standards, best practices, or authoritative guidance.

## Standards and specifications
- IETF and RFC documents for protocol and web standards
- OpenAPI Initiative for REST API description guidance
- JSON Schema official documentation
- W3C specifications when relevant
- CNCF and Kubernetes official documentation for cloud-native patterns

## Cloud architecture and operations
- AWS Well-Architected Framework and AWS service documentation
- Microsoft Azure Well-Architected Framework and Azure service documentation
- Google Cloud architecture framework and Google Cloud product documentation

## Security and threat modelling
- OWASP cheat sheets and project documentation
- NIST publications when security controls or risk language matter
- Official identity provider documentation for authn/authz flows

## Reliability and SRE
- Google SRE book and official sre.google guidance
- Official observability vendor documentation when the user names a platform

## Data and platform services
- PostgreSQL official documentation
- MySQL official documentation
- MongoDB official documentation
- Redis official documentation
- Kafka and Confluent official documentation when directly relevant
- RabbitMQ official documentation

## API and integration platforms
- Stripe docs, Twilio docs, SendGrid docs, and other official vendor docs when named by the user
- Official webhook and SDK documentation from the integration provider

## Source preference order
1. Standards or protocol owner
2. Official product or vendor documentation
3. Official framework or maintainer documentation
4. Reputable engineering guidance only when no official source exists

## Usage rules
- Prefer the current version of the official docs.
- Verify feature availability, limits, and terminology in the docs before writing.
- Do not cite unofficial tutorials when the claim can be supported by an official source.
- If multiple clouds or vendors are possible, stay vendor-neutral unless the user specifies one.
