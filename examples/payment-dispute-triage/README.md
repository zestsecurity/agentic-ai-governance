# Payment dispute triage governance demo

This local example uses fictional, masked transaction information. The policy allows one read-only case summary and denies other actions by default, including a refund, before the mock tool executes.

## Run

Install the toolkit in a Python 3.11+ virtual environment:

```cmd
python -m pip install "agent-governance-toolkit[full]"
python demo.py
```

Run both commands from this folder. The first installs the Microsoft Agent Governance Toolkit. The second runs the mock example.

## Expected result

- The read action prints `MOCK TOOL EXECUTED: read_case ...` and returns a masked sample case.
- The refund action prints a governance denial.
- There must be no `MOCK TOOL EXECUTED: issue_refund ...` line. If it appears, the example exits with a failure message.

## What this demonstrates

The policy wraps a tool function and blocks selected actions before the mock tool runs. This is a small example of translating a Skill's read-only boundary into an enforced action rule.

It does not scan or validate a `SKILL.md`, integrate with a real MCP server, connect to a bank, or establish that a production system is secure or compliant. A real assessment would also inspect identity and token scope, server-side authorization, data flows, approval records, logging, release gates, and the full agent call path.

All case data is synthetic. Do not add customer records, account numbers, credentials, or production configuration to this example.
