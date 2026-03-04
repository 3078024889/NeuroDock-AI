from signal_agent import SignalAgent
from risk_agent import RiskAgent
from sentiment_agent import SentimentAgent
from strategy_agent import StrategyAgent

def run_neurodock():
    print("\n=== NeuroDock AI - Binance Neural Grid ===\n")
    
    signal_agent = SignalAgent()
    risk_agent = RiskAgent()
    sentiment_agent = SentimentAgent()
    strategy_agent = StrategyAgent()
    
    signal = signal_agent.analyze_market()
    print("Signal Agent Output:", signal)
    
    risk = risk_agent.evaluate_risk(signal)
    print("Risk Agent Output:", risk)
    
    sentiment = sentiment_agent.analyze_sentiment()
    print("Sentiment Agent Output:", sentiment)
    
    strategy = strategy_agent.generate_strategy(signal, risk, sentiment)
    print("Strategy Agent Output:", strategy)
    
    print("\n=== End of Analysis ===\n")

if __name__ == "__main__":
    run_neurodock()
