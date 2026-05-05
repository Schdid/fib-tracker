# Fib Tracker

24/7 crypto futures dashboard tracking Open Interest, Funding Rate, CVD, and auto-drawn Fibonacci retracements across Binance + Bybit. Sends email when a fib level fills.

## Coins

BTC, ETH, SOL, TAO, ZEC, ENA, LTC, HYPE

Per-coin toggle between Binance and Bybit (HYPE = Bybit only).

## Fib Levels

- BTC: 0.786, 0.75
- All others: 0.618, 0.5, 0.382, 0.25

Fill = price wicks into the level after the fib is drawn. One email per fill (deduped).

## Timeframes

15m, 30m, 1h, 4h, 1D, 1W (TradingView-style switcher in the UI).

## Stack

- Worker: Python, GitHub Actions cron (every 5 min)
- Frontend: static HTML + TradingView Lightweight Charts on Cloudflare Pages
- State: `data/state.json` committed back to repo
- Email: Gmail SMTP via app password (stored in GitHub Actions secrets)

## Layout

```
fib-tracker/
  config.py              # coins, fib levels, email settings
  worker.py              # main loop, runs every 5 min
  requirements.txt
  tools/
    fetch_binance.py     # OI, funding, candles, aggTrades
    fetch_bybit.py       # same for bybit
    compute_cvd.py       # cumulative volume delta from trades
    detect_swings.py     # zigzag swing detection
    draw_fib.py          # compute fib levels from swing high/low
    check_fills.py       # detect new fills, dedupe
    notify_email.py      # SMTP send
    store.py             # read/write state.json
  frontend/
    index.html
    app.js
    style.css
  data/
    state.json           # current OI/funding/CVD + active fibs + fill history
  .github/workflows/
    poll.yml             # cron: every 5 min, runs worker.py
```

## Deploy

1. Push repo public to GitHub
2. Add secrets in repo settings: `GMAIL_USER`, `GMAIL_APP_PASSWORD`, `NOTIFY_TO`
3. Enable GitHub Actions
4. Connect Cloudflare Pages to the repo, build dir = `frontend/`

## Local dev

```bash
cd projects/fib-tracker
pip install -r requirements.txt
python worker.py        # one-shot poll
python -m http.server 8000 --directory frontend
```
