
def calculate_financial_health(
    monthly_income,
    monthly_expenses,
    emergency_reserve
):
    """
    Calculate a transparent financial health score out of 100.
    """

    # 1. Calculate monthly savings
    monthly_savings = monthly_income - monthly_expenses

    # 2. Calculate savings rate
    if monthly_income > 0:
        savings_rate = (monthly_savings / monthly_income) * 100
    else:
        savings_rate = 0

    # 3. Savings performance: maximum 40 points
    savings_score = max(
        0,
        min(40, (savings_rate / 20) * 40)
    )

    # 4. Monthly cash flow: maximum 30 points
    cash_flow_score = 30 if monthly_savings > 0 else 0

    # 5. Emergency reserve coverage: maximum 30 points
    if monthly_expenses > 0:
        reserve_months = emergency_reserve / monthly_expenses
    else:
        reserve_months = 0

    reserve_score = min(30, (reserve_months / 6) * 30)

    # 6. Total financial health score
    total_score = round(
        savings_score + cash_flow_score + reserve_score
    )

    # 7. Assign a financial health category
    if total_score >= 80:
        health_status = "Healthy"
    elif total_score >= 60:
        health_status = "Moderate"
    elif total_score >= 40:
        health_status = "Needs Improvement"
    else:
        health_status = "At Risk"

    return {
        "monthly_savings": round(monthly_savings, 2),
        "savings_rate": round(savings_rate, 2),
        "reserve_months": round(reserve_months, 2),
        "savings_score": round(savings_score, 2),
        "cash_flow_score": cash_flow_score,
        "reserve_score": round(reserve_score, 2),
        "total_score": total_score,
        "health_status": health_status
    }
