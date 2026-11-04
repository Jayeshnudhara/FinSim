
def compare_financial_decisions(
    monthly_income,
    monthly_expenses,
    expense_reduction=0,
    additional_income=0,
    duration_months=6
):
    """
    Compare two financial decisions over a selected period.
    """

    # Current financial position
    baseline_savings = monthly_income - monthly_expenses

    # Decision A: Reduce monthly expenses
    decision_a_savings = (
        monthly_income
        - (monthly_expenses - expense_reduction)
    )

    # Decision B: Increase monthly income
    decision_b_savings = (
        (monthly_income + additional_income)
        - monthly_expenses
    )

    # Project savings over the selected duration
    baseline_projection = baseline_savings * duration_months
    decision_a_projection = decision_a_savings * duration_months
    decision_b_projection = decision_b_savings * duration_months

    # Compare the decisions
    if decision_a_projection > decision_b_projection:
        better_decision = "Decision A: Reduce Expenses"
    elif decision_b_projection > decision_a_projection:
        better_decision = "Decision B: Increase Income"
    else:
        better_decision = "Both decisions have the same impact"

    return {
        "baseline_monthly_savings": round(baseline_savings, 2),
        "decision_a_monthly_savings": round(decision_a_savings, 2),
        "decision_b_monthly_savings": round(decision_b_savings, 2),
        "baseline_projection": round(baseline_projection, 2),
        "decision_a_projection": round(decision_a_projection, 2),
        "decision_b_projection": round(decision_b_projection, 2),
        "decision_a_improvement": round(
            decision_a_projection - baseline_projection, 2
        ),
        "decision_b_improvement": round(
            decision_b_projection - baseline_projection, 2
        ),
        "better_decision": better_decision
    }
