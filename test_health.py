from modules.financial_health import calculate_financial_health

result = calculate_financial_health(
    monthly_income=30000,
    monthly_expenses=22000,
    emergency_reserve=60000
)

print("\nFINSIM FINANCIAL HEALTH REPORT")
print("--------------------------------")

for key, value in result.items():
    print(f"{key}: {value}")