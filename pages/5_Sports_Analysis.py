import streamlit as st
from utils.loader import load_data
from utils.charts import *
from utils.sidebar import sidebar_filters

st.set_page_config(
    page_title="Sports Analysis",
    page_icon="🏆",
    layout="wide"
)

athletes, medal_df = load_data()
year, sport, country, gender = sidebar_filters(athletes)

st.title("🏆 Sports Analysis")

sports = sorted(
    athletes["Sport"].dropna().unique().tolist()
)

selected_sport = st.selectbox(
    "Select Sport",
    sports
)

st.divider()

# KPIs

temp = athletes[
    athletes["Sport"] == selected_sport
]

medal_temp = medal_df[
    medal_df["Sport"] == selected_sport
]

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "👤 Athletes",
        temp["Name"].nunique()
    )

with c2:
    st.metric(
        "🌍 Countries",
        temp["Region"].nunique()
    )

with c3:
    st.metric(
        "🎯 Events",
        temp["Event"].nunique()
    )

with c4:
    st.metric(
        "🥇 Medals",
        medal_temp.shape[0]
    )

st.divider()

st.plotly_chart(
    sport_participation(
        athletes,
        selected_sport
    ),
    use_container_width=True
)

st.divider()

st.plotly_chart(
    sport_top_countries(
        medal_df,
        selected_sport
    ),
    use_container_width=True
)

st.divider()

st.subheader("🏅 Top Athletes")

st.dataframe(
    sport_top_athletes(
        medal_df,
        selected_sport
    ),
    use_container_width=True,
    hide_index=True
)

st.divider()

st.subheader("🎯 Events")

events = sport_events(
    athletes,
    selected_sport
)

st.dataframe(
    events.to_frame(name="Event"),
    use_container_width=True,
    hide_index=True
)