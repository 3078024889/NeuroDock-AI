import random

class SignalAgent:
    def analyze_market(self):
        volatility = random.choice(["Low", "Moderate", "High"])
        structure = random.choice(["Range", "Breakout", "Reversal"])
        
        return {
            "volatility": volatility,
            "structure": structure
        }
