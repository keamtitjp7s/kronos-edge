from .predictor import Predictor
from .data import LiveAdapter
from .backtest import Backtest

def main():
    print("kronos-edge ready")
    adapter = LiveAdapter(symbol="BTC/USDT")
    candles = adapter.fetch(limit=5)
    print("Sample candles:", candles)

    pred = Predictor()
    signal = pred.predict(candles)
    print("Signal:", signal)

    bt = Backtest(pred)
    print("Backtest result:", bt.run(candles))

if __name__ == "__main__":
    main()
