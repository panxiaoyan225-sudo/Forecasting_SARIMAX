import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import itertools

# 1. Load Data (Standard Airline Passengers dataset)
# Link to dataset: https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv
df = pd.read_csv('airline-passengers.csv', parse_dates=['Month'], index_col='Month')
y = df['Passengers']

# 2. Define Parameter Ranges for Grid Search
p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
# Seasonal components (P, D, Q, s) - s=12 for monthly data
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

# 3. Grid Search to find the best SARIMAX parameters based on AIC
best_aic = float("inf")
best_param = None
best_seasonal_param = None

for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(y,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)
            results = mod.fit(disp=False)
            if results.aic < best_aic:
                best_aic = results.aic
                best_param = param
                best_seasonal_param = param_seasonal
        except:
            continue

print(f'Best SARIMAX: {best_param}x{best_seasonal_param} - AIC:{best_aic}')

# 4. Fit the final model
final_model = sm.tsa.statespace.SARIMAX(y,
                                        order=best_param,
                                        seasonal_order=best_seasonal_param)
results = final_model.fit()

# 5. Forecasting (predicting the next 24 months)
pred_uc = results.get_forecast(steps=24)
pred_ci = pred_uc.conf_int()

# 6. Visualization
ax = y.plot(label='Observed', figsize=(12, 6))
pred_uc.predicted_mean.plot(ax=ax, label='Forecast')
ax.fill_between(pred_ci.index, pred_ci.iloc[:, 0], pred_ci.iloc[:, 1], color='k', alpha=.15)
plt.legend()
plt.show()