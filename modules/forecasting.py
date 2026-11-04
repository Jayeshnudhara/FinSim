
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


def forecast_finances(df, forecast_days=30):

    df = df.copy()

    # 1. Prepare transaction data
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    df = df.dropna(subset=["date", "amount"])
    df = df[df["amount"] > 0]

    # 2. Separate income and expenses
    income = df[df["type"] == "Income"].copy()
    expenses = df[df["type"] == "Expense"].copy()

    # 3. Calculate daily income and expenses
    daily_income = income.groupby("date")["amount"].sum()
    daily_expenses = expenses.groupby("date")["amount"].sum()

    # 4. Create a complete daily date range
    all_dates = pd.date_range(
        start=df["date"].min(),
        end=df["date"].max(),
        freq="D"
    )

    daily_data = pd.DataFrame(index=all_dates)

    daily_data["income"] = daily_income.reindex(
        all_dates, fill_value=0
    )

    daily_data["expenses"] = daily_expenses.reindex(
        all_dates, fill_value=0
    )

    daily_data["savings"] = (
        daily_data["income"] - daily_data["expenses"]
    )

    # 5. Prepare data for Linear Regression
    X = np.arange(len(daily_data)).reshape(-1, 1)

    # Generate future dates
    future_dates = pd.date_range(
        start=all_dates[-1] + pd.Timedelta(days=1),
        periods=forecast_days,
        freq="D"
    )

    future_X = np.arange(
        len(daily_data),
        len(daily_data) + forecast_days
    ).reshape(-1, 1)

    # 6. Train income forecasting model
    income_model = LinearRegression()
    income_model.fit(X, daily_data["income"])

    predicted_income = income_model.predict(future_X)

    # 7. Train expense forecasting model
    expense_model = LinearRegression()
    expense_model.fit(X, daily_data["expenses"])

    predicted_expenses = expense_model.predict(future_X)

    # 8. Prevent negative financial predictions
    predicted_income = np.maximum(predicted_income, 0)
    predicted_expenses = np.maximum(predicted_expenses, 0)

    # 9. Calculate predicted savings
    predicted_savings = (
        predicted_income - predicted_expenses
    )

    # 10. Return forecast results
    forecast_df = pd.DataFrame({
        "date": future_dates,
        "predicted_income": predicted_income,
        "predicted_expenses": predicted_expenses,
        "predicted_savings": predicted_savings
    })

    return forecast_df
