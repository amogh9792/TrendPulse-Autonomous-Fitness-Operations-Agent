````markdown
# TrendPulse: Autonomous Fitness Operations AI

**TrendPulse** is an **agentic AI system** designed to help fitness companies make data-driven operational decisions. It predicts product demand, generates actionable recommendations, and provides a real-time dashboard — all using **Python, modular code, and open-source tools**.  

This project is demo-ready and showcases AI capabilities in supply chain, operations, and analytics.

---

## Features

- **Demand Prediction**  
  Predicts next 7 days’ product demand using historical sales and trend data.  

- **Actionable Recommendations**  
  Suggests reorders automatically when predicted demand exceeds a threshold.  

- **Interactive Dashboard**  
  Built with Streamlit to visualize predicted demand and recommended actions.  

- **Fully Modular**  
  - `utils/`: Data cleaning & preprocessing  
  - `agents/`: Demand prediction, recommendations, alerts  
  - `run_trendpulse.py`: Main workflow  
  - `dashboard/app.py`: Streamlit dashboard  

- **Demo-Ready**  
  Generates **synthetic but realistic sales and trend data** (300+ records)  
  Ensures **non-empty recommendations** for presentation purposes.  

---

## Installation

1. Clone the repository:

```bash
git clone <repo-url>
cd TrendPulse
````

2. Create a virtual environment (recommended):

```bash
python -m venv trendpulse_venv
source trendpulse_venv/bin/activate   # Linux/Mac
trendpulse_venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install pandas numpy scikit-learn streamlit
```

---

## How to Run

### 1️⃣ Generate Predictions & Recommendations

```bash
python run_trendpulse.py
```

* Generates **synthetic sales and trends data**.
* Trains a **Random Forest demand prediction model**.
* Predicts next 7 days’ demand.
* Generates **recommended actions** (reorder alerts).
* Saves CSV files in `data/processed/`.

### 2️⃣ Launch the Dashboard

```bash
streamlit run dashboard/app.py
```

* Interactive dashboard displays:

  * Predicted demand per city/product
  * Recommended actions for inventory management
* Console also prints actionable alerts for quick demo recording.

---

## Key Notes

* **Threshold for recommendations**: `predicted_units >= 40` (adjustable in `action_recommender.py`)
* **Trend boost**: `trend_score * 1.2` ensures visible recommendations for demo.
* **No scraping or paid API required** — uses synthetic, realistic data.
* **Modular design** makes it easy to extend:

  * Connect real sales/trend databases
  * Replace RandomForest with more advanced models
  * Add more analytics agents


## License

Open-source for demo and educational purposes.


