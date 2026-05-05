"""Detect when a fib level has been filled by recent price action.

A level is "filled" the first time price touches it (within tolerance) AFTER
the fib was drawn. We dedupe by (coin, exchange, timeframe, swing_end_ts, ratio)
so the same level only fires once per fib.
"""
from config import FILL_TOLERANCE_PCT


def fill_key(coin: str, exchange: str, tf: str, swing_end_ts: int, ratio: float) -> str:
    return f"{coin}|{exchange}|{tf}|{swing_end_ts}|{ratio}"


def check_fills(
    levels: dict,           # {ratio: price}
    candles_since_swing: list[dict],  # candles AFTER the swing-end pivot
    direction: str,         # 'up' (retracement down) or 'down' (retracement up)
    already_filled: set[float],
) -> list[dict]:
    """Returns list of newly filled levels: [{ratio, price, ts}].

    Direction matters: in an up-move retracement, price has to drop INTO the
    level from above; in a down-move retracement, price has to rise INTO it.
    """
    new_fills = []
    tol = FILL_TOLERANCE_PCT / 100.0

    for ratio, level_price in levels.items():
        if ratio in already_filled:
            continue
        for c in candles_since_swing:
            band_lo = level_price * (1 - tol)
            band_hi = level_price * (1 + tol)
            if direction == "up":
                # Pullback from a high: price must drop to or below the level
                if c["l"] <= band_hi:
                    new_fills.append({"ratio": ratio, "price": level_price, "ts": c["ts"]})
                    break
            else:
                # Bounce from a low: price must rise to or above the level
                if c["h"] >= band_lo:
                    new_fills.append({"ratio": ratio, "price": level_price, "ts": c["ts"]})
                    break

    return new_fills


def candles_after(candles: list[dict], swing_end_ts: int) -> list[dict]:
    return [c for c in candles if c["ts"] > swing_end_ts]
