"""state.json read/write.

Schema:
{
  "updated_ts": 1234567890000,
  "coins": {
    "BTC": {
      "binance": {
        "oi_qty": 12345.6, "oi_usd": ..., "oi_history": [{ts, oi_usd}, ...],
        "funding_rate": 0.0001, "next_funding_ts": ..., "mark_price": ...,
        "cvd": 12345.6,
        "timeframes": {
          "15m": {
            "swing_start": {ts, price, kind},
            "swing_end":   {ts, price, kind},
            "direction":   "up" | "down",
            "levels":      {"0.618": 64321.0, ...},
            "filled":      [{ratio, price, ts}, ...],
            "candles":     [{ts,o,h,l,c,v}, ...]   # last N for the chart
          },
          ...
        }
      },
      "bybit": { ... same shape ... }
    },
    ...
  }
}
"""
import json
from config import STATE_FILE


def load_state() -> dict:
    if not STATE_FILE.exists():
        return {"updated_ts": 0, "coins": {}}
    return json.loads(STATE_FILE.read_text())


def save_state(state: dict) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, separators=(",", ":")))


def ensure_path(state: dict, coin: str, exchange: str) -> dict:
    state["coins"].setdefault(coin, {})
    state["coins"][coin].setdefault(exchange, {
        "oi_qty": 0, "oi_usd": 0, "oi_history": [],
        "funding_rate": 0, "next_funding_ts": 0, "mark_price": 0,
        "cvd": 0,
        "timeframes": {},
    })
    return state["coins"][coin][exchange]


def append_oi_history(node: dict, ts: int, oi_usd: float, max_points: int = 288) -> None:
    """Keep ~24h of 5-min snapshots."""
    node["oi_history"].append({"ts": ts, "oi_usd": oi_usd})
    node["oi_history"] = node["oi_history"][-max_points:]


def append_cvd_history(node: dict, ts: int, cvd: float, max_points: int = 288) -> None:
    """Keep ~24h of CVD snapshots so the frontend can plot a line."""
    node.setdefault("cvd_history", []).append({"ts": ts, "cvd": cvd})
    node["cvd_history"] = node["cvd_history"][-max_points:]
