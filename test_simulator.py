
import pandas as pd
from modules.financial_simulator import simulate_scenario

# Load cleaned financial data
df = pd.read_csv("data/processed/cleaned_transactions.csv")

# Test 1: No financial changes
result1 = simulate_scenario(df)

print("\nTEST 1: CURRENT FINANCIAL SITUATION")
print(result1)

# Test 2: Income increases by 10%
result2 = simulate_scenario(
    df,
    income_change_pct=10
)

print("\nTEST 2: INCOME INCREASES BY 10%")
print(result2)

# Test 3: Expenses decrease by 15%
result3 = simulate_scenario(
    df,
    expense_change_pct=-15
)

print("\nTEST 3: EXPENSES DECREASE BY 15%")
print(result3)

# Test 4: Additional monthly expense of ₹5,000
result4 = simulate_scenario(
    df,
    additional_expense=5000
)

print("\nTEST 4: ADDITIONAL EXPENSE OF ₹5,000")
print(result4)
