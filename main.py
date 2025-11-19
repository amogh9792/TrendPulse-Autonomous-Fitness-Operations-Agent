import os
from datetime import datetime, timedelta
import pandas as pd
from utils.data_cleaning import load_and_clean_sales, load_and_clean_trends, merge_sales_trends
from agents.demand_predictor import train_demand_model, predict_demand
from agents.action_recommender import generate_recommendations
from agents.notifier import send_alert

os.makedirs("data/processed", exist_ok=True)

cities = ["Bangalore", "Delhi", "Mumbai", "Chennai", "Hyderabad"]
products = ["Resistance Band", "Kettlebell", "Yoga Mat", "Dumbbell Set", "Protein Powder", "Treadmill", "Exercise Ball"]

sales_df = load_and_clean_sales("data/sales_history.csv")
trends_df = load_and_clean_trends("data/trends.csv")
merged_df = merge_sales_trends(sales_df, trends_df)

model = train_demand_model(merged_df)

future_dates = [datetime(2025, 11, 20) + timedelta(days=i) for i in range(7)]
future_records = []

for date in future_dates:
    for city in cities:
        for product in products:
            trend_score = int(trends_df[trends_df["product"] == product]["trend_score"].mean() * 1.2)
            future_records.append({
                "date": date,
                "city": city,
                "product": product,
                "trend_score": trend_score
            })

future_df = pd.DataFrame(future_records)
future_df = predict_demand(model, future_df)

recs = generate_recommendations(future_df, threshold=40)
send_alert(recs)

future_df.to_csv("data/processed/predictions.csv", index=False)
recs.to_csv("data/processed/recommendations.csv", index=False)
print("✅ Predictions and recommendations saved in data/processed/")
