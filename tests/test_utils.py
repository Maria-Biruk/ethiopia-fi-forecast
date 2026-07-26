from pathlib import Path

import pandas as pd

from src.utils import dataframe_summary, ensure_directory


def test_dataframe_summary():
    df = pd.DataFrame({"A": [1, 2], "B": [3, None]})

    summary = dataframe_summary(df)

    assert summary["rows"] == 2
    assert summary["columns"] == 2
    assert summary["missing_values"] == 1


def test_ensure_directory(tmp_path):
    new_dir = tmp_path / "output"

    ensure_directory(new_dir)

    assert new_dir.exists()
    assert new_dir.is_dir()