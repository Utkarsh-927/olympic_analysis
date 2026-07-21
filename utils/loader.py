from pathlib import Path
import pandas as pd
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

@st.cache_data
def load_data():

    athletes = pd.read_csv(DATA_DIR / "all_athlete_games.csv")
    regions = pd.read_csv(DATA_DIR / "all_regions.csv")

    athletes.columns = athletes.columns.str.strip()
    regions.columns = regions.columns.str.strip()

    athletes = athletes.merge(
        regions,
        on="NOC",
        how="left"
    )


    medal_df = athletes.drop_duplicates(
        subset=[
            "Team",
            "NOC",
            "Year",
            "City",
            "Sport",
            "Event",
            "Medal"
        ]
    )

    return athletes, medal_df    