import pandas as pd
import streamlit as st

st.title("TrendPulse Lite: Fitness Operations Agentic AI")

# Load CSVs safely
try:
    predictions = pd.read_csv("data/processed/predictions.csv")
except (FileNotFoundError, pd.errors.EmptyDataError):
    st.warning("Run run_trendpulse.py first to generate predictions.")
    predictions = pd.DataFrame()

try:
    recommendations = pd.read_csv("data/processed/recommendations.csv")
except (FileNotFoundError, pd.errors.EmptyDataError):
    st.warning("No recommended actions available.")
    recommendations = pd.DataFrame()

st.subheader("Predicted Demand for Next 7 Days")
st.dataframe(predictions)

st.subheader("Recommended Actions")
if not recommendations.empty:
    st.dataframe(recommendations)
else:
    st.warning("No recommended actions for the next 7 days.")
