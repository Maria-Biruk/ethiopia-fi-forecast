import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(page_title="Inclusion Projections", layout="wide")

st.title("🎯 Financial Inclusion Projections")

st.markdown("""
This page evaluates Ethiopia's progress toward the national financial inclusion
target using forecasted account ownership for 2027. Compare different scenarios
and assess whether projected growth is sufficient to achieve the target.
""")

st.divider()

# -------------------------------------------------
# Load Forecast Data
# -------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[2]

FORECAST_FILE = BASE_DIR / "data" / "processed" / "forecast_results.csv"

forecast_df = pd.read_csv(FORECAST_FILE)

TARGET = 60

# -------------------------------------------------
# Scenario Selection
# -------------------------------------------------
scenario = st.selectbox(
    "Select Forecast Scenario",
    [
        "Base",
        "Optimistic",
        "Pessimistic",
    ],
)

if scenario == "Base":
    projected = forecast_df["Access_Baseline"].iloc[-1]
elif scenario == "Optimistic":
    projected = forecast_df["Access_Optimistic"].iloc[-1]
else:
    projected = forecast_df["Access_Pessimistic"].iloc[-1]

gap = max(0, TARGET - projected)
progress = min(projected / TARGET, 1.0)

# -------------------------------------------------
# KPI Summary
# -------------------------------------------------
st.subheader("2027 Projection Summary")

c1, c2, c3 = st.columns(3)

c1.metric(
    "Projected Account Ownership",
    f"{projected:.1f}%"
)

c2.metric(
    "National Target",
    f"{TARGET}%"
)

c3.metric(
    "Remaining Gap",
    f"{gap:.1f}%"
)

st.divider()

# -------------------------------------------------
# Gauge Chart
# -------------------------------------------------
fig = go.Figure(
    go.Indicator(
        mode="gauge+number",
        value=projected,
        title={"text": "Projected Account Ownership (2027)"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "royalblue"},
            "steps": [
                {"range": [0, TARGET], "color": "lightgray"},
                {"range": [TARGET, 100], "color": "lightgreen"},
            ],
            "threshold": {
                "line": {
                    "color": "red",
                    "width": 4,
                },
                "value": TARGET,
            },
        },
    )
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------------------------------
# Progress Indicator
# -------------------------------------------------
st.subheader("Progress Toward National Target")

st.progress(progress)

st.write(
    f"**Progress:** {progress * 100:.1f}% of the national financial inclusion target achieved."
)

st.divider()

# -------------------------------------------------
# Executive Summary
# -------------------------------------------------
st.subheader("Executive Summary")

if projected >= TARGET:
    st.success(f"""
Under the **{scenario}** scenario, Ethiopia is projected to achieve the
national financial inclusion target by 2027 with an estimated account
ownership rate of **{projected:.1f}%**.
""")
else:
    st.warning(f"""
Under the **{scenario}** scenario, Ethiopia is projected to reach
**{projected:.1f}%** account ownership by 2027.

This remains **{gap:.1f} percentage points** below the national target
of **{TARGET}%**.
""")

# -------------------------------------------------
# Key Growth Drivers
# -------------------------------------------------
st.subheader("Key Growth Drivers")

st.success("""
- 📱 Expansion of Telebirr and mobile money services
- 🪪 National Fayda Digital ID rollout
- 🏦 Continued expansion of formal banking services
- 💳 Increased adoption of digital payment platforms
- 🌐 Improved digital infrastructure and financial accessibility
""")

# -------------------------------------------------
# Risks and Uncertainties
# -------------------------------------------------
st.subheader("Risks and Uncertainties")

st.info("""
Several factors may influence future financial inclusion outcomes:

- Limited historical observations available for forecasting.
- Changes in government policy or regulation.
- Economic growth and inflation.
- Mobile network and digital infrastructure expansion.
- Adoption rates in rural and underserved communities.
""")

# -------------------------------------------------
# Strategic Recommendations
# -------------------------------------------------
st.subheader("Recommendations")

st.markdown("""
To accelerate financial inclusion, stakeholders should consider:

1. Expanding digital financial infrastructure.
2. Increasing financial literacy programs.
3. Encouraging mobile banking adoption.
4. Supporting fintech innovation.
5. Monitoring financial inclusion indicators regularly.
""")