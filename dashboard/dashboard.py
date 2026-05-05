import streamlit as st
import pandas as pd
import time
import os
st.set_page_config(page_title="Motor Monitoring", layout="wide")
CSV_FILE = "data_log.csv"
st.title("⚙ Motor Fault Detection Dashboard")
# placeholders
metric_placeholder = st.empty()
chart_placeholder = st.empty()
table_placeholder = st.empty()
def load_data():
if not os.path.exists(CSV_FILE):
return None
try:
df = pd.read_csv(CSV_FILE)
return df
except:
return None
while True:
df = load_data()
if df is None or df.empty:
st.warning("Waiting for data...")
time.sleep(1)
st.rerun()
latest = df.iloc[-1]
current = latest["Current"]
temp = latest["Temp"]
vib = latest["Vibration"]
state = str(latest["State"]).lower()
# -----------------------
# METRICS
# -----------------------
with metric_placeholder.container():
col1, col2, col3, col4 = st.columns(4)
col1.metric("Current (A)", f"{current:.2f}")
col2.metric("Temperature (°C)", f"{temp:.2f}")
col3.metric("Vibration", f"{vib:.2f}")
if state == "jam":
col4.metric("State", "JAM 🚨")
st.error("⚠ JAM DETECTED - Motor OFF")
else:
col4.metric("State", "NORMAL ✅")
# -----------------------
# CHARTS
# -----------------------
with chart_placeholder.container():
st.subheader("Sensor Graphs")
df_small = df.tail(50)
st.line_chart(df_small[["Current"]], height=200)
st.line_chart(df_small[["Vibration"]], height=200)
st.line_chart(df_small[["Temp"]], height=200)
# -----------------------
# TABLE
# -----------------------
with table_placeholder.container():
st.subheader("Last Readings")
st.dataframe(df.tail(10), width="stretch")
time.sleep(1)
st.rerun()