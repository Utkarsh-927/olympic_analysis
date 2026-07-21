import pandas as pd

def total_athletes(df):
    return df["Name"].nunique()


def total_countries(df):
    return df["Region"].dropna().nunique()


def total_sports(df):
    return df["Sport"].nunique()


def total_events(df):
    return df["Event"].nunique()


def total_games(df):
    return df["Year"].nunique()


def total_medals(df):
    return df["Medal"].notna().sum()