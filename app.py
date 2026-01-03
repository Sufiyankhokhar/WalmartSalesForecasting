import streamlit as st
import pandas as pd
import joblib

model  = joblib.load("Walmart_sales_model.pkl")

st.set_page_config(page_title="Walmart Sales Forecast", layout = "centered")
st.title("Walmart Weekly Sales Prediction")

store = st.number_input("Store Number", 1, 45)
holiday = st.selectbox("Holiday Week?", [0, 1])
temp = st.slider("Temperature", -10.0, 100.0, 50.0)
fuel = st.slider("Fuel Price", 2.0, 5.0, 3.0)
cpi = st.slider("CPI", 120.0, 250.0, 180.0)
unemp = st.slider("Unemploymennt", 3.0, 15.0, 7.0)
year = st.number_input("Year", 2010, 2025)
month = st.slider("Month", 1, 12)
week = st.slider("Week", 1, 52)

input_data  = pd.DataFrame([[store, holiday, temp, fuel, cpi, unemp, year, month, week]], columns=['Store', 'Holiday_Flag', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment', 'Year', 'Month', 'Week'])

if st.button("Predict Sales"):
    prediction = model.predict(input_data)
    st.success(f"Predict Weekly Sales: ${prediction[0]:,.2f}")