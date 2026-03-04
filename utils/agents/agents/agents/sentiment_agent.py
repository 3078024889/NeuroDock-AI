class SentimentAgent:

    def analyze(self, structure):
        if structure == "Bullish Trend":
            sentiment = "Market Optimistic"
        else:
            sentiment = "Market Defensive"

        return {"sentiment": sentiment}
