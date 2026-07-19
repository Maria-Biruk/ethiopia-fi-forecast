"""Load and validate the Ethiopia FI unified dataset + reference codes."""
from pathlib import Path
import pandas as pd

RAW_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"

REQUIRED_COLUMNS = {
    "record_id", "record_type", "pillar", "indicator", "indicator_code",
    "value_numeric", "unit", "record_date", "category", "source_type",
    "source_name", "source_url", "original_text", "confidence",
    "collected_by", "collection_date", "notes", "parent_id",
    "related_indicator", "impact_direction", "impact_magnitude",
    "lag_months", "evidence_basis",
}


def load_unified_data(path: Path = RAW_DIR / "ethiopia_fi_unified_data.csv") -> pd.DataFrame:
    df = pd.read_csv(path)
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing expected columns: {missing}")
    return df


def load_reference_codes(path: Path = RAW_DIR / "reference_codes.csv") -> pd.DataFrame:
    return pd.read_csv(path)


def profile(df: pd.DataFrame) -> None:
    print("Records by record_type:")
    print(df["record_type"].value_counts(dropna=False), "\n")

    print("Records by pillar:")
    print(df["pillar"].value_counts(dropna=False), "\n")

    print("Records by source_type:")
    print(df["source_type"].value_counts(dropna=False), "\n")

    print("Records by confidence:")
    print(df["confidence"].value_counts(dropna=False), "\n")

    dates = pd.to_datetime(df["record_date"], errors="coerce").dropna()
    if not dates.empty:
        print(f"Temporal range: {dates.min().date()} to {dates.max().date()}\n")

    print("Indicator coverage (indicator_code x count):")
    print(df["indicator_code"].value_counts(dropna=False), "\n")