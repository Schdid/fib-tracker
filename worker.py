"""Main poll cycle. Runs once per invocation; GitHub Actions cron fires it
every 5 minutes. For each (coin, exchange, timeframe):

  1. Refresh OI + funding + recent CVD
  2. Re-detect swings on the latest candles
  3. Recompute fib levels
  4. Check for new fills (deduped against state)
  5. Email any new fills
  6. Persist everything to data/state.json
"""
import time
import traceback

from config import (
    COINS, TIMEFRAMES, SWING_THRESHOLD_PCT,
    CANDLE_LOOKBACK, fib_levels_for,
)
from tools import fetch_binance, fetch_bybit, compute_cvd, store
from tools.detect_swings import find_swings, latest_swing_pair
from tools.draw_fib import fib_levels, fib_direction
from tools.check_fills import check_fills, candles_after
from tools.notify_email import send_fill_email


CHART_CANDLE_KEEP = 200  # how many candles to keep in state for the chart


def process_coin_exchange(state: dict, coin: str, exchange: str, symbol: str) -> list[dict]:
    """Returns list of newly filled levels (with metadata) for emailing."""
    fetcher = fetch_binance if exchange == "binance" else fetch_bybit
    node = store.ensure_path(state, coin, exchange)
    new_fills_for_email: list[dict] = []

    # 1. OI + funding (one call each, shared across timeframes)
    try:
        oi = fetcher.get_open_interest(symbol)
        node["oi_qty"], node["oi_usd"] = oi["oi_qty"], oi["oi_usd"]
        store.append_oi_history(node, oi["ts"], oi["oi_usd"])
    except Exception as e:
        print(f"[{coin} {exchange}] OI fetch failed: {e}")

    try:
        f = fetcher.get_funding_rate(symbol)
        node["funding_rate"]    = f["funding_rate"]
        node["next_funding_ts"] = f["next_funding_ts"]
        node["mark_price"]      = f["mark_price"]
    except Exception as e:
        print(f"[{coin} {exchange}] funding fetch failed: {e}")

    # 2. CVD: compute delta over the last poll window and add to running total.
    try:
        if exchange == "binance":
            trades = fetcher.get_agg_trades(symbol, lookback_minutes=5)
            delta = compute_cvd.cvd_from_binance_trades(trades)
        else:
            trades = fetcher.get_recent_trades(symbol)
            delta = compute_cvd.cvd_from_bybit_trades(trades)
        node["cvd"] = compute_cvd.running_cvd(node.get("cvd", 0.0), delta)
        store.append_cvd_history(node, int(time.time() * 1000), node["cvd"])
    except Exception as e:
        print(f"[{coin} {exchange}] CVD fetch failed: {e}")

    # 3-5. Per-timeframe: swing → fib → fills
    for tf in TIMEFRAMES:
        try:
            candles = fetcher.get_klines(symbol, tf, limit=CANDLE_LOOKBACK)
            if len(candles) < 10:
                continue

            tf_node = node["timeframes"].setdefault(tf, {})
            tf_node["candles"] = candles[-CHART_CANDLE_KEEP:]

            pivots = find_swings(candles, SWING_THRESHOLD_PCT[tf])
            pair = latest_swing_pair(pivots)
            if pair is None:
                continue
            start, end = pair

            # If the swing-end pivot changed, this is a new fib.
            # Backfill any already-touched levels SILENTLY (no email).
            prev_end_ts = tf_node.get("swing_end", {}).get("ts")
            new_fib = prev_end_ts != end["ts"]

            tf_node["swing_start"] = start
            tf_node["swing_end"]   = end
            direction = fib_direction(start, end)
            tf_node["direction"]   = direction

            ratios = fib_levels_for(coin)
            levels = fib_levels(start, end, ratios)
            tf_node["levels"] = {str(r): p for r, p in levels.items()}

            if new_fib:
                # Seed filled list from history without emailing.
                tf_node["filled"] = []
                since = candles_after(candles, end["ts"])
                backfill = check_fills(levels, since, direction, set())
                for f in backfill:
                    f["backfilled"] = True
                tf_node["filled"].extend(backfill)
                continue  # skip the new-fill email path on this cycle

            already = {f["ratio"] for f in tf_node.get("filled", [])}
            # Only look at candles since the LAST poll (use updated_ts as the cutoff
            # if available; otherwise since swing end).
            cutoff = max(end["ts"], state.get("updated_ts", 0) - 60_000)
            since  = candles_after(candles, cutoff)
            new    = check_fills(levels, since, direction, already)

            if new:
                tf_node["filled"].extend(new)
                for f in new:
                    new_fills_for_email.append({
                        "coin": coin, "exchange": exchange, "tf": tf,
                        "ratio": f["ratio"], "level_price": f["price"],
                        "ts": f["ts"], "current_price": candles[-1]["c"],
                    })
        except Exception as e:
            print(f"[{coin} {exchange} {tf}] failed: {e}")
            traceback.print_exc()

    return new_fills_for_email


def main() -> None:
    state = store.load_state()
    state.setdefault("coins", {})
    all_new_fills: list[dict] = []

    for coin, syms in COINS.items():
        for exchange in ("binance", "bybit"):
            symbol = syms.get(exchange)
            if not symbol:
                continue
            try:
                fills = process_coin_exchange(state, coin, exchange, symbol)
                all_new_fills.extend(fills)
            except Exception as e:
                print(f"[{coin} {exchange}] cycle failed: {e}")
                traceback.print_exc()

    state["updated_ts"] = int(time.time() * 1000)
    store.save_state(state)

    if all_new_fills:
        try:
            send_fill_email(all_new_fills)
        except Exception as e:
            print(f"email send failed: {e}")

    print(f"cycle done. coins: {len(state['coins'])}. new fills: {len(all_new_fills)}.")


if __name__ == "__main__":
    main()
