import pandas as pd

class SignalAgent:

    def analyze(self, df: pd.DataFrame):
        last_price = df["close"].iloc[-1]
        ma20 = df["close"].rolling(20).mean().iloc[-1]
        ma50 = df["close"].rolling(50).mean().iloc[-1]

        if ma20 > ma50:
            structure = "Bullish Trend"
        else:
            structure = "Bearish Trend"

        return {
            "last_price": last_price,
            "ma20": ma20,
            "ma50": ma50,
            "structure": structure
        }
