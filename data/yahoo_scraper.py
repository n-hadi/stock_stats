import yfinance as yf
import pandas as pd

tickers = [
    "AAPL","MSFT","GOOGL","AMZN","META","NVDA","TSLA","JPM","V","MA"
]

df = yf.download(
    tickers,
    start="2025-01-01",
    end="2025-12-14",
    auto_adjust=True,
    group_by="ticker"
)

df.to_csv("us_stocks_daily.csv")