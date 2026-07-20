import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Overview", layout="wide")

st.title("📊 Financial Inclusion Overview")

# Load data
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]

DATA_FILE = BASE_DIR / "data" / "processed" / "ethiopia_fi_unified_data_enriched.xlsx"

df = pd.read_excel(DATA_FILE)

# -----------------------------
# Current Metrics
# -----------------------------
access = df[
    (df["indicator_code"] == "ACC_OWNERSHIP") &
    (df["record_type"] == "observation")
]

usage = df[
    (df["indicator_code"] == "USG_DIGITAL_PAYMENT") &
    (df["record_type"] == "observation")
]

current_access = access.sort_values("observation_date").iloc[-1]["value_numeric"]
current_usage = usage.sort_values("observation_date").iloc[-1]["value_numeric"]

growth = current_access - access.sort_values("observation_date").iloc[-2]["value_numeric"]

# Example P2P/ATM ratio
p2p_ratio = 1.35

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Account Ownership",
    f"{current_access:.1f}%"
)

col2.metric(
    "Digital Payment Usage",
    f"{current_usage:.1f}%"
)

col3.metric(
    "Growth Since Previous Survey",
    f"{growth:.1f}%"
)

col4.metric(
    "P2P / ATM Ratio",
    f"{p2p_ratio:.2f}"
)

st.divider()

# -----------------------------
# Account Ownership Trend
# -----------------------------
access["year"] = pd.to_datetime(access["observation_date"]).dt.year

fig = px.line(
    access,
    x="year",
    y="value_numeric",
    markers=True,
    title="Account Ownership Over Time"
)

st.plotly_chart(fig, use_container_width=True)

st.dataframe(access)