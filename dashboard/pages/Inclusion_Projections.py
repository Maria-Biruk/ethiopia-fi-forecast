import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(page_title="Inclusion Projections", layout="wide")

st.title("🎯 Financial Inclusion Projections")

# -----------------------------------------
# Load Forecast Data
# -----------------------------------------
BASE_DIR = Path(__file__).resolve().parents[2]

FORECAST_FILE = BASE_DIR / "data" / "processed" / "forecast_results.csv"

forecast_df = pd.read_csv(FORECAST_FILE)

TARGET = 60

# -----------------------------------------
# Scenario Selector
# -----------------------------------------
scenario = st.selectbox(
    "Select Scenario",
    ["Base", "Optimistic", "Pessimistic"]
)

# -----------------------------------------
# Use 2027 Projection
# -----------------------------------------
if scenario == "Base":
    projected = forecast_df["Access_Baseline"].iloc[-1]

elif scenario == "Optimistic":
    projected = forecast_df["Access_Optimistic"].iloc[-1]

else:
    projected = forecast_df["Access_Pessimistic"].iloc[-1]

progress = min(projected / TARGET, 1.0)

# -----------------------------------------
# Gauge Chart
# -----------------------------------------
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=projected,
    title={"text": "Projected Account Ownership (2027)"},
    gauge={
        "axis": {"range": [0, 100]},
        "bar": {"color": "royalblue"},
        "threshold": {
            "line": {"color": "red", "width": 4},
            "value": TARGET
        }
    }
))

st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------
# Progress
# -----------------------------------------
st.subheader("Progress Toward Target")

st.progress(progress)

col1, col2, col3 = st.columns(3)

col1.metric(
    "2027 Projection",
    f"{projected:.1f}%"
)

col2.metric(
    "National Target",
    f"{TARGET}%"
)

col3.metric(
    "Gap Remaining",
    f"{max(0, TARGET-projected):.1f}%"
)

st.divider()

# -----------------------------------------
# Key Findings
# -----------------------------------------
st.subheader("Key Findings")

st.markdown(f"""
### Will Ethiopia reach the 60% target?

Under the **{scenario}** scenario, the projected account ownership
rate in **2027** is **{projected:.1f}%**.

""")

if projected >= TARGET:
    st.success("✅ The forecast suggests the national target is achieved.")
else:
    st.warning(
        f"⚠️ The forecast remains {TARGET - projected:.1f} percentage points below the target."
    )

st.subheader("Major Drivers")

st.markdown("""
- 📱 Expansion of Telebirr and mobile money services
- 🪪 Rollout of the Fayda Digital ID program
- 🏦 Growth in formal financial services
- 💳 Increased adoption of digital payments
""")

st.subheader("Key Uncertainties")

st.markdown("""
- Limited number of historical Findex observations
- Pace of policy implementation
- Economic conditions
- Technology adoption across urban and rural areas
""")