"""Central config for fib-tracker."""
import os

# Coins → preferred exchange. UI lets the user override per coin at runtime.
COINS = {
    "BTC":  {"binance": "BTCUSDT",  "bybit": "BTCUSDT"},
    "ETH":  {"binance": "ETHUSDT",  "bybit": "ETHUSDT"},
    "SOL":  {"binance": "SOLUSDT",  "bybit": "SOLUSDT"},
    "TAO":  {"binance": "TAOUSDT",  "bybit": "TAOUSDT"},
    "ZEC":  {"binance": "ZECUSDT",  "bybit": "ZECUSDT"},
    "ENA":  {"binance": "ENAUSDT",  "bybit": "ENAUSDT"},
    "LTC":  {"binance": "LTCUSDT",  "bybit": "LTCUSDT"},
    "HYPE": {"binance": None,        "bybit": "HYPEUSDT"},  # Bybit only
}

DEFAULT_EXCHANGE = "binance"

# Timeframes the UI exposes. Worker polls all of them every cycle for every coin.
TIMEFRAMES = ["15m", "30m", "1h", "4h", "1D", "1W"]

# Fib levels per coin. BTC has its own set.
FIB_LEVELS_BTC = [0.7816, 0.75]
FIB_LEVELS_DEFAULT = [0.618, 0.5, 0.382, 0.25]

def fib_levels_for(coin: str) -> list[float]:
    return FIB_LEVELS_BTC if coin == "BTC" else FIB_LEVELS_DEFAULT

# ZigZag swing detection threshold per timeframe (% move required to mark a swing).
# Tuned to roughly match TradingView's auto-fib behavior.
SWING_THRESHOLD_PCT = {
    "15m": 1.5,
    "30m": 2.0,
    "1h":  2.5,
    "4h":  4.0,
    "1D":  6.0,
    "1W":  10.0,
}

# How many candles to pull for swing detection.
CANDLE_LOOKBACK = 500

# Fill tolerance: price must touch within this % of the level to count as filled.
FILL_TOLERANCE_PCT = 0.05  # 0.05% = 5 bps

# Email — matches the GMAIL_ADDRESS / GMAIL_APP_PASSWORD convention used
# elsewhere in the executive-assistant repo (leads-pipeline/.env).
GMAIL_ADDRESS       = os.environ.get("GMAIL_ADDRESS", os.environ.get("GMAIL_USER", ""))
GMAIL_APP_PASSWORD  = os.environ.get("GMAIL_APP_PASSWORD", "")
NOTIFY_TO           = os.environ.get("NOTIFY_TO", "adam.chedid@gmail.com")

# Paths
import pathlib
ROOT = pathlib.Path(__file__).parent
STATE_FILE = ROOT / "data" / "state.json"
