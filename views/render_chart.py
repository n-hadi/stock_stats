import streamlit as st

def render_chart(df, ticker, metric ):
    sub = df[df["ticker"] == ticker].sort_values("date")
    st.line_chart(sub.set_index("date")[metric])