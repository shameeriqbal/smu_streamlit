import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("titles.csv")

year = st.slider("year", 1894, 2022, (1894, 2022))
title = st.text_input("title")
if title:
    df = df[df.title == title]
df = df[(df.year >= year[0]) & (df.year<=year[1])]

st.write(df)

fig, ax = plt.subplots()

df["decade"] = df.year//10 * 10
df["decade"].value_counts().sort_index().plot(kind='bar')

st.pyplot(fig)
