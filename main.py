import os
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import random

from utils.data_cleaning import load_and_clean_sales, load_and_clean_trends, merge_sales_trends
from agents.demand_predictor import train_demand_model, predict_demand
from agents.action_recommender import generate_recommendations
from agents.notifier import send_alert

# -------------------------------
# Create folders
# -------------------------------
os.makedirs("data", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

# -------------------------------
# Generate Mock Data
# -------------------------------
cities = ["Bangalore", "Delhi", "Mumbai", "Chennai", "Hyderabad"]
products = ["Resistance Band", "Kettlebell", "Yoga Mat", "Dumbbell Set", "Protein Powder", "Treadmill", "Exercise Ball"]
price_dict = {
    "Resistance Band": 500,
    "Kettlebell": 1200,
    "Yoga Mat": 700,
    "Dumbbell Set": 2500,
    "Protein Powder": 1500,
    "Treadmill": 25000,
    "Exercise Ball": 900
}

start_date = datetime(2025, 8, 1)
num_days = 60
sales_records = []
trend_records = []

for day_offset in range(num_days):
    date = start_date + timedelta(days=day_offset)
    for city in cities:
        for product in products:
            units_sold = max(0, int(np.random.normal(loc=50, scale=20)))
            price = price_dict[product]
            sales_records.append([date.strftime("%Y-%m-%d"), city, product, units_sold, price])
    for product in products:
        base = random.randint(30, 70)
        trend_score = min(100, max(0, int(np.random.normal(loc=base, scale=10))))
        trend_records.append([date.strftime("%Y-%m-%d"), product, trend_score])

sales_df = pd.DataFrame(sales_records, columns=["date", "city", "product", "units_sold", "price"])
sales_df.to_csv("data/sales_history.csv", index=False)

trends_df = pd.DataFrame(trend_records, columns=["date", "product", "trend_score"])
trends_df.to_csv("data/trends.csv", index=False)

print("✅ Mock data generated")

# -------------------------------
# Load & merge
# -------------------------------
sales_df = load_and_clean_sales()
trends_df = load_and_clean_trends()
merged_df = merge_sales_trends(sales_df, trends_df)

# -------------------------------
# Train model
# -------------------------------
model = train_demand_model(merged_df)

# -------------------------------
# Predict next 7 days
# -------------------------------
future_dates = [datetime(2025, 11, 20) + timedelta(days=i) for i in range(7)]
future_records = []

for date in future_dates:
    for city in cities:
        for product in products:
            trend_score = int(trends_df[trends_df["product"] == product]["trend_score"].mean() * 1.2)  # boost for demo
            future_records.append({
                "date": date,
                "city": city,
                "product": product,
                "trend_score": trend_score
            })

future_df = pd.DataFrame(future_records)
future_df = predict_demand(model, future_df)

# -------------------------------
# Generate recommendations
# -------------------------------
recs = generate_recommendations(future_df, threshold=40)

# -------------------------------
# Alerts
# -------------------------------
send_alert(recs)

# -------------------------------
# Save for dashboard
# -------------------------------
future_df.to_csv("data/processed/predictions.csv", index=False)
recs.to_csv("data/processed/recommendations.csv", index=False)
print("✅ Predictions and recommendations saved in data/processed/")
