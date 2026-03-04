import streamlit as st
from utils.binance_fetcher import BinanceFetcher
from agents.signal_agent import SignalAgent
from agents.risk_agent import RiskAgent
from agents.sentiment_agent import SentimentAgent
from agents.strategy_agent import StrategyAgent

st.title("NeuroDock AI - Binance Neural Grid")

symbol = st.selectbox("Select Trading Pair", ["BTCUSDT", "ETHUSDT"])

fetcher = BinanceFetcher()
df = fetcher.fetch_klines(symbol)

signal_agent = SignalAgent()
signal = signal_agent.analyze(df)

risk_agent = RiskAgent()
risk = risk_agent.evaluate(signal)

sentiment_agent = SentimentAgent()
sentiment = sentiment_agent.analyze(signal["structure"])

strategy_agent = StrategyAgent()
strategy = strategy_agent.generate(
    signal["structure"],
    risk["risk_level"],
    sentiment["sentiment"]
)

st.subheader("Market Structure")
st.write(signal)

st.subheader("Risk Evaluation")
st.write(risk)

st.subheader("Sentiment Analysis")
st.write(sentiment)

st.subheader("Strategy Output")
st.write(strategy)

st.line_chart(df["close"])
