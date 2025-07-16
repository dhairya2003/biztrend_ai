import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.summary import generate_summary
from utils.charts import plot_monthly_sales

st.set_page_config(page_title="BizTrend AI", layout="wide")
st.title("📊 BizTrend AI - SMB Dashboard")

uploaded_file = st.file_uploader("Upload your sales CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("File uploaded successfully!")

    st.subheader("📌 Summary")
    summary = generate_summary(df)
    st.json(summary)

    st.subheader("📈 Monthly Sales Chart")
    fig = plot_monthly_sales(df)
    st.pyplot(fig)
