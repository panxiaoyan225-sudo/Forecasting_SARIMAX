# Forecasting with SARIMAX# 

A seasonal time series forecasting model using the **SARIMAX** (Seasonal AutoRegressive Integrated Moving Average with eXogenous regressors) algorithm to predict monthly airline passenger traffic.

## 🚀 Project Overview
The goal of this analysis is to model the historical growth and seasonal patterns of airline travelers and project those trends 24 months into the future. 

### Key Features:
* **Decomposition:** Analysis of Trend, Seasonality, and Residuals.
* **Stationarity Testing:** Implementation of the Augmented Dickey-Fuller (ADF) test.
* **Auto-Tuning:** Automated grid search for optimal $(p, d, q)$ and seasonal $(P, D, Q, s)$ hyperparameters based on AIC scores.
* **Forecasting:** 24-month projection with calculated confidence intervals.

---

## 🛠️ Technical Stack
* **Language:** Python 3.x
* **Data Handling:** `pandas`, `numpy`
* **Statistics/Modeling:** `statsmodels`
* **Visualization:** `matplotlib`

---

## 📋 Workflow Breakdown

### 1. Data Preparation
The dataset is loaded from a remote source, and the index is coerced into a datetime format with a specific "Monthly Start" (`MS`) frequency to satisfy `statsmodels` requirements.

### 2. Exploratory Data Analysis (EDA)
We use a **multiplicative decomposition** model. This is chosen because the seasonal amplitude in the passenger data increases proportionally with the overall trend.

### 3. Stationarity Check
A critical step in time series modeling. The ADF test determines if the series needs differencing to stabilize the mean and variance.

### 4. Hyperparameter Optimization
The script runs a nested loop to test combinations of parameters. 
* **AIC (Akaike Information Criterion)** is used as the primary metric. 
* A lower AIC indicates a better-fitting model that avoids overfitting.

### 5. Diagnostics & Forecasting
Before finalizing the forecast, we check:
* **Standardized Residuals:** Should appear as white noise.
* **Histogram/QQ-Plot:** Checks for normal distribution of errors.
* **Correlogram:** Ensures no significant autocorrelation remains in the residuals.

---

## 📊 Results
The final output generates a visualization showing:
1.  **Historical Data:** The actual observed passenger counts.
2.  **Point Forecast:** The predicted future values (Red Line).
3.  **Confidence Interval:** The range of uncertainty (Pink Shadow), providing a 95% probability of where future values will fall.

---

## ⚙️ How to Run
1. Ensure you have the required libraries installed:
   ```bash
   pip install pandas numpy matplotlib statsmodels