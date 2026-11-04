
import pandas as pd
from pathlib import Path


def get_sample_data():

    # Locate the cleaned dataset
    project_folder = Path(__file__).resolve().parent

    file_path = (
        project_folder
        / "data"
        / "processed"
        / "cleaned_transactions.csv"
    )

    # Check whether the dataset exists
    if not file_path.exists():
        raise FileNotFoundError(
            f"Cleaned dataset not found at: {file_path}"
        )

    # Load the actual financial data
    df = pd.read_csv(file_path)

    # Convert date column into datetime format
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Ensure amount is numeric
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    return df
