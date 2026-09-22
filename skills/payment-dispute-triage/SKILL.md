# Payment Dispute Triage Skill Contract

**Version:** 1.0 (Draft)  
**Owner:** AI Assessment & Strategy  
**Last Reviewed:** 2026-09-20

## Purpose

Payment Dispute Triage is a read-only demonstration workload. It summarizes a dispute case, categorizes the case, flags missing information, and recommends whether a human analyst should review it.

The Skill does not approve, deny, refund, modify records, or contact customers.

## Supported Use Cases

- Classify a new dispute by type
- Identify missing or incomplete case information
- Recommend escalation to a human analyst
- Produce a structured case summary

## Prohibited Actions

- Approve or deny a dispute
- Issue a refund or credit
- Modify a dispute record or customer account
- Initiate external communication
- Make a final financial decision
- Access live financial systems or real customer data

## Input and Output

**Input:** A structured dispute case object.

**Output:**

- Case summary
- Triage category
- Confidence and limitations
- Missing-information flags
- Human escalation recommendation
- Evidence references

If the input is malformed or incomplete, the Skill returns structured missing-field information and recommends human review.

## Data and Authorization Boundaries

- Read-only access to demonstration case data
- No writes and no persistence
- Short-lived, case-scoped authorization
- Non-human workload identity with no inherited administrator privileges
- Invocation and output traceable to the authorized requester

## Evaluation and Release Controls

Evaluation covers:

1. Standard classification cases
2. Missing-data and conflicting-data cases
3. Prohibited-action tests
4. Evidence-supported escalation recommendations
5. Confidence and limitation formatting

Changes require evaluation evidence, security review appropriate to risk, and recorded approval before release.

## Observability

The audit record captures invocation time, request and correlation IDs, Skill and tool version, requester identity, case identifier, tool outcome, output category, escalation result, and evidence references.

The audit record does not include hidden model reasoning, credentials, or unnecessary sensitive data.

## Lifecycle

The Skill has a named owner, documented version, defined change control, and a retirement path.

> Demonstration artifact. No client data or production configurations.
