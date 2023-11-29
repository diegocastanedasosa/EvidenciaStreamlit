import pandas as pd
import streamlit as st

st.markdown("Ventas junio 2023")

chart_data = pd.read_csv("datos .csv")
st.line_chart(chart_data)