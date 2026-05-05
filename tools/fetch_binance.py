"""Binance USDT-M Futures public API client. No key required for these endpoints."""
import requests
import time

BASE = "https://fapi.binance.com"

# Map our timeframe codes to Binance interval codes.
TF_MAP = {"15m": "15m", "30m": "30m", "1h": "1h", "4h": "4h", "1D": "1d", "1W": "1w"}


def _get(path: str, params: dict | None = None) -> dict | list:
    r = requests.get(f"{BASE}{path}", params=params or {}, timeout=15)
    r.raise_for_status()
    return r.json()


def get_open_interest(symbol: str) -> dict:
    """Latest OI value (in coin units) and notional via mark price."""
    oi = _get("/fapi/v1/openInterest", {"symbol": symbol})
    mark = _get("/fapi/v1/premiumIndex", {"symbol": symbol})
    qty = float(oi["openInterest"])
    price = float(mark["markPrice"])
    return {
        "symbol": symbol,
        "oi_qty": qty,
        "oi_usd": qty * price,
        "ts": int(oi["time"]),
    }


def get_funding_rate(symbol: str) -> dict:
    """Current funding rate + next funding time."""
    p = _get("/fapi/v1/premiumIndex", {"symbol": symbol})
    return {
        "symbol": symbol,
        "funding_rate": float(p["lastFundingRate"]),
        "next_funding_ts": int(p["nextFundingTime"]),
        "mark_price": float(p["markPrice"]),
    }


def get_klines(symbol: str, interval: str, limit: int = 500) -> list[dict]:
    """OHLCV candles. Returns list of {ts, o, h, l, c, v}."""
    raw = _get("/fapi/v1/klines", {
        "symbol": symbol,
        "interval": TF_MAP[interval],
        "limit": limit,
    })
    return [
        {"ts": k[0], "o": float(k[1]), "h": float(k[2]),
         "l": float(k[3]), "c": float(k[4]), "v": float(k[5])}
        for k in raw
    ]


def get_agg_trades(symbol: str, lookback_minutes: int = 15) -> list[dict]:
    """Aggregated trades for the last N minutes. Used to compute CVD.

    Binance returns max 1000 trades per call. For high-volume pairs over 15 min
    we may need multiple calls; this simple version fetches the most recent batch.
    """
    end = int(time.time() * 1000)
    start = end - lookback_minutes * 60_000
    raw = _get("/fapi/v1/aggTrades", {
        "symbol": symbol,
        "startTime": start,
        "endTime": end,
        "limit": 1000,
    })
    return [
        {"ts": t["T"], "price": float(t["p"]), "qty": float(t["q"]),
         "buyer_maker": t["m"]}
        for t in raw
    ]
