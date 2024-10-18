import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("tests/data/Activities.csv")

fig, ax = plt.subplots(1, 1)
ax.scatter(df.Date, df.Distance)

st.pyplot(fig)