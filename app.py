import streamlit as st
import pandas as pd
from adapters.yfinance_adapter import yahoo_csv_to_canonical
from views.render_chart import render_chart

df = yahoo_csv_to_canonical("data/us_stocks_daily.csv")

tickers = sorted(df["ticker"].unique())
ticker = st.selectbox("Ticker", tickers)
metric = st.selectbox("Metric", ["close","open","high","low","volume"])

render_chart(df, ticker, metric)
