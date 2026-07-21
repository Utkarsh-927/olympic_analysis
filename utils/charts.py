import plotly.express as px


def participation_trend(df):

    yearly = (
        df.groupby("Year")["Name"]
        .nunique()
        .reset_index(name="Athletes")
    )

    fig = px.line(
        yearly,
        x="Year",
        y="Athletes",
        markers=True,
        title="Athlete Participation Over Time"
    )

    return fig


def medal_distribution(df):

    medals = (
        df["Medal"]
        .dropna()
        .value_counts()
        .reset_index()
    )

    medals.columns = ["Medal", "Count"]

    return px.pie(
        medals,
        names="Medal",
        values="Count",
        hole=.45,
        title="Medal Distribution"
    )


def top_countries(df):

    countries = (
        df.groupby("Region")["Medal"]
        .count()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        countries,
        x="Region",
        y="Medal",
        text_auto=True,
        title="Top 10 Countries by Medals"
    )

    fig.update_layout(
        template="plotly_white",
        height=500
    )

    return fig

def top_sports(df):

    sports = (
        df.groupby("Sport")["Name"]
        .nunique()
        .sort_values(ascending=False)
        .head(10)
        .reset_index(name="Athletes")
    )

    fig = px.bar(
        sports,
        x="Athletes",
        y="Sport",
        orientation="h",
        title="Top 10 Sports by Athlete Participation",
        text="Athletes"
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending"),
        template="plotly_white",
        height=500
    )

    return fig

def top_events(df):

    events = (
        df.groupby("Event")["Name"]
        .nunique()
        .sort_values(ascending=False)
        .head(10)
        .reset_index(name="Athletes")
    )

    fig = px.bar(
        events,
        x="Event",
        y="Athletes",
        title="Top 10 Olympic Events",
        text="Athletes"
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_tickangle=-35,
        height=500
    )

    return fig

def gender_distribution(df):

    gender = (
        df["Gender"]
        .value_counts()
        .reset_index()
    )

    gender.columns = ["Gender", "Count"]

    fig = px.pie(
        gender,
        names="Gender",
        values="Count",
        hole=0.45,
        title="Gender Distribution"
    )

    fig.update_layout(
        template="plotly_white",
        height=450
    )

    return fig

def age_distribution(df):

    age_df = df[df["Age"].notna()]

    fig = px.histogram(
        age_df,
        x="Age",
        nbins=25,
        title="Age Distribution of Athletes"
    )

    fig.update_layout(
        template="plotly_white",
        height=450
    )

    return fig

def top_countries_by_athletes(df):

    countries = (
        df.groupby("Region")["Name"]
        .nunique()
        .sort_values(ascending=False)
        .head(10)
        .reset_index(name="Athletes")
    )
    fig = px.bar(
        countries,
        x="Region",
        y="Athletes",
        text="Athletes",
        title="Top 10 Countries by Athlete Participation"
    )

    fig.update_layout(
        template="plotly_white",
        height=450,
        xaxis_tickangle=-30
    )

    return fig

def medal_table(df):

    medals = (
        df[df["Medal"].notna()]
        .groupby(["Region", "Medal"])
        .size()
        .unstack(fill_value=0)
    )

    
    for medal in ["Gold", "Silver", "Bronze"]:
        if medal not in medals.columns:
            medals[medal] = 0

    medals["Total"] = (
        medals["Gold"] +
        medals["Silver"] +
        medals["Bronze"]
    )

    medals = (
        medals.sort_values("Total", ascending=False)
        .head(15)
        .reset_index()
    )

    return medals
def top_athletes(df):

    athletes = (
        df[df["Medal"].notna()]
        .groupby("Name")
        .size()
        .reset_index(name="Medals")
        .sort_values("Medals", ascending=False)
        .head(10)
    )

    fig = px.bar(
        athletes,
        x="Name",
        y="Medals",
        text="Medals",
        title="Top 10 Athletes by Medals"
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_tickangle=-35,
        height=450
    )

    return fig

def average_age_by_sport(df):

    age = (
        df[df["Age"].notna()]
        .groupby("Sport")["Age"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        age,
        x="Sport",
        y="Age",
        title="Average Athlete Age by Sport",
        text_auto=True
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_tickangle=-35,
        height=450
    )

    return fig
def youngest_medalists(df):

    youngest = (
        df[df["Medal"].notna()]
        .sort_values("Age")
        .head(10)
    )

    return youngest[
        ["Name", "Age", "Sport", "Region", "Year", "Medal"]
    ]
def oldest_medalists(df):

    oldest = (
        df[df["Medal"].notna()]
        .sort_values("Age", ascending=False)
        .head(10)
    )

    return oldest[
        ["Name", "Age", "Sport", "Region", "Year", "Medal"]
    ]        
def country_medal_breakdown(df):

    medal_df = df[df["Medal"].notna()]

    medal_table = (
        medal_df.groupby(["Region", "Medal"])
        .size()
        .unstack(fill_value=0)
    )

    # Ensure all medal columns exists
    for medal in ["Gold", "Silver", "Bronze"]:
        if medal not in medal_table.columns:
            medal_table[medal] = 0

    medal_table["Total"] = (
        medal_table["Gold"]
        + medal_table["Silver"]
        + medal_table["Bronze"]
    )

    medal_table = (
        medal_table.sort_values("Total", ascending=False)
        .reset_index()
    )

    return medal_table    
def country_medal_trend(df, country):

    country_df = df[
        (df["Region"] == country) &
        (df["Medal"].notna())
    ]

    trend = (
        country_df.groupby("Year")
        .size()
        .reset_index(name="Medals")
    )

    fig = px.line(
        trend,
        x="Year",
        y="Medals",
        markers=True,
        title=f"{country} Medal Trend"
    )

    fig.update_layout(
        template="plotly_white",
        height=450
    )

    return fig
def compare_countries(df, country1, country2):

    compare = df[df["Region"].isin([country1, country2])]

    result = (
        compare.groupby("Region")
        .agg(
            Athletes=("Name", "nunique"),
            Medals=("Medal", "count"),
            Sports=("Sport", "nunique"),
            Events=("Event", "nunique"),
            Olympic_Years=("Year", "nunique")
        )
        .reset_index()
    )

    return result    
def medal_trend(df):

    yearly = (
        df.groupby("Year")["Medal"]
        .count()
        .reset_index()
    )

    fig = px.line(
        yearly,
        x="Year",
        y="Medal",
        markers=True,
        title="Medals Won Over Time"
    )

    fig.update_layout(
        template="plotly_white",
        height=500
    )

    return fig    
def country_medal_timeline(df, country):

    temp = df[df["Region"] == country]

    timeline = (
        temp.groupby("Year")["Medal"]
        .count()
        .reset_index()
    )

    fig = px.line(
        timeline,
        x="Year",
        y="Medal",
        markers=True,
        title=f"{country} Medal Timeline"
    )

    fig.update_layout(
        template="plotly_white",
        height=450
    )

    return fig
def country_top_sports(df, country):

    temp = df[df["Region"] == country]

    sports = (
        temp.groupby("Sport")["Medal"]
        .count()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        sports,
        x="Sport",
        y="Medal",
        text_auto=True,
        title=f"Top Sports - {country}"
    )

    fig.update_layout(
        template="plotly_white",
        height=450
    )

    return fig
def country_top_athletes(df, country):

    temp = df[df["Region"] == country]

    athletes = (
        temp.groupby("Name")["Medal"]
        .count()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    return athletes    
def athlete_medal_timeline(df, athlete):

    temp = df[
        (df["Name"] == athlete) &
        (df["Medal"].notna())
    ]

    timeline = (
        temp.groupby("Year")
        .size()
        .reset_index(name="Medals")
    )

    fig = px.line(
        timeline,
        x="Year",
        y="Medals",
        markers=True,
        title=f"{athlete} Medal Timeline"
    )

    fig.update_layout(
        template="plotly_white",
        height=450
    )

    return fig
def athlete_summary(df, athlete):

    temp = df[df["Name"] == athlete]

    summary = {
        "Country": temp["Region"].dropna().iloc[0] if not temp["Region"].dropna().empty else "N/A",
        "Sports": temp["Sport"].nunique(),
        "Olympics": temp["Year"].nunique(),
        "Gold": (temp["Medal"] == "Gold").sum(),
        "Silver": (temp["Medal"] == "Silver").sum(),
        "Bronze": (temp["Medal"] == "Bronze").sum(),
        "Total": temp["Medal"].notna().sum()
    }

    return summary
def athlete_history(df, athlete):

    temp = df[df["Name"] == athlete]

    return temp[
        [
            "Year",
            "City",
            "Sport",
            "Event",
            "Medal"
        ]
    ].sort_values("Year")      
def sport_participation(df, sport):

    temp = df[df["Sport"] == sport]

    yearly = (
        temp.groupby("Year")["Name"]
        .nunique()
        .reset_index(name="Athletes")
    )

    fig = px.line(
        yearly,
        x="Year",
        y="Athletes",
        markers=True,
        title=f"{sport} Participation Trend"
    )

    fig.update_layout(
        template="plotly_white",
        height=450
    )

    return fig
def sport_top_countries(df, sport):

    temp = df[
        (df["Sport"] == sport) &
        (df["Medal"].notna())
    ]

    countries = (
        temp.groupby("Region")["Medal"]
        .count()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        countries,
        x="Region",
        y="Medal",
        text_auto=True,
        title=f"Top Countries in {sport}"
    )

    fig.update_layout(
        template="plotly_white",
        height=450
    )

    return fig
def sport_top_athletes(df, sport):

    temp = df[
        (df["Sport"] == sport) &
        (df["Medal"].notna())
    ]

    athletes = (
        temp.groupby("Name")["Medal"]
        .count()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    return athletes
def sport_events(df, sport):

    temp = df[df["Sport"] == sport]

    return (
        temp["Event"]
        .drop_duplicates()
        .sort_values()
        .reset_index(drop=True)
    )              