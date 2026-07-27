import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Historical Trends", layout="wide")

# --------------------------------------------------
# Load Data
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_FILE = BASE_DIR / "data" / "processed" / "ethiopia_fi_unified_data_enriched.xlsx"

df = pd.read_excel(DATA_FILE)

df = df[df["record_type"] == "observation"].copy()
df["year"] = pd.to_datetime(df["observation_date"]).dt.year

st.title("📈 Historical Financial Inclusion Trends")

st.markdown("""
Explore historical financial inclusion indicators across Ethiopia.
Use the filters below to compare trends over time and identify changes
in financial access and digital payment adoption.
""")

# --------------------------------------------------
# Filters
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    indicator = st.selectbox(
        "Select Indicator",
        sorted(df["indicator"].dropna().unique())
    )

with col2:
    gender = st.selectbox(
        "Select Gender",
        sorted(df["gender"].fillna("All").unique())
    )

filtered = df[df["indicator"] == indicator]

if gender != "All":
    filtered = filtered[filtered["gender"] == gender]

# --------------------------------------------------
# KPI Summary
# --------------------------------------------------

latest_value = filtered.iloc[-1]["value_numeric"]
average_value = filtered["value_numeric"].mean()
first_value = filtered.iloc[0]["value_numeric"]
growth = latest_value - first_value

st.subheader("Trend Summary")

c1, c2, c3 = st.columns(3)

c1.metric(
    "Latest Value",
    f"{latest_value:.1f}%"
)

c2.metric(
    "Average",
    f"{average_value:.1f}%"
)

c3.metric(
    "Overall Growth",
    f"{growth:.1f}%"
)

st.divider()

# --------------------------------------------------
# Line Chart
# --------------------------------------------------

fig = px.line(
    filtered,
    x="year",
    y="value_numeric",
    color="gender",
    markers=True,
    title=f"{indicator} Over Time"
)

fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Value (%)"
)

st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------------
# Bar Chart
# --------------------------------------------------

bar = px.bar(
    filtered,
    x="year",
    y="value_numeric",
    color="gender",
    title="Yearly Comparison"
)

st.plotly_chart(bar, use_container_width=True)

# --------------------------------------------------
# Business Insights
# --------------------------------------------------

st.subheader("Business Insights")

st.info(f"""
The selected indicator **{indicator}** demonstrates historical changes
in financial inclusion.

These trends can help policymakers and financial institutions evaluate
progress, identify underserved populations, and support strategic planning
for future digital financial services.
""")

# --------------------------------------------------
# Download Data
# --------------------------------------------------

st.download_button(
    "⬇ Download Filtered Data",
    filtered.to_csv(index=False),
    file_name="filtered_data.csv",
    mime="text/csv",
)

# --------------------------------------------------
# Data Preview
# --------------------------------------------------

with st.expander("View Filtered Data"):
    st.dataframe(filtered, use_container_width=True)