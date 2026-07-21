import streamlit as st
from utils.loader import load_data
from utils.helper import *
from utils.charts import *
from utils.sidebar import sidebar_filters



st.set_page_config(
    page_title="Overall Analysis",
    page_icon="📊",
    layout="wide"
)

# Load data
athletes, medal_df = load_data()

year, sport, country, gender = sidebar_filters(athletes)

st.title("📊 Overall Olympic Analysis")

st.markdown(
"""
Explore the complete Olympic dataset and analyze participation,
countries, sports, athletes and overall Olympic trends.
"""
)

st.divider()



c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("👤 Athletes", f"{total_athletes(athletes):,}")

with c2:
    st.metric("🌍 Countries", total_countries(athletes))

with c3:
    st.metric("🏅 Sports", total_sports(athletes))

with c4:
    st.metric("🎯 Events", total_events(athletes))

st.divider()



st.subheader("📈 Athlete Participation Over Time")

st.plotly_chart(
    participation_trend(athletes),
    use_container_width=True
)

st.divider()



st.subheader("🌍 Top Countries by Medal Count")

st.plotly_chart(
    top_countries(medal_df),
    use_container_width=True
)

st.divider()


st.subheader("🥇 Medal Distribution")

st.plotly_chart(
    medal_distribution(medal_df),
    use_container_width=True
)

st.divider()



st.subheader("📄 Dataset Preview")

st.dataframe(
    athletes.head(100),
    use_container_width=True,
    hide_index=True
)