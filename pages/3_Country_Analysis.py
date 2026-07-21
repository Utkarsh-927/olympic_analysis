import streamlit as st
from utils.loader import load_data
from utils.charts import *
from utils.sidebar import sidebar_filters

st.set_page_config(
    page_title="Country Analysis",
    page_icon="🌍",
    layout="wide"
)

athletes, medal_df = load_data()
year, sport, country, gender = sidebar_filters(athletes)

st.title("🌍 Country Analysis")

countries = sorted(
    medal_df["Region"].dropna().unique().tolist()
)

country = st.selectbox(
    "Select Country",
    countries
)

st.divider()

# Medal Statistics

temp = medal_df[medal_df["Region"] == country]

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("🥇 Gold", (temp["Medal"] == "Gold").sum())

with c2:
    st.metric("🥈 Silver", (temp["Medal"] == "Silver").sum())

with c3:
    st.metric("🥉 Bronze", (temp["Medal"] == "Bronze").sum())

with c4:
    st.metric("🏅 Total", temp.shape[0])

st.divider()

st.plotly_chart(
    country_medal_timeline(
        medal_df,
        country
    ),
    use_container_width=True
)

st.divider()

st.plotly_chart(
    country_top_sports(
        medal_df,
        country
    ),
    use_container_width=True
)

st.divider()

st.subheader("🏆 Top Athletes")

st.dataframe(
    country_top_athletes(
        medal_df,
        country
    ),
    use_container_width=True,
    hide_index=True
)