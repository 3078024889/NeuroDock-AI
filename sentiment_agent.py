import random

class SentimentAgent:
    def analyze_sentiment(self):
        sentiment = random.choice(["Bullish", "Neutral", "Bearish"])
        return {
            "sentiment": sentiment
        }
