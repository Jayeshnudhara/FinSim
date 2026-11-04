
import pandas as pd
from pathlib import Path


def clean_transactions(df):
    """
    Clean and standardise financial transaction data.
    Returns a DataFrame with six standard columns.
    """

    df = df.copy()

    # 1. Standardise column names
    df.columns = df.columns.str.strip().str.lower()

    # 2. Correct the known date formatting typo
    df["date"] = df["date"].astype(str).str.replace(
        "26-0 2-2022",
        "26-02-2022",
        regex=False
    )

    # 3. Convert dates into proper datetime values
    df["date"] = pd.to_datetime(
        df["date"],
        format="%d-%m-%Y",
        errors="coerce"
    )

    # 4. Convert amounts into numeric values
    df["amount"] = pd.to_numeric(
        df["amount"],
        errors="coerce"
    )

    # 5. Clean descriptions
    df["description"] = (
        df["description"]
        .fillna("Unknown")
        .astype(str)
        .str.strip()
        .replace("", "Unknown")
    )

    # 6. Standardise transaction types
    df["type"] = df["type"].astype(str).str.strip().str.title()

    # 7. Clean categories
    df["category"] = (
        df["category"]
        .fillna("Unknown")
        .astype(str)
        .str.strip()
        .replace("", "Unknown")
    )

    # 8. Add merchant column (not available in original dataset)
    if "merchant" not in df.columns:
        df["merchant"] = "Unknown"
    else:
        df["merchant"] = df["merchant"].fillna("Unknown")

    # 9. Remove rows with invalid essential values
    df = df.dropna(subset=["date", "amount"])
    df = df[df["type"].isin(["Income", "Expense"])]
    df = df[df["amount"] > 0]

    # 10. Remove exact duplicate transactions
    df = df.drop_duplicates()

    # 11. Keep only the required columns in the correct order
    df = df[
        ["date", "description", "amount", "type", "category", "merchant"]
    ]

    # 12. Reset row numbering
    df = df.reset_index(drop=True)

    return df


# Run this file directly to clean and save the dataset
if __name__ == "__main__":

    project_folder = Path(__file__).resolve().parent.parent

    input_path = project_folder / "data" / "raw" / "cleaned_expense_data.csv"
    output_folder = project_folder / "data" / "processed"
    output_path = output_folder / "cleaned_transactions.csv"

    raw_data = pd.read_csv(input_path)

    print("Original dataset:", len(raw_data), "transactions")

    cleaned_data = clean_transactions(raw_data)

    output_folder.mkdir(parents=True, exist_ok=True)
    cleaned_data.to_csv(output_path, index=False)

    print("Cleaned dataset:", len(cleaned_data), "transactions")
    print("Saved to:", output_path)
    print("\nFinal columns:")
    print(cleaned_data.columns.tolist())
    print("\nTransaction types:")
    print(cleaned_data["type"].value_counts())
