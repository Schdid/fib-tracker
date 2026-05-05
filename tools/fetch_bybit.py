"""Bybit v5 public API client for linear (USDT) perpetuals. No key required."""
import requests
import time

BASE = "https://api.bybit.com"
CATEGORY = "linear"

TF_MAP = {"15m": "15", "30m": "30", "1h": "60", "4h": "240", "1D": "D", "1W": "W"}


def _get(path: str, params: dict | None = None) -> dict:
    r = requests.get(f"{BASE}{path}", params=params or {}, timeout=15)
    r.raise_for_status()
    j = r.json()
    if j.get("retCode") != 0:
        raise RuntimeError(f"Bybit error: {j}")
    return j["result"]


def get_open_interest(symbol: str) -> dict:
    """Latest 5-min OI snapshot."""
    res = _get("/v5/market/open-interest", {
        "category": CATEGORY,
        "symbol": symbol,
        "intervalTime": "5min",
        "limit": 1,
    })
    row = res["list"][0]
    qty = float(row["openInterest"])
    # Get mark price for USD notional
    tick = _get("/v5/market/tickers", {"category": CATEGORY, "symbol": symbol})
    price = float(tick["list"][0]["markPrice"])
    return {
        "symbol": symbol,
        "oi_qty": qty,
        "oi_usd": qty * price,
        "ts": int(row["timestamp"]),
    }


def get_funding_rate(symbol: str) -> dict:
    """Current funding + next funding time."""
    tick = _get("/v5/market/tickers", {"category": CATEGORY, "symbol": symbol})
    t = tick["list"][0]
    return {
        "symbol": symbol,
        "funding_rate": float(t["fundingRate"]),
        "next_funding_ts": int(t["nextFundingTime"]),
        "mark_price": float(t["markPrice"]),
    }


def get_klines(symbol: str, interval: str, limit: int = 500) -> list[dict]:
    """OHLCV candles. Bybit returns newest-first → we reverse."""
    res = _get("/v5/market/kline", {
        "category": CATEGORY,
        "symbol": symbol,
        "interval": TF_MAP[interval],
        "limit": limit,
    })
    rows = list(reversed(res["list"]))
    return [
        {"ts": int(r[0]), "o": float(r[1]), "h": float(r[2]),
         "l": float(r[3]), "c": float(r[4]), "v": float(r[5])}
        for r in rows
    ]


def get_recent_trades(symbol: str) -> list[dict]:
    """Bybit only exposes the last 1000 public trades (no time-range query).
    We use this snapshot for CVD; the worker builds CVD over time by appending
    deltas across runs.
    """
    res = _get("/v5/market/recent-trade", {
        "category": CATEGORY,
        "symbol": symbol,
        "limit": 1000,
    })
    return [
        {"ts": int(t["time"]), "price": float(t["price"]),
         "qty": float(t["size"]), "side": t["side"]}  # Buy / Sell
        for t in res["list"]
    ]
