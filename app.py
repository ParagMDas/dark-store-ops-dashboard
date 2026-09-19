import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dark Store Ops & SLA Tracker", layout="wide")

st.title("📦 Quick-Commerce Ops & Inventory Reconciliation Engine")
st.caption("Built for Dark Store Hub Managers & Logistics Team Leads")

# Sidebar - Hub Configuration
st.sidebar.header("Hub Configuration")
hub_name = st.sidebar.selectbox("Select Hub Location", ["Geetanagar Hub", "Bijaynagar Sorting Center", "Dhupdhara Hub"])
total_riders = st.sidebar.slider("Active Riders/Wishmasters", 5, 50, 20)

# Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric(label="On-Time Delivery Rate", value="99.2%", delta="0.4%")
col2.metric(label="Rider Attrition Rate", value="12%", delta="-3%")
col3.metric(label="Stock Discrepancy", value="1.4%", delta="-0.6%")
col4.metric(label="Avg Pick/Pack Time", value="2.4 mins", delta="-0.3 mins")

st.divider()

# COD Reconciliation Section
st.subheader("💰 Rider Daily COD Cash Reconciliation")
rider_data = {
    "Rider ID": [f"WM-{100+i}" for i in range(1, 6)],
    "Assigned Orders": [25, 30, 22, 28, 35],
    "System Expected COD (₹)": [4500, 6200, 3100, 5400, 8000],
    "Cash Collected (₹)": [4500, 6200, 2900, 5400, 8000]
}

df_cod = pd.DataFrame(rider_data)
df_cod["Discrepancy (₹)"] = df_cod["Cash Collected (₹)"] - df_cod["System Expected COD (₹)"]
df_cod["Status"] = df_cod["Discrepancy (₹)"].apply(lambda x: "MATCHED ✅" if x == 0 else "SHORTAGE 🚨")

st.dataframe(df_cod, use_container_width=True)

st.divider()

# Hourly Dispatch Chart
st.subheader("📈 Hourly Order Dispatch Trend vs. Target SLA")
chart_data = pd.DataFrame({
    "Hour": [f"{h}:00" for h in range(8, 20)],
    "Target Orders": [40, 60, 80, 100, 120, 110, 90, 80, 100, 130, 110, 70],
    "Actual Dispatched": [38, 58, 82, 98, 115, 112, 88, 81, 102, 125, 108, 69]
}).set_index("Hour")

st.line_chart(chart_data)
