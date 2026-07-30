class Backtest:
    def __init__(self, predictor):
        self.predictor = predictor

    def run(self, candles):
        signal = self.predictor.predict(candles)
        # Extremely simplified paper result
        return {
            "signal": signal,
            "pnl_pct": 0.0,
            "mode": "paper"
        }
