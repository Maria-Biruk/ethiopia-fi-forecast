import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(page_title="Forecasts", layout="wide")

st.title("📈 Financial Inclusion Forecasts (2025–2027)")

st.markdown("""
This dashboard presents forecasted financial inclusion indicators for Ethiopia
under multiple scenarios. Compare historical performance with projected
outcomes and explore how different assumptions influence future financial
access and digital payment adoption.
""")

st.divider()

# -------------------------------------------------
# Load Data
# -------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[2]

DATA_FILE = BASE_DIR / "data" / "processed" / "ethiopia_fi_unified_data_enriched.xlsx"
FORECAST_FILE = BASE_DIR / "data" / "processed" / "forecast_results.csv"

df = pd.read_excel(DATA_FILE)
forecast_df = pd.read_csv(FORECAST_FILE)

# -------------------------------------------------
# Selectors
# -------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    indicator = st.selectbox(
        "Forecast Indicator",
        [
            "Account Ownership",
            "Digital Payment Usage",
        ],
    )

with col2:
    scenario = st.selectbox(
        "Scenario",
        [
            "Base",
            "Optimistic",
            "Pessimistic",
        ],
    )

# -------------------------------------------------
# Historical Data
# -------------------------------------------------
if indicator == "Account Ownership":

    historical = df[
        (df["indicator_code"] == "ACC_OWNERSHIP")
        & (df["record_type"] == "observation")
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
        (df["indicator_code"] == "USG_DIGITAL_PAYMENT")
        & (df["record_type"] == "observation")
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
# KPI Summary
# -------------------------------------------------
st.subheader("Forecast Summary")

latest_actual = historical.iloc[-1]["value_numeric"]
projected_2027 = forecast.iloc[-1]
growth = projected_2027 - latest_actual

c1, c2, c3, c4 = st.columns(4)

c1.metric("Forecast 2025", f"{forecast.iloc[0]:.1f}%")
c2.metric("Forecast 2026", f"{forecast.iloc[1]:.1f}%")
c3.metric("Forecast 2027", f"{forecast.iloc[2]:.1f}%")
c4.metric("Projected Growth", f"{growth:.1f}%")

st.divider()

# -------------------------------------------------
# Forecast Chart
# -------------------------------------------------
fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=historical["year"],
        y=historical["value_numeric"],
        mode="lines+markers",
        name="Historical Data",
    )
)

fig.add_trace(
    go.Scatter(
        x=years,
        y=forecast,
        mode="lines+markers",
        name=f"{scenario} Forecast",
    )
)

fig.add_trace(
    go.Scatter(
        x=list(years) + list(years[::-1]),
        y=list(upper) + list(lower[::-1]),
        fill="toself",
        fillcolor="rgba(0,100,255,0.2)",
        line=dict(color="rgba(255,255,255,0)"),
        hoverinfo="skip",
        name="95% Confidence Interval",
    )
)

fig.update_layout(
    title=f"{indicator}: Historical Trend and {scenario} Forecast",
    xaxis_title="Year",
    yaxis_title="Percentage of Adults",
    hovermode="x unified",
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------------------------------
# Business Impact
# -------------------------------------------------
st.subheader("Business Impact")

st.success(f"""
### Key Insights

• Under the **{scenario}** scenario, **{indicator}** is expected to continue
growing through 2027.

• Confidence intervals highlight the uncertainty around future projections
while providing a reasonable range for expected outcomes.

• These forecasts can support policymakers, financial institutions,
and development partners in planning investments and financial inclusion
initiatives.

• Scenario analysis helps stakeholders evaluate both opportunities and risks
associated with Ethiopia's digital financial transformation.
""")

# -------------------------------------------------
# Forecast Table
# -------------------------------------------------
st.subheader("Forecast Dataset")

with st.expander("View Forecast Results"):
    st.dataframe(
        forecast_df,
        use_container_width=True,
    )

# -------------------------------------------------
# Download
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
    st.info("""
Financial account ownership is projected to continue increasing through
2027. Continued expansion of digital financial services, improved access
to banking infrastructure, and national financial inclusion initiatives
are expected to support this positive trend.
""")
else:
    st.info("""
Digital payment adoption is expected to grow steadily over the forecast
period. Expansion of mobile money services, digital banking platforms,
and broader digital identification initiatives could further accelerate
usage under the optimistic scenario.
""")