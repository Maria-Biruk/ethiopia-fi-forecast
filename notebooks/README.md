# 🇪🇹 Ethiopia Financial Inclusion Forecast Dashboard

## Overview

This project forecasts financial inclusion in Ethiopia using historical Global Findex data and key digital finance events.

The dashboard allows stakeholders to:

- Explore historical trends
- Analyze financial inclusion indicators
- View forecasts for 2025–2027
- Compare optimistic, base, and pessimistic scenarios
- Download forecast results

---

## Features

- 📊 Overview Dashboard
- 📈 Interactive Trend Analysis
- 🔮 Forecast Visualization
- 🎯 Inclusion Projection Dashboard
- 📥 CSV Download
- 📉 Confidence Intervals
- 🌍 Scenario Analysis

---

## Technology Stack

- Python
- Streamlit
- Pandas
- Plotly
- NumPy
- SciPy

---

## Project Structure

```
dashboard/
│
├── app.py
├── pages/
│   ├── 1_Overview.py
│   ├── 2_Trends.py
│   ├── 3_Forecasts.py
│   └── 4_Inclusion_Projections.py

data/
│
├── processed/
│   ├── ethiopia_fi_unified_data_enriched.xlsx
│   └── forecast_results.csv
```

---

## Installation

```bash
git clone <repository-url>

cd ethiopia-fi-forecast

pip install -r requirements.txt
```

---

## Run Dashboard

```bash
streamlit run dashboard/app.py
```

---

## Forecast Scenarios

- Base Scenario
- Optimistic Scenario
- Pessimistic Scenario

---

## Authors

10 Academy Week 11 Challenge
