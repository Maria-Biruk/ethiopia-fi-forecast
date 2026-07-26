from pathlib import Path

# Base project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Data directories
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# File paths
UNIFIED_DATA_FILE = RAW_DATA_DIR / "ethiopia_fi_unified_data.xlsx"
REFERENCE_CODES_FILE = RAW_DATA_DIR / "reference_codes.xlsx"
ENRICHED_DATA_FILE = PROCESSED_DATA_DIR / "ethiopia_fi_unified_data_enriched.xlsx"
FORECAST_RESULTS_FILE = PROCESSED_DATA_DIR / "forecast_results.csv"

# Forecast settings
FORECAST_YEARS = 3
CONFIDENCE_LEVEL = 0.95