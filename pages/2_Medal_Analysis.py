import streamlit as st
from utils.loader import load_data
from utils.charts import *
from utils.sidebar import sidebar_filters

st.set_page_config(
    page_title="Medal Analysis",
    page_icon="🥇",
    layout="wide"
)

athletes, medal_df = load_data()
year, sport, country, gender = sidebar_filters(athletes)

st.title("🥇 Medal Analysis")

st.markdown(
"""
Analyze Olympic medals using interactive filters and visualizations.
"""
)

st.divider()



col1, col2 = st.columns(2)

years = ["All"] + sorted(
    medal_df["Year"].unique().tolist()
)

countries = ["All"] + sorted(
    medal_df["Region"].dropna().unique().tolist()
)

with col1:
    selected_year = st.selectbox(
        "Olympic Year",
        years
    )

with col2:
    selected_country = st.selectbox(
        "Country",
        countries
    )

filtered = medal_df.copy()

if selected_year != "All":
    filtered = filtered[
        filtered["Year"] == selected_year
    ]

if selected_country != "All":
    filtered = filtered[
        filtered["Region"] == selected_country
    ]

st.divider()

# Medal Table

st.subheader("🏆 Medal Table")

table = (
    filtered.groupby("Region")["Medal"]
    .count()
    .sort_values(ascending=False)
    .reset_index()
)

table.columns = ["Country", "Total Medals"]

st.dataframe(
    table,
    use_container_width=True,
    hide_index=True
)

st.divider()

left, right = st.columns(2)

with left:
    st.plotly_chart(
        medal_distribution(filtered),
        use_container_width=True
    )

with right:
    st.plotly_chart(
        top_countries(filtered),
        use_container_width=True
    )

st.divider()

st.subheader("📈 Medal Trend")

st.plotly_chart(
    medal_trend(filtered),
    use_container_width=True
)