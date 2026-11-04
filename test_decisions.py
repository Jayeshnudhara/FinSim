from modules.decision_engine import compare_financial_decisions

result = compare_financial_decisions(
    monthly_income=30000,
    monthly_expenses=22000,
    expense_reduction=5000,
    additional_income=10000,
    duration_months=6
)

print("\nFINANCIAL DECISION COMPARISON")
print("--------------------------------")

for key, value in result.items():
    print(f"{key}: {value}")