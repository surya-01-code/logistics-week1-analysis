"""
Week 1 Logistics Analytics — Starter Analysis Plan
This file is a template. Replace the input filename and column names with the actual dataset.
"""

import pandas as pd
import numpy as np

# 1. Load
df = pd.read_csv("logistics_data.csv")

# 2. Basic quality checks
print(df.shape)
print(df.dtypes)
print(df.isna().sum())
print("Duplicates:", df.duplicated().sum())

# 3. Example datetime features
df["dispatch_time"] = pd.to_datetime(df["dispatch_time"], errors="coerce")
df["delivery_time"] = pd.to_datetime(df["delivery_time"], errors="coerce")
df["promised_time"] = pd.to_datetime(df["promised_time"], errors="coerce")

df["lead_time_hours"] = (
    df["delivery_time"] - df["dispatch_time"]
).dt.total_seconds() / 3600

df["delay_hours"] = (
    df["delivery_time"] - df["promised_time"]
).dt.total_seconds() / 3600

# 4. KPI examples
on_time_rate = (df["delay_hours"] <= 0).mean() * 100
avg_lead_time = df["lead_time_hours"].mean()

print("On-time delivery rate:", round(on_time_rate, 2), "%")
print("Average lead time:", round(avg_lead_time, 2), "hours")

# 5. Regression — implement after confirming columns
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_absolute_error, r2_score

# 6. Clustering — implement after constructing customer/route features
# from sklearn.preprocessing import StandardScaler
# from sklearn.cluster import KMeans
# from sklearn.metrics import silhouette_score

# 7. Optimization
# Define decision variables, objective and constraints.
# Use an appropriate MILP/VRP solver after the business rules are confirmed.
