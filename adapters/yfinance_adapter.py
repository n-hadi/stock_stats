import streamlit as st
import pandas as pd

@st.cache_data
def yahoo_csv_to_canonical(path: str) -> pd.DataFrame:
    # load wide-format CSV
    df = pd.read_csv(
        path,
        header=[0, 1],      # MultiIndex columns
        index_col=0,
        parse_dates=True
    )

    # stack ticker level -> rows
    df = df.stack(level=0).reset_index()

    # rename columns to canonical names
    df = df.rename(columns={
        "Date": "date",
        "Ticker": "ticker",
        "Open": "open",
        "High": "high",
        "Low": "low",
        "Close": "close",
        "Volume": "volume",
    })

    df = df[["date", "ticker", "open", "high", "low", "close", "volume"]]

    df = df.sort_values(["ticker", "date"]).reset_index(drop=True)

    return df
