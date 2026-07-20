import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Trends", layout="wide")

st.title("📈 Financial Inclusion Trends")

# Load data
BASE_DIR = Path(__file__).resolve().parents[2]
DATA_FILE = BASE_DIR / "data" / "processed" / "ethiopia_fi_unified_data_enriched.xlsx"

df = pd.read_excel(DATA_FILE)

# Keep only observations
df = df[df["record_type"] == "observation"].copy()
df["year"] = pd.to_datetime(df["observation_date"]).dt.year

# Sidebar filter
indicator = st.sidebar.selectbox(
    "Select Indicator",
    sorted(df["indicator"].dropna().unique())
)

filtered = df[df["indicator"] == indicator]

# Interactive line chart
fig = px.line(
    filtered,
    x="year",
    y="value_numeric",
    color="gender",
    markers=True,
    title=indicator,
)

st.plotly_chart(fig, use_container_width=True)

# Interactive bar chart
bar = px.bar(
    filtered,
    x="year",
    y="value_numeric",
    color="gender",
    title=f"{indicator} by Year",
)

st.plotly_chart(bar, use_container_width=True)

# Download button
st.download_button(
    "⬇ Download Filtered Data",
    filtered.to_csv(index=False),
    file_name="filtered_data.csv",
    mime="text/csv",
)

st.dataframe(filtered)