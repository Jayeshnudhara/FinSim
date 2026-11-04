
import pandas as pd


def simulate_scenario(
    df,
    income_change_pct=0,
    expense_change_pct=0,
    additional_expense=0
):

    df = df.copy()

    # Prepare data
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df = df.dropna(subset=["amount"])
    df = df[df["amount"] > 0]

    # Calculate average monthly income and expenses
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"])

    months = df["date"].dt.to_period("M").nunique()

    if months == 0:
        raise ValueError("No valid transaction months found.")

    current_income = (
        df.loc[df["type"] == "Income", "amount"].sum() / months
    )

    current_expenses = (
        df.loc[df["type"] == "Expense", "amount"].sum() / months
    )

    current_savings = current_income - current_expenses

    # Apply user changes
    simulated_income = (
        current_income * (1 + income_change_pct / 100)
    )

    simulated_expenses = (
        current_expenses * (1 + expense_change_pct / 100)
        + additional_expense
    )

    simulated_savings = simulated_income - simulated_expenses

    # Calculate savings rate
    if simulated_income > 0:
        savings_rate = (
            simulated_savings / simulated_income
        ) * 100
    else:
        savings_rate = 0

    return {
        "current_income": round(current_income, 2),
        "current_expenses": round(current_expenses, 2),
        "current_savings": round(current_savings, 2),
        "simulated_income": round(simulated_income, 2),
        "simulated_expenses": round(simulated_expenses, 2),
        "simulated_savings": round(simulated_savings, 2),
        "savings_rate": round(savings_rate, 2)
    }
