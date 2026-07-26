"""Utility functions for the Ethiopia Financial Inclusion project."""

from pathlib import Path
import pandas as pd


def ensure_directory(path: Path) -> None:
    """Create a directory if it does not already exist."""
    path.mkdir(parents=True, exist_ok=True)


def save_dataframe(df: pd.DataFrame, path: Path) -> None:
    """Save a DataFrame to CSV."""
    ensure_directory(path.parent)
    df.to_csv(path, index=False)


def dataframe_summary(df: pd.DataFrame) -> dict:
    """Return basic summary statistics for a DataFrame."""
    return {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": int(df.isna().sum().sum()),
    }