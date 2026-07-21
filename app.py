import streamlit as st

from utils.loader import load_data
from utils.helper import *
from utils.charts import *
from utils.sidebar import sidebar_filters

st.set_page_config(
    page_title="Olympic Analytics Dashboard",
    page_icon="🏅",
    layout="wide"
)


def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True,
        )


load_css()
athletes, medal_df = load_data()

year, sport, country, gender = sidebar_filters(athletes)


st.sidebar.header("Filters")

filtered = athletes.copy()
filtered_medals = medal_df.copy()

if year != "All":
    filtered = filtered[filtered["Year"] == year]
    filtered_medals = filtered_medals[filtered_medals["Year"] == year]

if sport != "All":
    filtered = filtered[filtered["Sport"] == sport]
    filtered_medals = filtered_medals[filtered_medals["Sport"] == sport]

if gender != "All":
    filtered = filtered[filtered["Gender"] == gender]

if country != "All":
    filtered = filtered[filtered["Region"] == country]
    filtered_medals = filtered_medals[filtered_medals["Region"] == country]

st.title("🏅 Olympic Analytics Dashboard")

st.markdown(
"""
### Explore more than 120 years of Olympic history.

Analyze athletes, countries, sports, medals and participation through interactive visualizations.
"""
)

st.divider()

c1, c2, c3 = st.columns(3)

c4, c5, c6 = st.columns(3)

with c1:
    st.metric("👤 Athletes", f"{total_athletes(filtered):,}")

with c2:
    st.metric("🌍 Countries", total_countries(filtered))

with c3:
    st.metric("🏅 Sports", total_sports(filtered))

with c4:
    st.metric("🎯 Events", total_events(filtered))

with c5:
    st.metric("📅 Olympic Games", total_games(filtered))

with c6:
    st.metric("🥇 Medals", f"{total_medals(filtered_medals):,}")

st.divider()

st.subheader("Dataset Preview")

st.dataframe(
    filtered,
    use_container_width=True,
    hide_index=True
)
st.divider()

left, right = st.columns(2)

with left:
    st.plotly_chart(
        participation_trend(filtered),
        use_container_width=True
    )

with right:
    st.plotly_chart(
        medal_distribution(filtered_medals),
        use_container_width=True
    )

st.divider()

st.plotly_chart(
    top_countries(filtered_medals),
    use_container_width=True
)
st.divider()

left, right = st.columns(2)

with left:
    st.plotly_chart(
        top_sports(filtered),
        use_container_width=True
    )

with right:
    st.plotly_chart(
        gender_distribution(filtered),
        use_container_width=True
    )

st.divider()

left, right = st.columns(2)

with left:
    st.plotly_chart(
        top_events(filtered),
        use_container_width=True
    )

with right:
    st.plotly_chart(
        age_distribution(filtered),
        use_container_width=True
    )

st.divider()

st.plotly_chart(
    medal_trend(filtered_medals),
    use_container_width=True
)
st.divider()

st.subheader("🌍 Country Performance Analysis")

left, right = st.columns(2)

with left:
    st.plotly_chart(
        top_countries_by_athletes(filtered),
        use_container_width=True
    )

with right:
    st.dataframe(
        medal_table(filtered_medals),
        use_container_width=True,
        hide_index=True
    )
st.divider()

st.subheader("👤 Athlete Analysis")

left, right = st.columns(2)

with left:
    st.plotly_chart(
        top_athletes(filtered),
        use_container_width=True
    )

with right:
    st.plotly_chart(
        average_age_by_sport(filtered),
        use_container_width=True
    )

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("🏅 Youngest Medal Winners")
    st.dataframe(
        youngest_medalists(filtered),
        use_container_width=True,
        hide_index=True
    )

with right:
    st.subheader("🏆 Oldest Medal Winners")
    st.dataframe(
        oldest_medalists(filtered),
        use_container_width=True,
        hide_index=True
    )    
st.divider()

st.subheader("🥇 Country-wise Medal Table")

medals = country_medal_breakdown(filtered_medals)

st.dataframe(
    medals,
    use_container_width=True,
    hide_index=True
) 
st.divider()

st.subheader("🥇 Country-wise Medal Table")

medals = country_medal_breakdown(filtered_medals)

selected_country = st.selectbox(
    "Select Country",
    ["All"] + sorted(medals["Region"].dropna().unique().tolist())
)

if selected_country != "All":
    medals = medals[
        medals["Region"] == selected_country
    ]

st.dataframe(
    medals,
    use_container_width=True,
    hide_index=True
) 
st.divider()

st.subheader("📈 Country Performance Over Time")

country_list = sorted(
    medal_df["Region"].dropna().unique().tolist()
)

selected_country = st.selectbox(
    "Choose a Country",
    country_list,
    key="country_trend"
)

st.plotly_chart(
    country_medal_trend(filtered_medals, selected_country),
    use_container_width=True
)  
st.divider()

st.subheader("⚔️ Country Comparison")

countries = sorted(
    filtered_medals["Region"].dropna().unique().tolist()
)

col1, col2 = st.columns(2)
if len(countries) < 2:
    st.warning("At least two countries are required for comparison.")
else:
    with col1:
       country1 = st.selectbox(
          "Country 1",
           countries,
             key="compare_country1"
        )

    with col2:
        country2 = st.selectbox(
            "Country 2",
             countries,
            index=1,
            key="compare_country2"
        )



comparison = compare_countries(
    filtered_medals,
    country1,
    country2
)

st.dataframe(
    comparison,
    use_container_width=True,
    hide_index=True
)
comparison_chart = comparison.melt(
    id_vars="Region",
    var_name="Metric",
    value_name="Value"
)

fig = px.bar(
    comparison_chart,
    x="Metric",
    y="Value",
    color="Region",
    barmode="group",
    title="Country Comparison"
)

st.plotly_chart(
    fig,
    use_container_width=True
)