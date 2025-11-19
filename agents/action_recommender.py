import pandas as pd

def generate_recommendations(predictions_df, threshold=40):
    """
    Generate actionable recommendations.
    threshold: units above which reorder is suggested
    """
    recs = []
    for _, row in predictions_df.iterrows():
        if row["predicted_units"] >= threshold:
            recs.append({
                "date": row["date"].strftime("%Y-%m-%d"),
                "city": row["city"],
                "product": row["product"],
                "action": f"Reorder {row['predicted_units']} units"
            })

    if not recs:
        recs.append({
            "date": predictions_df["date"].iloc[0].strftime("%Y-%m-%d"),
            "city": predictions_df["city"].iloc[0],
            "product": predictions_df["product"].iloc[0],
            "action": f"Reorder {max(predictions_df['predicted_units'].iloc[0], 40)} units"
        })

    return pd.DataFrame(recs)
