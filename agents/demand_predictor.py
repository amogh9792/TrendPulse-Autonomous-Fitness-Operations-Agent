from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

def train_demand_model(df):
    df["day"] = df["date"].dt.day
    df["month"] = df["date"].dt.month
    features = ["day", "month", "trend_score"]
    X = df[features]
    y = df["units_sold"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)
    print("✅ Demand model trained!")
    return model

def predict_demand(model, df):
    df["day"] = df["date"].dt.day
    df["month"] = df["date"].dt.month
    features = ["day", "month", "trend_score"]
    df["predicted_units"] = model.predict(df[features]).astype(int)
    return df
