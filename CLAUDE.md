# CLAUDE.md — Model Governance

This file governs how Claude operates in this repository.

## What Claude can do
- Review and assess SKILL.md files against the 8-dimension rubric
- Analyze MCP server configurations for security gaps
- Generate evaluation case suggestions for existing Skills
- Summarize assessment findings in structured format

## What Claude must never do
- Access, infer, or reproduce real client data or production configurations
- Approve, deny, or recommend financial decisions
- Invoke tools outside this repository's declared MCP server list
- Bypass the human checkpoint requirement on any write action

## Data boundary
- This repository contains demonstration artifacts only
- No PAN, CVV, account numbers, or customer PII enters this context
- All examples use synthetic case data

## Model version
- Alias: claude-sonnet-latest
- Never pin to a hardcoded version string
- Alias advancement requires regression suite pass and named owner approval

## Audit
- Every Claude invocation in this repo is logged with identity, timestamp, and output summary
- Logs are retained for audit review
