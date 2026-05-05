"""Cumulative Volume Delta from trade data.

CVD = sum(buy_volume - sell_volume) over time.
On Binance, trade["buyer_maker"] = True means the aggressor was a SELLER
  (buyer was passive maker), so qty counts as sell volume.
On Bybit, trade["side"] is "Buy" or "Sell" from the aggressor's perspective.
"""


def cvd_from_binance_trades(trades: list[dict]) -> float:
    """Returns delta over the window: positive = net buying, negative = net selling."""
    delta = 0.0
    for t in trades:
        if t["buyer_maker"]:  # aggressor sold
            delta -= t["qty"]
        else:                  # aggressor bought
            delta += t["qty"]
    return delta


def cvd_from_bybit_trades(trades: list[dict]) -> float:
    delta = 0.0
    for t in trades:
        if t["side"] == "Buy":
            delta += t["qty"]
        else:
            delta -= t["qty"]
    return delta


def running_cvd(prev_cvd: float, delta: float) -> float:
    """Append a window's delta to the running total."""
    return prev_cvd + delta
