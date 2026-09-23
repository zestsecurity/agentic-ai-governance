"""Local governance demo using synthetic payment dispute data only."""

from agentmesh.governance import govern


SAMPLE_CASE = {
    "case_id": "DEMO-1042",
    "account": "**** 4821",
    "amount_usd": 84.50,
    "merchant": "Example Market",
    "customer_note": "I do not recognize this purchase.",
}


def dispute_tool(action: str, case_id: str) -> dict:
    """Mock tool. It has no connection to a bank or payment system."""
    if action == "read_case":
        print(f"MOCK TOOL EXECUTED: {action} {case_id}")
        return {"case": SAMPLE_CASE, "triage": "human_review_recommended"}

    # If a write action reaches this function, the policy gate failed.
    print(f"MOCK TOOL EXECUTED: {action} {case_id}")
    return {"action": action, "case_id": case_id}


safe_dispute_tool = govern(dispute_tool, policy="policy.yaml")


def main() -> None:
    result = safe_dispute_tool(action="read_case", case_id="DEMO-1042")
    print("Allowed read result:", result)

    try:
        safe_dispute_tool(action="issue_refund", case_id="DEMO-1042")
    except Exception as exc:
        print(f"Blocked as expected: {type(exc).__name__}: {exc}")
    else:
        raise SystemExit("FAIL: refund action was not blocked")


if __name__ == "__main__":
    main()
