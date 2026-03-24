# -----------------Expense_Dashboard-----------------:


import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("💰 Smart Expense Dashboard")

# Load Data
data = pd.read_csv("expense.csv")

# Convert Date
data['Date'] = pd.to_datetime(data['Date'])
data['Month'] = data['Date'].dt.month_name()

# Sidebar Filter
st.sidebar.header("Filter Options")
selected_type = st.sidebar.selectbox("Select Type", data['Type'].unique())

filtered_data = data[data['Type'] == selected_type]

st.divider()

# 🔹 Total Amount
total = filtered_data['Amount'].sum()
st.metric(f"Total {selected_type}", f"₹ {total}")

st.divider()

# 🔹 Category Analysis
st.subheader("📊 Category Analysis")

category = filtered_data.groupby('Category')['Amount'].sum()
st.bar_chart(category)

st.divider()

# 🔹 Monthly Analysis
st.subheader("📈 Monthly Trend")

monthly = filtered_data.groupby('Month')['Amount'].sum()

# Sort months correctly
month_order = [
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
]

monthly = monthly.reindex(month_order).dropna()

# Highest & Lowest Month
highest_month = monthly.idxmax()
highest_amount = monthly.max()

lowest_month = monthly.idxmin()
lowest_amount = monthly.min()

col1, col2 = st.columns(2)

col1.metric("Highest Month", f"{highest_month} (₹ {highest_amount})")
col2.metric("Lowest Month", f"{lowest_month} (₹ {lowest_amount})")

st.line_chart(monthly)