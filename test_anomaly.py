import pandas as pd

from modules.anomaly_detector import (
    detect_anomalies,
    explain_anomalies
)

# Create sample transaction data
data = {
    "date": [
        f"2026-11-{day:02d}" for day in range(1, 31)
    ],

    "description": [
        "Lunch", "Bus", "Groceries", "Coffee",
        "Shopping", "Lunch", "Bus", "Groceries",
        "Coffee", "Shopping", "Lunch", "Bus",
        "Groceries", "Coffee", "Shopping", "Lunch",
        "Bus", "Groceries", "Coffee", "Shopping",
        "Lunch", "Bus", "Groceries", "Coffee",
        "Shopping", "Lunch", "Bus", "Groceries",
        "Coffee", "Expensive purchase"
    ],

    "amount": [
        120, 50, 600, 80, 900,
        130, 50, 550, 90, 850,
        110, 60, 620, 75, 950,
        125, 50, 580, 85, 880,
        115, 55, 610, 70, 920,
        140, 45, 590, 95, 15000
    ],

    "type": ["Expense"] * 30,

    "category": [
        "Food", "Transport", "Groceries", "Food", "Shopping",
        "Food", "Transport", "Groceries", "Food", "Shopping",
        "Food", "Transport", "Groceries", "Food", "Shopping",
        "Food", "Transport", "Groceries", "Food", "Shopping",
        "Food", "Transport", "Groceries", "Food", "Shopping",
        "Food", "Transport", "Groceries", "Food", "Shopping"
    ],

    "merchant": ["Sample"] * 30
}

df = pd.DataFrame(data)

# Run the anomaly detection model
result = detect_anomalies(df)

# Generate explanations
result = explain_anomalies(result)

# Display results
print("\nFIN SIGHT - ANOMALY DETECTION RESULTS\n")

print(
    result[
        ["description", "amount", "category",
         "anomaly", "anomaly_score", "explanation"]
    ].to_string(index=False)
)

print("\nUnusual transactions found:")

print(result[result["anomaly"] == True][
    ["description", "amount", "category", "explanation"]
].to_string(index=False))
print("\nOUTPUT COLUMNS:")
print(result.columns.tolist())