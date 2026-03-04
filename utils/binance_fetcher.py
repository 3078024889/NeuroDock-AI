import requests
import pandas as pd

class BinanceFetcher:

    BASE_URL = "https://api.binance.com/api/v3/klines"

    def fetch_klines(self, symbol="BTCUSDT", interval="1h", limit=100):
        params = {
            "symbol": symbol,
            "interval": interval,
            "limit": limit
        }

        response = requests.get(self.BASE_URL, params=params)
        data = response.json()

        df = pd.DataFrame(data, columns=[
            "time","open","high","low","close","volume",
            "close_time","qav","trades","tbbav","tbqav","ignore"
        ])

        df["close"] = df["close"].astype(float)
        return df
