
def analyze_financial_resilience(
    monthly_income,
    monthly_expenses,
    emergency_reserve,
    income_reduction_pct=0,
    emergency_expense=0,
    disruption_months=1
):
    """
    Simulates financial shocks and evaluates
    the user's financial resilience.
    """

    # Apply income reduction
    reduced_income = monthly_income * (
        1 - income_reduction_pct / 100
    )

    # Calculate monthly savings after the shock
    monthly_balance = reduced_income - monthly_expenses

    # Calculate total reserve after emergency expense
        # Calculate total financial impact
    total_balance = monthly_balance * disruption_months

    # Calculate remaining reserve
    remaining_reserve = max(
        0,
        emergency_reserve - emergency_expense
    )

    # Calculate projected reserve, including any funding deficit
    projected_reserve = (
        emergency_reserve
        - emergency_expense
        + total_balance
    )

    # Calculate financial runway
    if monthly_expenses > 0:
        financial_runway = remaining_reserve / monthly_expenses
    else:
        financial_runway = 0

    # Calculate the reserve required to survive the scenario
    required_reserve = max(
        0,
        emergency_expense - total_balance
    )

    # Calculate the funding shortfall
    reserve_shortfall = max(
        0,
        -projected_reserve
    )

    # Assess resilience
    if projected_reserve >= emergency_reserve and monthly_balance >= 0:
        resilience_status = "Strong"
    elif projected_reserve >= 0:
        resilience_status = "Moderate"
    else:
        resilience_status = "At Risk"

    return {
        "reduced_income": round(reduced_income, 2),
        "monthly_balance": round(monthly_balance, 2),
        "remaining_reserve": round(remaining_reserve, 2),
        "projected_reserve": round(projected_reserve, 2),
        "financial_runway": round(financial_runway, 2),
        "required_reserve": round(required_reserve, 2),
        "reserve_shortfall": round(reserve_shortfall, 2),
        "resilience_status": resilience_status
    }
