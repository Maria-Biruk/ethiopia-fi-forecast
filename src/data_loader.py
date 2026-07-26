"""Load and validate the Ethiopia Financial Inclusion datasets."""

from pathlib import Path

import pandas as pd

from src.constants import (
    UNIFIED_DATA_FILE,
    REFERENCE_CODES_FILE,
    ENRICHED_DATA_FILE,
)

REQUIRED_COLUMNS = {
    "record_id",
    "record_type",
    "category",
    "pillar",
    "indicator",
    "indicator_code",
    "indicator_direction",
    "value_numeric",
    "value_text",
    "value_type",
    "unit",
    "observation_date",
    "period_start",
    "period_end",
    "fiscal_year",
    "gender",
    "location",
    "region",
    "source_name",
    "source_type",
    "source_url",
    "confidence",
    "related_indicator",
    "relationship_type",
    "impact_direction",
    "impact_magnitude",
    "impact_estimate",
    "lag_months",
    "evidence_basis",
    "comparable_country",
    "collected_by",
    "collection_date",
    "original_text",
    "notes",
}


def load_unified_data(path: Path = UNIFIED_DATA_FILE) -> pd.DataFrame:
    """Load and validate the unified financial inclusion dataset."""

    data = pd.read_excel(path, sheet_name="ethiopia_fi_unified_data")
    impacts = pd.read_excel(path, sheet_name="Impact_sheet")

    combined = pd.concat([data, impacts], ignore_index=True)

    missing = REQUIRED_COLUMNS - set(combined.columns)
    if missing:
        raise ValueError(f"Missing expected columns: {missing}")

    return combined


def load_reference_codes(path: Path = REFERENCE_CODES_FILE) -> pd.DataFrame:
    """Load reference codes."""

    return pd.read_excel(path)


def load_enriched_data(path: Path = ENRICHED_DATA_FILE) -> pd.DataFrame:
    """Load enriched dataset."""

    return pd.read_excel(path)


if __name__ == "__main__":
    combined = load_unified_data()
    refs = load_reference_codes()

    print(f"Loaded {len(combined)} unified records.")
    print(f"Loaded {len(refs)} reference code rows.")