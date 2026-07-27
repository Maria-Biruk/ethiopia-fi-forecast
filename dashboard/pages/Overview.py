import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Financial Inclusion Overview", layout="wide")

# --------------------------------------------------
# Load Data
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_FILE = BASE_DIR / "data" / "processed" / "ethiopia_fi_unified_data_enriched.xlsx"

df = pd.read_excel(DATA_FILE)

st.title("📊 Financial Inclusion Overview")
st.markdown("""
This page provides a high-level summary of Ethiopia's financial inclusion
performance using historical Global Findex indicators and digital finance data.
""")

# --------------------------------------------------
# Filter Data
# --------------------------------------------------

access = df[
    (df["indicator_code"] == "ACC_OWNERSHIP")
    & (df["record_type"] == "observation")
].copy()

usage = df[
    (df["indicator_code"] == "USG_DIGITAL_PAYMENT")
    & (df["record_type"] == "observation")
].copy()

access["year"] = pd.to_datetime(access["observation_date"]).dt.year
usage["year"] = pd.to_datetime(usage["observation_date"]).dt.year

current_access = access.iloc[-1]["value_numeric"]
current_usage = usage.iloc[-1]["value_numeric"]

growth = current_access - access.iloc[-2]["value_numeric"]

p2p_ratio = 1.35

# --------------------------------------------------
# KPI Cards
# --------------------------------------------------

st.subheader("Key Performance Indicators")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Account Ownership",
    f"{current_access:.1f}%",
    f"{growth:.1f}%"
)

c2.metric(
    "Digital Payment Usage",
    f"{current_usage:.1f}%"
)

c3.metric(
    "Forecast Horizon",
    "2025–2027"
)

c4.metric(
    "P2P / ATM Ratio",
    f"{p2p_ratio:.2f}"
)

st.divider()

# --------------------------------------------------
# Trend Chart
# --------------------------------------------------

fig = px.line(
    access,
    x="year",
    y="value_numeric",
    markers=True,
    title="Account Ownership Trend",
)

fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Population (%)",
)

st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------------
# Business Insights
# --------------------------------------------------

st.subheader("Business Insights")

st.success(
    """
• Financial account ownership has steadily increased over time.

• Digital financial services continue to expand across Ethiopia.

• Forecasts indicate continued growth through 2027.

• Policymakers and financial institutions can use these projections to
support investment and financial inclusion strategies.
"""
)

# --------------------------------------------------
# Data Preview
# --------------------------------------------------

with st.expander("View Processed Dataset"):
    st.dataframe(access, use_container_width=True)