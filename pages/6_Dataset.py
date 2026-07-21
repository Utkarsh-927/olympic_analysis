import streamlit as st
import pandas as pd
from utils.loader import load_data

st.set_page_config(
    page_title="Dataset Explorer",
    page_icon="📄",
    layout="wide"
)

athletes, medal_df = load_data()

st.title("📄 Dataset Explorer")

tab1, tab2, tab3, tab4 = st.tabs([
    "Preview",
    "Columns",
    "Missing Values",
    "Statistics"
])

# Preview
with tab1:

    st.subheader("Dataset Preview")

    rows = st.slider(
        "Rows",
        10,
        200,
        50
    )

    st.dataframe(
        athletes.head(rows),
        use_container_width=True
    )

# Columns
with tab2:

    info = pd.DataFrame({
        "Column": athletes.columns,
        "Data Type": athletes.dtypes.astype(str),
        "Non Null": athletes.count().values,
        "Missing": athletes.isnull().sum().values
    })

    st.dataframe(
        info,
        use_container_width=True,
        hide_index=True
    )

# Missing Values
with tab3:

    missing = (
        athletes.isnull()
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    missing.columns = [
        "Column",
        "Missing Values"
    ]

    st.dataframe(
        missing,
        use_container_width=True,
        hide_index=True
    )

# Statistics
with tab4:

    st.dataframe(
        athletes.describe(include="all"),
        use_container_width=True
    )

st.divider()

csv = athletes.to_csv(index=False)

st.download_button(
    "⬇ Download Dataset",
    csv,
    file_name="olympic_dataset.csv",
    mime="text/csv"
)