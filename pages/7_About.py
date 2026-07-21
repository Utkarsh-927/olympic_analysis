import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("🏅 Olympic Analytics Dashboard")

st.markdown("""
## 📌 Project Overview

This dashboard provides an interactive analysis of Olympic Games data from 1896 to 2016.

Users can explore athletes, countries, sports, events and medal trends using interactive charts and filters.

---

## 🚀 Technologies Used

- Python
- Pandas
- Plotly
- Streamlit

---

## 📊 Features

- Overall Olympic Analysis
- Medal Analysis
- Country Analysis
- Athlete Analysis
- Sports Analysis
- Dataset Explorer

---

## 📂 Dataset

Olympic History Dataset

Source:
https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results

---

## 👨‍💻 Analysis By

Utkarsh Singh

B.Tech CSE (AI)

University of Lucknow
""")