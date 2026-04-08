# Forecasting with SARIMAX on Azure Databricks

A seasonal time series forecasting model using the **SARIMAX** algorithm. The analysis is performed within **Azure Databricks**, utilizing its distributed computing capabilities and integrated Git version control.

## 🚀 Project Overview
The goal of this analysis is to model the historical growth and seasonal patterns of airline travelers and project those trends 24 months into the future. 

### Key Features:
* **Cloud-Native Workflow:** Developed using Azure Databricks notebooks for interactive data exploration.
* **Decomposition:** Analysis of Trend, Seasonality, and Residuals using `statsmodels`.
* **Stationarity Testing:** Implementation of the Augmented Dickey-Fuller (ADF) test.
* **Auto-Tuning:** Automated grid search for optimal $(p, d, q) \times (P, D, Q, s)$ hyperparameters based on AIC scores.
* **Forecasting:** 24-month projection with calculated 95% confidence intervals.

---

## 🛠️ Technical Stack
* **Platform:** Azure Databricks (Standard/Premium Cluster)
* **Language:** Python 3.x
* **Data Handling:** `pandas`, `numpy`
* **Statistics/Modeling:** `statsmodels`
* **Visualization:** `matplotlib`, `Databricks Display`

---

## 📋 Azure Databricks Implementation

### 1. Workspace Integration
This project is managed via **Databricks Git Folders (Repos)**. This allows for a seamless CI/CD experience where code is developed in Databricks and synced directly to GitHub.

### 2. Environment Setup
The notebook is designed to run on a Databricks Runtime (ML recommended). Key dependencies are installed via `%pip` magic commands or cluster-scoped libraries:
```python
%pip install statsmodels pandas matplotlib