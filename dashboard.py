
import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("sa3_investment_data_from_excel.csv")

# Branding Header
st.markdown("""
    <div style='text-align: center; padding: 10px;'>
        <h1 style='color: #2E86C1; font-size: 48px;'>PropwealthNext</h1>
        <h4 style='color: #555;'>Regional Investment Intelligence Dashboard</h4>
    </div>
""", unsafe_allow_html=True)

# Sidebar
selected_sa3 = st.sidebar.selectbox("📍 Select an SA3 Region", df["SA3"].unique())
sa3 = df[df["SA3"] == selected_sa3].iloc[0]

# KPIs Display
st.subheader(f"📊 Key Metrics for {sa3['SA3']} ({sa3['Sa4']})")

col1, col2, col3 = st.columns(3)
col1.metric("💰 Median Price", f"${int(sa3['Median']):,}")
col2.metric("📈 12M Price Growth", f"{sa3['12M Price Change']}%")
col3.metric("💸 Yield", f"{float(sa3['YIELD']) * 100:.2f}%")

col4, col5, col6 = st.columns(3)
col4.metric("📊 Rent Change", f"{float(sa3['RENT CHANGE']) * 100:.1f}%")
col5.metric("🧮 Buy Affordability", f"{sa3['Buy Affordability']} yrs")
col6.metric("📉 Rent Affordability", f"{float(sa3['Rent Afford']) * 100:.1f}%")

st.metric("📈 10Y Growth (PA)", f"{sa3['10 Year % Price Change (PA)']}%")

# Map placeholder
st.info("🗺 Map view can be enabled once latitude/longitude columns are added.")

# Download CSV
csv = df.to_csv(index=False)
st.download_button("📥 Download Full Dataset", csv, "sa3_investment_data.csv", "text/csv")
