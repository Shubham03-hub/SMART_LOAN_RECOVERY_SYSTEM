import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/LOAN_DATAS.csv")

st.title("Smart Loan Recovery System")

st.subheader("Dataset Preview")
st.write(df.head())

st.metric("Total Loans", len(df))

st.subheader("Default Distribution")

fig, ax = plt.subplots()
sns.countplot(x="default", data=df, ax=ax)
st.pyplot(fig)