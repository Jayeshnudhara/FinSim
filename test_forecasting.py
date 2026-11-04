
import pandas as pd
from modules.forecasting import forecast_finances

# Load cleaned dataset
df = pd.read_csv("data/processed/cleaned_transactions.csv")

# Generate 30-day forecast
forecast = forecast_finances(df, forecast_days=30)

print("\n30-DAY FINANCIAL FORECAST")
print(forecast.to_string(index=False))

print("\nTotal predicted income:",
      round(forecast["predicted_income"].sum(), 2))

print("Total predicted expenses:",
      round(forecast["predicted_expenses"].sum(), 2))

print("Total predicted savings:",
      round(forecast["predicted_savings"].sum(), 2))
