class StrategyAgent:

    def generate(self, structure, risk, sentiment):

        if risk == "High Volatility":
            action = "Wait for pullback confirmation."
        elif structure == "Bullish Trend":
            action = "Consider trend-following strategy."
        else:
            action = "Consider defensive positioning."

        return {"strategy": action}
