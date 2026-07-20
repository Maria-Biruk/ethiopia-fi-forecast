import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(page_title="Forecasts", layout="wide")

st.title("📈 Forecasts (2025–2027)")

# -------------------------------------------------
# Load Data
# -------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[2]

DATA_FILE = BASE_DIR / "data" / "processed" / "ethiopia_fi_unified_data_enriched.xlsx"
FORECAST_FILE = BASE_DIR / "data" / "processed" / "forecast_results.csv"

df = pd.read_excel(DATA_FILE)
forecast_df = pd.read_csv(FORECAST_FILE)

# -------------------------------------------------
# Indicator Selector
# -------------------------------------------------
indicator = st.selectbox(
    "Select Forecast Indicator",
    ["Account Ownership", "Digital Payment Usage"]
)

# -------------------------------------------------
# Scenario Selector
# -------------------------------------------------
scenario = st.selectbox(
    "Select Scenario",
    ["Base", "Optimistic", "Pessimistic"]
)

# -------------------------------------------------
# Historical Data
# -------------------------------------------------
if indicator == "Account Ownership":

    historical = df[
        (df["indicator_code"] == "ACC_OWNERSHIP") &
        (df["record_type"] == "observation")
    ].copy()

    historical["year"] = pd.to_datetime(
        historical["observation_date"]
    ).dt.year

    historical = historical.sort_values("year")

    if scenario == "Base":
        forecast = forecast_df["Access_Baseline"]
    elif scenario == "Optimistic":
        forecast = forecast_df["Access_Optimistic"]
    else:
        forecast = forecast_df["Access_Pessimistic"]

    lower = forecast_df["Access_CI_Low"]
    upper = forecast_df["Access_CI_High"]

else:

    historical = df[
        (df["indicator_code"] == "USG_DIGITAL_PAYMENT") &
        (df["record_type"] == "observation")
    ].copy()

    historical["year"] = pd.to_datetime(
        historical["observation_date"]
    ).dt.year

    historical = historical.sort_values("year")

    if scenario == "Base":
        forecast = forecast_df["Usage_Baseline"]
    elif scenario == "Optimistic":
        forecast = forecast_df["Usage_Optimistic"]
    else:
        forecast = forecast_df["Usage_Pessimistic"]

    lower = forecast_df["Usage_CI_Low"]
    upper = forecast_df["Usage_CI_High"]

years = forecast_df["Year"]

# -------------------------------------------------
# Key Metrics
# -------------------------------------------------
st.subheader("Forecast Summary")

col1, col2, col3 = st.columns(3)

col1.metric("2025", f"{forecast.iloc[0]:.1f}%")
col2.metric("2026", f"{forecast.iloc[1]:.1f}%")
col3.metric("2027", f"{forecast.iloc[2]:.1f}%")

st.divider()

# -------------------------------------------------
# Forecast Chart
# -------------------------------------------------
fig = go.Figure()

# Historical Data
fig.add_trace(
    go.Scatter(
        x=historical["year"],
        y=historical["value_numeric"],
        mode="lines+markers",
        name="Historical",
    )
)

# Forecast
fig.add_trace(
    go.Scatter(
        x=years,
        y=forecast,
        mode="lines+markers",
        name=f"{scenario} Forecast",
    )
)

# Confidence Interval
fig.add_trace(
    go.Scatter(
        x=list(years) + list(years[::-1]),
        y=list(upper) + list(lower[::-1]),
        fill="toself",
        fillcolor="rgba(0,100,255,0.2)",
        line=dict(color="rgba(255,255,255,0)"),
        hoverinfo="skip",
        name="Confidence Interval",
    )
)

fig.update_layout(
    title=f"{indicator} Forecast ({scenario} Scenario)",
    xaxis_title="Year",
    yaxis_title="Percentage of Adults",
    hovermode="x unified",
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------------------------------
# Forecast Table
# -------------------------------------------------
st.subheader("Forecast Results")

st.dataframe(forecast_df, use_container_width=True)

# -------------------------------------------------
# Download Button
# -------------------------------------------------
st.download_button(
    "⬇ Download Forecast Results",
    forecast_df.to_csv(index=False),
    file_name="forecast_results.csv",
    mime="text/csv",
)

# -------------------------------------------------
# Interpretation
# -------------------------------------------------
st.subheader("Interpretation")

if indicator == "Account Ownership":
    st.info(
        "The forecast suggests that account ownership will continue "
        "to grow through 2027. Scenario differences reflect varying "
        "assumptions about the impact of financial inclusion initiatives "
        "such as Telebirr expansion and the Fayda Digital ID rollout."
    )
else:
    st.info(
        "Digital payment usage is projected to increase steadily "
        "between 2025 and 2027. Higher adoption is expected under the "
        "optimistic scenario due to continued growth in mobile money "
        "and digital financial services."
    )