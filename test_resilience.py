from modules.financial_resilience import analyze_financial_resilience

result = analyze_financial_resilience(
    monthly_income=30000,
    monthly_expenses=22000,
    emergency_reserve=10000,
    income_reduction_pct=50,
    emergency_expense=20000,
    disruption_months=3
)

print("\nFINANCIAL RESILIENCE STRESS TEST")
print("--------------------------------")

for key, value in result.items():
    print(f"{key}: {value}")