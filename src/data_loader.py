"""Load and validate the Ethiopia FI unified dataset + reference codes."""
from pathlib import Path
import pandas as pd

RAW_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"
PROCESSED_DIR = Path(__file__).resolve().parents[1] / "data" / "processed"

REQUIRED_COLUMNS = {
    "record_id", "record_type", "category", "pillar", "indicator",
    "indicator_code", "indicator_direction", "value_numeric", "value_text",
    "value_type", "unit", "observation_date", "period_start", "period_end",
    "fiscal_year", "gender", "location", "region", "source_name",
    "source_type", "source_url", "confidence", "related_indicator",
    "relationship_type", "impact_direction", "impact_magnitude",
    "impact_estimate", "lag_months", "evidence_basis", "comparable_country",
    "collected_by", "collection_date", "original_text", "notes",
}


def load_unified_data(path: Path = RAW_DIR / "ethiopia_fi_unified_data.xlsx") -> pd.DataFrame:
    data = pd.read_excel(path, sheet_name="ethiopia_fi_unified_data")
    impacts = pd.read_excel(path, sheet_name="Impact_sheet")
    combined = pd.concat([data, impacts], ignore_index=True)
    missing = REQUIRED_COLUMNS - set(combined.columns)
    if missing:
        raise ValueError(f"Missing expected columns: {missing}")
    return combined


def load_reference_codes(path: Path = RAW_DIR / "reference_codes.xlsx") -> pd.DataFrame:
    return pd.read_excel(path)


def load_enriched_data(path: Path = PROCESSED_DIR / "ethiopia_fi_unified_data_enriched.xlsx") -> pd.DataFrame:
    return pd.read_excel(path)


if __name__ == "__main__":
    combined = load_unified_data()
    refs = load_reference_codes()
    print(f"Loaded {len(combined)} unified records and {len(refs)} reference code rows.")