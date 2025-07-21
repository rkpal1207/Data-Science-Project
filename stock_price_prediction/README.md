# 📈 Tesla Stock Price Predictor

A data science project that predicts the next-day closing price of Tesla stock using machine learning and also performs time series forecasting using Facebook Prophet.

---

## 🗂️ Project Structure

```
.
├── data/
│   └── processed/               # Cleaned dataset and forecast (tesla_stock_cleaned.csv, prophet_forecast.csv)
├── models/                      # Trained models (linear_model.pkl, feature_list.pkl)
├── notebooks/
│   ├── data_cleaning.ipynb      # Data cleaning steps
│   ├── eda.ipynb                # Exploratory Data Analysis
│   ├── data_modeling.ipynb      # Feature engineering and ML modeling
│   └── forecasting_prophet.ipynb# Prophet forecasting notebook
├── scripts/
│   └── streamlit_app.py         # Streamlit web app
├── requirements.txt
└── README.md
```

---

## 📌 Objective

Build a beginner-friendly, real-world stock prediction project that:
- Predicts Tesla’s **next-day closing price**
- Visualizes **actual vs predicted prices**
- Forecasts future prices using **Prophet**
- Deploys a clean and interactive **Streamlit app**

---

## 📊 Dataset

- Source: [Kaggle Tesla Stock Dataset](https://www.kaggle.com/datasets/timoboz/tesla-stock-data)
- Timeframe: ~2010 to 2024
- Original columns: `Open`, `High`, `Low`, `Close`, `Volume`
- Engineered features:
  - `lag_1`, `lag_2`, `lag_3` — Previous day prices
  - `sma_10` — 10-day simple moving average
  - `daily_return` — % return since previous close

---

## 🔍 Exploratory Data Analysis (EDA)

- Visualized price trends, volatility, and moving averages
- Correlation analysis and heatmaps
- Insight into periods of rapid price movement (e.g., COVID boom)

---

## ⚙️ Feature Engineering

To prepare the dataset for supervised learning:

- Lag features: `lag_1`, `lag_2`, `lag_3`
- Moving average: `sma_10`
- Percentage change: `daily_return`
- Handled nulls caused by rolling and shifting
- Saved clean dataset to `tesla_processed.csv`

---

## 🤖 Modeling

Trained and evaluated multiple regression models:

| Model               | RMSE   | R² Score |
|--------------------|--------|----------|
| Linear Regression   | 7.88   | 0.9833   |
| Gradient Boosting   | 25.08  | 0.8313   |
| Random Forest       | 26.45  | 0.8124   |

**✅ Final model used:** Linear Regression  
Exported with `joblib` for use in Streamlit.

---

## 🌐 Streamlit Web App

Interactive interface to:
- Input lag/technical values
- Predict next-day close price
- Visualize actual vs predicted prices

### Run the app locally:
```bash
streamlit run scripts/streamlit_app.py
```

---

## 🔮 Forecasting Future Prices (with Prophet)

Performed long-term time series forecasting using **Facebook Prophet**.

### Key Info:
- Forecast horizon: **90 days**
- Input: Cleaned Tesla stock history
- Output: `prophet_forecast.csv` with `yhat`, `yhat_lower`, `yhat_upper`
- Used in a standalone notebook (`forecasting_prophet.ipynb`)

📌 Forecasting results are not part of the Streamlit UI but are available for reference and future analysis.

---

## 📦 Setup Instructions

1. Clone this repo:
```bash
git clone https://github.com/your-username/tesla-stock-predictor.git
cd tesla-stock-predictor
```

2. (Optional) Create a virtual environment:
```bash
conda create -n stock-predictor python=3.9
conda activate stock-predictor
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Launch the app:
```bash
streamlit run scripts/streamlit_app.py
```

---

## 💼 Skills Demonstrated

| Area                     | Description                                           |
|--------------------------|-------------------------------------------------------|
| 🧹 Data Cleaning         | Removing missing values, formatting dates, renaming   |
| 📊 EDA                  | Trends, seasonality, correlation                      |
| 🧠 Feature Engineering   | Lags, SMA, daily return                               |
| 🤖 Modeling              | Regression models with evaluation                    |
| 🔮 Time Series Forecast  | Prophet-based multi-day forecast                     |
| 🖼️ Visualization         | Matplotlib, Streamlit charts                         |
| 🖥️ Web App               | User interaction with Streamlit                     |
| 📄 Documentation         | Well-structured README and project organization      |

---

