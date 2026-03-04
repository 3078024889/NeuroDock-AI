class RiskAgent:

    def evaluate(self, signal_data):

        diff = abs(signal_data["ma20"] - signal_data["ma50"])

        if diff / signal_data["last_price"] > 0.03:
            risk = "High Volatility"
        else:
            risk = "Normal"

        return {"risk_level": risk}
