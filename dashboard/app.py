import streamlit as st

st.set_page_config(
    page_title="Ethiopia Financial Inclusion Dashboard",
    page_icon="🇪🇹",
    layout="wide",
)

st.title("🇪🇹 Ethiopia Financial Inclusion Forecast Dashboard")

st.markdown("""
### Finance Sector Analytics Platform

This interactive dashboard forecasts Ethiopia's financial inclusion trends using
historical financial data and scenario-based forecasting.

The application supports policymakers, financial institutions, and development
organizations in monitoring progress toward greater financial inclusion and
understanding future trends.
""")

st.divider()

st.subheader("Project Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Forecast Period",
        "2025–2027"
    )

with col2:
    st.metric(
        "Forecast Scenarios",
        "3"
    )

with col3:
    st.metric(
        "Dashboard Pages",
        "4"
    )

st.divider()

st.subheader("Dashboard Features")

st.markdown("""
- 📊 **Overview** – Summary of Ethiopia's financial inclusion indicators.
- 📈 **Historical Trends** – Explore historical financial inclusion data.
- 🔮 **Forecasts** – View projected trends with confidence intervals.
- 🎯 **Inclusion Projections** – Compare optimistic, base, and pessimistic scenarios.
""")

st.divider()

st.subheader("Business Impact")

st.success("""
This dashboard helps stakeholders:

- Monitor financial inclusion progress.
- Support evidence-based policy decisions.
- Evaluate digital financial service adoption.
- Forecast future financial access trends.
""")

st.info("👈 Use the sidebar to navigate through the dashboard pages.")

st.caption(
    "Developed for the 10 Academy Artificial Intelligence Mastery Program | Week 12 Capstone"
)