import streamlit as st
import pandas as pd
import joblib

# Load model and feature list
model = joblib.load('../stock_price_prediction/models/linear_model.pkl')
features = joblib.load('../stock_price_prediction/models/features_list.pkl')

# Load cleaned dataset
#df = pd.read_csv('C:/Users/palre/Desktop/Interview_prep/personal-projects/Data-Science-Project/stock_price_prediction/data/processed/tesla_stock_cleaned.csv')  # or use your real path
df = pd.read_csv('../data/processed/tesla_processed.csv')

# Get the most recent row (last available day)
latest_row = df[features].iloc[-1]

# Title and subtitle
st.title("📈 Tesla Stock Price Predictor")
st.markdown("Enter the most recent values to predict the next day's **closing price**.")

# Input form
user_input = {}
for feature in features:
    user_input[feature] = st.number_input(
        label=f"{feature}",
        value=float(latest_row[feature]),
        step=0.1,
        format="%.4f"
    )

# Convert to DataFrame
input_df = pd.DataFrame([user_input])

# Predict
if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    st.success(f"📊 Predicted Close Price: **${prediction:.2f}**")


st.markdown("---")
st.header("📉 Actual vs Predicted Close Prices")

# Load prediction results
df_results = pd.read_csv('../data/processed/predictions.csv', parse_dates=['Date'])

# Plot using matplotlib
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df_results['Date'], df_results['Close'], label='Actual')
ax.plot(df_results['Date'], df_results['Predicted_Close'], label='Predicted')
ax.set_title("Actual vs Predicted Tesla Close Prices")
ax.set_xlabel("Date")
ax.set_ylabel("Close Price ($)")
ax.legend()
st.pyplot(fig)
