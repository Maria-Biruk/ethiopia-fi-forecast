from src.data_loader import load_unified_data, load_reference_codes, REQUIRED_COLUMNS


def test_unified_data_loads():
    df = load_unified_data()
    assert len(df) == 57  # 43 main sheet + 14 impact_sheet rows
    assert REQUIRED_COLUMNS.issubset(set(df.columns))


def test_reference_codes_loads():
    df = load_reference_codes()
    assert len(df) == 71
    assert {"field", "code", "description"}.issubset(set(df.columns))


def test_record_types_are_valid():
    df = load_unified_data()
    valid = {"observation", "event", "impact_link", "target"}
    assert set(df["record_type"].dropna().unique()).issubset(valid)