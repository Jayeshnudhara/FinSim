
import pandas as pd


def get_sample_data():

    data = {
        "date": [
            "2026-10-01", "2026-10-02", "2026-10-03",
            "2026-10-04", "2026-10-05", "2026-10-06",
            "2026-10-07", "2026-10-08", "2026-10-09",
            "2026-10-10", "2026-10-11", "2026-10-12",
            "2026-10-13", "2026-10-14", "2026-10-15",
            "2026-10-16", "2026-10-17", "2026-10-18",
            "2026-10-19", "2026-10-20"
        ],

        "description": [
            "Monthly Salary", "Groceries", "Restaurant",
            "Bus Pass", "Freelance Income", "Shopping",
            "Electricity Bill", "Coffee", "Groceries",
            "Fuel", "Restaurant", "Online Shopping",
            "Monthly Salary", "Medical", "Groceries",
            "Entertainment", "Bus Pass", "Restaurant",
            "Shopping", "Freelance Income"
        ],

        "amount": [
            45000, 1200, 650, 500, 5000,
            2500, 1800, 180, 950, 1200,
            800, 3500, 45000, 2200, 1100,
            1500, 500, 700, 15000, 4000
        ],

        "type": [
            "Income", "Expense", "Expense",
            "Expense", "Income", "Expense",
            "Expense", "Expense", "Expense",
            "Expense", "Expense", "Expense",
            "Income", "Expense", "Expense",
            "Expense", "Expense", "Expense",
            "Expense", "Income"
        ],

        "category": [
            "Salary", "Groceries", "Food",
            "Transport", "Freelance", "Shopping",
            "Utilities", "Food", "Groceries",
            "Transport", "Food", "Shopping",
            "Salary", "Healthcare", "Groceries",
            "Entertainment", "Transport", "Food",
            "Shopping", "Freelance"
        ],

        "merchant": [
            "Company", "Supermarket", "Cafe",
            "BMTC", "Client", "Clothing Store",
            "Electricity Board", "Coffee Shop",
            "Supermarket", "Fuel Station",
            "Restaurant", "Online Store",
            "Company", "Pharmacy", "Supermarket",
            "Cinema", "BMTC", "Restaurant",
            "Online Store", "Client"
        ]
    }

    df = pd.DataFrame(data)

    extra_data = pd.DataFrame([
        ["2026-10-21", "Groceries", 1300, "Expense", "Groceries", "Supermarket"],
        ["2026-10-22", "Restaurant", 750, "Expense", "Food", "Restaurant"],
        ["2026-10-23", "Bus Fare", 450, "Expense", "Transport", "BMTC"],
        ["2026-10-24", "Shopping", 1800, "Expense", "Shopping", "Clothing Store"],
        ["2026-10-25", "Electricity", 1600, "Expense", "Utilities", "Electricity Board"],
        ["2026-10-26", "Medical", 900, "Expense", "Healthcare", "Pharmacy"]
    ], columns=[
        "date", "description", "amount", "type", "category", "merchant"
    ])

    df = pd.concat([df, extra_data], ignore_index=True)
    df["date"] = pd.to_datetime(df["date"])

    return df
