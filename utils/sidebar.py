import streamlit as st

def sidebar_filters(df):

    st.sidebar.header("🔍 Filters")

    year = st.sidebar.selectbox(
        "Year",
        ["All"] + sorted(df["Year"].unique().tolist())
    )

    sport = st.sidebar.selectbox(
        "Sport",
        ["All"] + sorted(df["Sport"].dropna().unique().tolist())
    )

    country = st.sidebar.selectbox(
        "Country",
        ["All"] + sorted(df["Region"].dropna().unique().tolist())
    )

    gender = st.sidebar.selectbox(
        "Gender",
        ["All"] + sorted(df["Gender"].dropna().unique().tolist())
    )

    return year, sport, country, gender