class RiskAgent:
    def evaluate_risk(self, signal_data):
        if signal_data["volatility"] == "High":
            risk_level = "Elevated"
        else:
            risk_level = "Normal"
            
        return {
            "risk_level": risk_level
        }
