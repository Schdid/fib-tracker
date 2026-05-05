"""Compute fib retracement levels from a swing pair."""


def fib_levels(start: dict, end: dict, ratios: list[float]) -> dict:
    """Returns {ratio: price} for each ratio.

    Convention: 0.0 = end of move (the most recent pivot), 1.0 = start of move.
    So for a swing low (end='L') after a swing high (start='H'):
      - 0.0 = the low,  1.0 = the high
      - 0.5 retracement = midpoint, where price would be on a 50% bounce
    For an up swing (end='H' after start='L'):
      - 0.0 = the high, 1.0 = the low
      - 0.5 retracement = where price would be on a 50% pullback
    """
    a = start["price"]
    b = end["price"]
    span = a - b  # positive if down-move, negative if up-move
    return {r: b + span * r for r in ratios}


def fib_direction(start: dict, end: dict) -> str:
    """'up' = retracement of an up-move (price pulling back down).
       'down' = retracement of a down-move (price bouncing up)."""
    return "up" if end["price"] > start["price"] else "down"
