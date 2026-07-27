# 🇪🇹 Forecasting Financial Inclusion in Ethiopia

A production-grade data science project that forecasts Ethiopia's financial inclusion trends using historical Global Findex data, digital finance indicators, and interactive visualizations. The project provides actionable insights for policymakers, financial institutions, and development organizations by forecasting account ownership and digital payment adoption through 2027.

---

# Business Problem

Financial inclusion is a key driver of economic growth and poverty reduction. Ethiopia has experienced rapid expansion of digital financial services through initiatives such as Telebirr and M-PESA, yet forecasting future adoption remains challenging.

Government agencies, financial institutions, and development partners require reliable forecasts to:

* Monitor progress toward national financial inclusion targets.
* Evaluate the impact of digital financial services.
* Support evidence-based policy decisions.
* Identify future investment opportunities.

---

# Solution Overview

This project combines historical financial inclusion indicators with forecasting techniques to estimate future trends in financial access and digital payment usage.

The solution includes:

* Historical trend analysis
* Forecasting for 2025–2027
* Scenario analysis (Optimistic, Base, and Pessimistic)
* Interactive Streamlit dashboard
* Automated testing using Pytest
* Continuous Integration using GitHub Actions

---

# Key Features

* 📊 Interactive Streamlit dashboard
* 📈 Historical financial inclusion trends
* 🔮 Multi-scenario forecasting
* 📉 Confidence interval visualization
* 📥 Downloadable forecast results
* 🧪 Unit testing with Pytest
* ⚙️ Automated CI/CD using GitHub Actions
* 🏗️ Modular and maintainable project architecture

---

# Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Plotly
* SciPy
* Pytest
* GitHub Actions
* OpenPyXL

---

# Project Structure

```text
ethiopia-fi-forecast/

├── dashboard/
│   ├── app.py
│   └── pages/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── config.py
│   ├── constants.py
│   ├── data_loader.py
│   ├── forecasting.py
│   ├── utils.py
│   └── visualization.py
│
├── tests/
│
├── .github/
│   └── workflows/
│
├── requirements.txt
└── README.md
```

---

# Dashboard

The dashboard provides four major views:

* **Overview** – Key financial inclusion indicators and summary metrics.
* **Historical Trends** – Interactive exploration of historical financial inclusion data.
* **Forecasts** – Projected trends for 2025–2027 with confidence intervals.
* **Inclusion Projections** – Comparison of future scenarios and progress toward financial inclusion goals.

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Maria-Biruk/ethiopia-fi-forecast.git
```

Move into the project directory:

```bash
cd ethiopia-fi-forecast
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Run the Dashboard

```bash
streamlit run dashboard/app.py
```

---

# Testing

Run all unit tests:

```bash
pytest
```

Current testing status:

* ✅ 5 Unit Tests
* ✅ All tests passing
* ✅ GitHub Actions CI pipeline configured

---

# Business Impact

This project demonstrates how forecasting can support financial decision-making by:

* Anticipating future financial inclusion trends.
* Supporting strategic planning for digital finance initiatives.
* Helping policymakers evaluate progress toward inclusion targets.
* Providing transparent and reproducible analytical workflows.

---

# Future Improvements

* Integrate real-time financial datasets.
* Evaluate additional forecasting models.
* Deploy the dashboard to a cloud platform.
* Add advanced model explainability where applicable.
* Expand the dashboard with additional socioeconomic indicators.

---

# Author

**Maya Brook**

Computer Science Student | Aspiring Data Engineer

GitHub: https://github.com/Maria-Biruk

LinkedIn: https://www.linkedin.com/in/maria-brook-2a6b91363
