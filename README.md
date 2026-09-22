# Agentic AI Governance Framework

Zest Ventures Inc.

> Enterprise reference methodology for AI Skills, MCP security, and governance controls.

## What We Assess

- AI Skills: purpose, prohibited actions, data boundaries, tools, evaluations, ownership, and lifecycle
- MCP-connected tools and APIs: identity, authorization, token handling, and least-privilege access
- Agent workflows: data flow, cross-agent calls, and combined permissions
- Delivery controls: testing, release gates, logging, incident response, and accountable ownership

## Assessment Method

### 1. Establish the evidence baseline

Review the Skill inventory, repositories, MCP configurations, API specifications, identity and authorization design, CI/CD controls, evaluations, logging, incident procedures, and ownership records.

### 2. Review each Skill

| Area | Question |
|---|---|
| Purpose | What is the Skill meant to do, and what must it never do? |
| Permissions | Which actions, tools, and downstream calls are allowed? |
| Access | What data, identity, and authorization scopes are required? |
| Proof | What tests, logs, approvals, and release evidence prove safe operation? |
| Ownership | Who owns changes, incidents, risk treatment, and retirement? |

### 3. Trace the full workflow

```text
Identity -> authorization -> data boundary -> Skill or agent -> tool or API -> resulting action -> evidence
```

The assessment reviews the combined workflow, not only individual components.

### 4. Turn gaps into delivery work

Each validated gap becomes a prioritized backlog item with evidence, risk, control objective, accountable owner, dependencies, and testable acceptance criteria.

## Five Architecture Questions

1. Who or what initiates the request?
2. What exact actions is that identity authorized to perform?
3. What data crosses each boundary?
4. Can one Skill, agent, or tool invoke a higher-impact capability?
5. What logs, tests, approvals, and release records prove the workflow remains within its approved boundary?

## Representative Risk Patterns

| Pattern | Assessment focus |
|---|---|
| Over-broad access | Minimum scopes, short-lived access, step-up authorization, and tool-level enforcement |
| Token misuse | Audience validation, scoped downstream credentials, and service-side authorization checks |
| Cross-agent privilege composition | Call-graph inventory, data-flow mapping, workflow approval, and human checkpoints |
| Weak evaluation | Normal, edge, prohibited-action, and adversarial testing with risk-tiered release gates |
| Orphaned capabilities | Named ownership, review cadence, lifecycle management, and retirement controls |

## Reference Artifact

The repository includes a read-only Payment Dispute Triage Skill contract. It demonstrates explicit scope, prohibited actions, data and authorization boundaries, structured outputs, testing expectations, logging, versioning, and lifecycle controls.

## About Zest Ventures

Zest Ventures provides enterprise architecture, AI governance, information security, and transformation delivery support for enterprise and regulated-industry clients.

**Service:** Agentic AI Governance and MCP Security Assessment

> Reference methodology. No client data or production configurations.
