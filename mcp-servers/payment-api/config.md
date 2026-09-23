# MCP Server — Payment API Governance

**Server name:** payment-api-mcp
**Owner:** Payments Engineering Lead
**Risk tier:** HIGH
**ARB approval:** ARB-2024-041

## Tool Authorization

| Tool | Scope | Write | Human Checkpoint Required |
|---|---|---|---|
| get-dispute | READ | No | No |
| get-order | READ | No | No |
| get-transaction | READ | No | No |
| create-case | WRITE | Yes | Yes — named analyst approval |
| refund-api | NOT AUTHORIZED | — | — |

## Token Governance
- Tokens are audience-restricted to this MCP server only
- Audience claim: `payment-api-mcp-prod`
- Token lifetime: 15 minutes maximum
- Scope: minimum required per tool call — not inherited from requesting identity
- Broad developer tokens are explicitly rejected at the server level

## What this server will not accept
- Tokens without a valid audience claim for this server
- Requests from identities not in the approved workload registry
- Write operations without a logged human approval record
- Any call to refund-api — not authorized under any condition

## Audit
- Every tool call logged: identity, timestamp, tool name, input parameters (sanitized), outcome
- Logs are append-only and immutable
- Retention: 7 years (PCI-DSS requirement)
- Log destination: payments-audit-log.internal

## Evergreen
- Server version pinned to semantic version in deployment manifest
- MCP spec version: tracked in ADR-2024-007
- Updates require regression test pass and ARB notification
