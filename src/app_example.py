from datetime import datetime
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("tests/data/Activities.csv")
max_heart_rate = st.number_input("Insert your Max HR")

df_filtered = df[["Activity Type", "Date", "Distance", "Avg HR"]]
df_filtered["heart_rate_percentage"] = (df_filtered["Avg HR"] / max_heart_rate) * 100


st.dataframe(
    df_filtered,
    column_config={
        "Date": st.column_config.DatetimeColumn(
            "Date time",
            min_value=datetime(2024, 1, 1),
            max_value=datetime(2025, 1, 1),
            format="D MMM YYYY, h:mm a",
            step=60,
        ),
        "Activity Type": "Activity",
        "Distance": st.column_config.NumberColumn(
            "Distance",
            help="Number of km in this activity",
            format="%f 📏",
        ),
        "Avg HR": st.column_config.LineChartColumn("Average HR", y_min=0, y_max=200),
        "heart_rate_percentage": st.column_config.NumberColumn(
            "HR percentage",
            help="Percentage of avg HR rate with maximum HR",
            format="%.2f ❤️",
        ),
    },
)

fig1, ax1 = plt.subplots(1, 1)
ax1.bar(df_filtered["Activity Type"], df_filtered.Distance)
st.pyplot(fig1)

fig2, ax2 = plt.subplots(1, 1)
ax2.hist(
    df_filtered.heart_rate_percentage,
    bins=[70, 75, 86, 88, 98, 100, 101],
    orientation="horizontal",
    rwidth=0.99,
)
st.pyplot(fig2)
