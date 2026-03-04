class StrategyAgent:
    def generate_strategy(self, signal, risk, sentiment):
        
        if risk["risk_level"] == "Elevated":
            action = "Reduce exposure and wait for confirmation."
        else:
            if sentiment["sentiment"] == "Bullish":
                action = "Monitor breakout opportunities."
            elif sentiment["sentiment"] == "Bearish":
                action = "Consider defensive positioning."
            else:
                action = "Wait for clearer direction."
                
        return {
            "strategy": action
        }
