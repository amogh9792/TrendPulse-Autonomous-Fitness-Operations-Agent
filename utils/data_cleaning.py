import pandas as pd

def load_and_clean_sales(file_path="data/sales_history.csv"):
    df = pd.read_csv(file_path, parse_dates=["date"])
    df["city"] = df["city"].str.strip().str.title()
    df["product"] = df["product"].str.strip().str.title()
    return df

def load_and_clean_trends(file_path="data/trends.csv"):
    df = pd.read_csv(file_path, parse_dates=["date"])
    df["product"] = df["product"].str.strip().str.title()
    return df

def merge_sales_trends(sales_df, trends_df):
    merged = sales_df.merge(trends_df, on=["date", "product"], how="left")
    merged["trend_score"].fillna(50, inplace=True)  # default trend score
    return merged
