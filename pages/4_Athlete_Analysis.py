import streamlit as st
from utils.loader import load_data
from utils.charts import *
from utils.sidebar import sidebar_filters

st.set_page_config(
    page_title="Athlete Analysis",
    page_icon="👤",
    layout="wide"
)

athletes, medal_df = load_data()
year, sport, country, gender = sidebar_filters(athletes)

st.title("👤 Athlete Analysis")

athlete_list = sorted(
    athletes["Name"].dropna().unique().tolist()
)

selected = st.selectbox(
    "Search Athlete",
    athlete_list
)

summary = athlete_summary(
    athletes,
    selected
)

st.divider()

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("🌍 Country", summary["Country"])

with c2:
    st.metric("🏃 Sports", summary["Sports"])

with c3:
    st.metric("📅 Olympics", summary["Olympics"])

with c4:
    st.metric("🏅 Total Medals", summary["Total"])

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("🥇 Gold", summary["Gold"])

with c2:
    st.metric("🥈 Silver", summary["Silver"])

with c3:
    st.metric("🥉 Bronze", summary["Bronze"])

st.divider()

st.plotly_chart(
    athlete_medal_timeline(
        medal_df,
        selected
    ),
    use_container_width=True
)

st.divider()

st.subheader("Olympic Participation History")

st.dataframe(
    athlete_history(
        athletes,
        selected
    ),
    use_container_width=True,
    hide_index=True
)