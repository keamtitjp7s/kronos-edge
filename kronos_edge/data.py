class LiveAdapter:
    """Live data adapter – replace with real CCXT calls."""

    def __init__(self, symbol="BTC/USDT"):
        self.symbol = symbol

    def fetch(self, limit=10):
        # Simulated candles
        base = 60000.0
        return [
            {"open": base + i * 10, "high": base + i * 10 + 50, "low": base + i * 10 - 30, "close": base + i * 10 + 20, "volume": 100 + i}
            for i in range(limit)
        ]
