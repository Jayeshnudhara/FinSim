import pandas as pd
import numpy as np

from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
def prepare_features(df):

    # Keep only expense transactions
    expenses = df[df["type"] == "Expense"].copy()

    # Convert date into datetime format
    expenses["date"] = pd.to_datetime(
        expenses["date"], errors="coerce"
    )

    # Convert amount into numeric format
    expenses["amount"] = pd.to_numeric(
        expenses["amount"], errors="coerce"
    )

    # Remove invalid transactions
    expenses = expenses.dropna(
        subset=["date", "amount"]
    )

    expenses = expenses[expenses["amount"] > 0]

    # Extract day and month
    expenses["day"] = expenses["date"].dt.day
    expenses["month"] = expenses["date"].dt.month

    expenses["category_avg"] = (
    expenses.groupby("category")["amount"]
    .transform("median")
)

    expenses["category_ratio"] = (
    expenses["amount"] /
    expenses["category_avg"].replace(0, np.nan)
)

    expenses["category_ratio"] = (
    expenses["category_ratio"].fillna(1)
)

    features = expenses[
    ["amount", "category_ratio"]
].copy()

    return expenses, features
def detect_anomalies(df, contamination=0.05):

    # Prepare the transaction data
    expenses, features = prepare_features(df)

    # Check whether there is enough data
    if len(features) < 20:
        expenses["anomaly"] = False
        expenses["anomaly_score"] = 0.0

        return expenses

    # Scale the numerical features
    scaler = StandardScaler()

    scaled_features = scaler.fit_transform(features)

    # Create the Isolation Forest model
    model = IsolationForest(
        n_estimators=100,
        contamination=contamination,
        random_state=42
    )

    # Train the model and predict anomalies
    predictions = model.fit_predict(scaled_features)

    # Convert predictions into True and False
    expenses["anomaly"] = predictions == -1

    # Calculate anomaly scores
    expenses["anomaly_score"] = model.decision_function(
        scaled_features
    )

    return expenses
def explain_anomalies(df):

    df = df.copy()

    df["alert_level"] = "Normal"
    df["explanation"] = ""

    for index, row in df.iterrows():

        if row["anomaly"]:

            category = row["category"]
            amount = row["amount"]

            category_data = df[
                df["category"] == category
            ]

            typical_amount = category_data["amount"].median()

            if typical_amount > 0:

                ratio = amount / typical_amount

                if ratio >= 2:

                    df.at[index, "alert_level"] = "High"

                    df.at[index, "explanation"] = (
                        f"Spending is {ratio:.1f} times "
                        f"the typical {category} amount."
                    )

                else:

                    df.at[index, "alert_level"] = "Review"

                    df.at[index, "explanation"] = (
                        "The ML model detected an unusual "
                        "pattern. Review this transaction."
                    )


    return df