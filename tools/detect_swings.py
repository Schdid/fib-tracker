"""ZigZag swing detector.

Walks candles in order, marking a new pivot when price has reversed by at
least `threshold_pct` from the last extreme. Returns the most recent swing
high → swing low (or low → high) pair so the fib can be drawn from it.
"""


def find_swings(candles: list[dict], threshold_pct: float) -> list[dict]:
    """Return a list of pivots: [{ts, price, kind}] where kind is 'H' or 'L'.

    threshold_pct: e.g. 2.0 means a 2% reversal confirms a new pivot.
    """
    if not candles:
        return []

    threshold = threshold_pct / 100.0
    pivots: list[dict] = []

    # Seed with the first candle as a tentative pivot, direction unknown.
    last_extreme_price = candles[0]["c"]
    last_extreme_ts    = candles[0]["ts"]
    direction: str | None = None  # 'up' = looking for higher highs

    for c in candles[1:]:
        high, low, ts = c["h"], c["l"], c["ts"]

        if direction is None:
            up_move = (high - last_extreme_price) / last_extreme_price
            dn_move = (last_extreme_price - low) / last_extreme_price
            if up_move >= threshold:
                pivots.append({"ts": last_extreme_ts, "price": last_extreme_price, "kind": "L"})
                last_extreme_price, last_extreme_ts = high, ts
                direction = "up"
            elif dn_move >= threshold:
                pivots.append({"ts": last_extreme_ts, "price": last_extreme_price, "kind": "H"})
                last_extreme_price, last_extreme_ts = low, ts
                direction = "down"
            continue

        if direction == "up":
            if high > last_extreme_price:
                last_extreme_price, last_extreme_ts = high, ts
                continue
            if (last_extreme_price - low) / last_extreme_price >= threshold:
                pivots.append({"ts": last_extreme_ts, "price": last_extreme_price, "kind": "H"})
                last_extreme_price, last_extreme_ts = low, ts
                direction = "down"
        else:  # direction == "down"
            if low < last_extreme_price:
                last_extreme_price, last_extreme_ts = low, ts
                continue
            if (high - last_extreme_price) / last_extreme_price >= threshold:
                pivots.append({"ts": last_extreme_ts, "price": last_extreme_price, "kind": "L"})
                last_extreme_price, last_extreme_ts = high, ts
                direction = "up"

    # Append the running extreme as the latest tentative pivot.
    if direction is not None:
        kind = "H" if direction == "up" else "L"
        pivots.append({"ts": last_extreme_ts, "price": last_extreme_price, "kind": kind})

    return pivots


def latest_swing_pair(pivots: list[dict]) -> tuple[dict, dict] | None:
    """Returns (swing_start, swing_end) where end is the most recent pivot.

    The fib is drawn from start → end. Direction is inferred from kinds:
      - if end is 'L' (down move): fib retracements measure the bounce up
      - if end is 'H' (up move):   fib retracements measure the pullback down
    """
    if len(pivots) < 2:
        return None
    return pivots[-2], pivots[-1]
