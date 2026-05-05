# Trader Study Guide: KillaXBT & zorathzzz

Researched 2026-05-05 for the fib-tracker dashboard project (BTC/ETH/SOL/TAO/ZEC/ENA/LTC/HYPE; OI + funding + CVD + fib retracements on Binance/Bybit).

> **Coverage caveat (read first).**
> - **KillaXBT**: extensive public footprint. Multiple news outlets quote his X posts verbatim, his trades are tracked on Phemex/CoinLive/ChainCatcher, and he appears on the ScalpX trading desk. Strong sourcing.
> - **zorathzzz**: **no verifiable public footprint.** Despite running broad neural and indexed searches across Exa, Google (WebSearch), Nitter mirrors (blocked), Threadreader, Rattibha, Typefully, twstalker, and direct X fetch, no quoted tweet, news article, podcast, or third-party coverage of `@zorathzzz` exists. The handle is either too small to be archived, recently created, frequently deleted, or the user typed the handle differently than how the account spells itself. **All claims about zorathzzz below are explicitly marked "no evidence found".** Do not treat any inferred section as fact — verify by opening the X profile directly.

---

## 1. KillaXBT — `@KillaXBT`

### 1.1 Bio / Background

- **Display name:** Killa
- **Bio (per follower-graph snapshot):** *"5 Years Trading | Wick hunting @scalpxofficial | ₿itcoin Order Flow Alchemist Trade on Bitunix"* ([twicopy snapshot](https://twicopy.com/lifeof100x/following))
- **Followers:** **180,000+** on X as of April 2026 ([ChainCatcher](https://www.chaincatcher.com/en/article/2258782), [Phemex News](https://phemex.com/news/article/trader-killa-shorts-bitcoin-at-74688-sets-stoploss-at-80000-73299))
- **Affiliation:** Trader at [ScalpX](https://scalpxtrades.com/) (paid signals/community alongside Saint, Chento, Blasto, ReBeL). Also publishes long-form posts to [OKX Feed](https://www.okx.com/en-ae/feed/post/57265338760384). Affiliate of Bitunix.
- **Track record / reputation:** Predicted the May 2025 cycle peak in advance; called the **$121,362 cycle top in June 2025**, off by only ~3.9% from the actual ~$126,100 ATH in October 2025 ([TradingView/NewsBTC](https://www.tradingview.com/news/newsbtc:a5832a4ca094b:0-analyst-who-called-bitcoin-s-top-correctly-now-predicting-the-bottom/), [Yahoo Finance](https://finance.yahoo.com/news/analyst-nailed-bitcoin-price-top-180733566.html)). Self-claims **"90% right this cycle on the HTF"**.
- **Style identity:** describes himself as a **"quantitative trader focused on BTC"** (per ChainCatcher / Phemex). His self-billed framework: **"rotational market mathematics"** and **"diminishing cycle analysis"** — counting market swings/oscillations and applying a decay multiple cycle-over-cycle.

### 1.2 Trading style summary

- **Primary asset:** BTC almost exclusively. Occasionally references ETH, but >95% of public output is Bitcoin.
- **Style mix:**
  - **HTF directional swing trader** (multi-week to multi-month). His "swing short at $74,688, SL $80k weekly close" trade is the canonical example ([CoinLive](https://www.coinlive.com/id/news-flash/1094321)).
  - **LTF/MTF setup caller** — weekly newsletter-style posts ("scenarios for the week ahead") that map liquidity grabs, FVG fills, and CME-gap magnets.
- **Time horizon:** says "long-term swing trade, not a short-term play" for his cycle short, intended hold "6–9 months".
- **Leverage:** uses **2.5x–3x cross margin** for HTF swings, sized to **10–15% of portfolio** with liquidation 40%+ from entry. Recommends **3–4x max** on smaller-range setups, **never 10x** ([NewsBTC Nov 2025](https://www.tradingview.com/news/newsbtc:55641d0e9094b:0-bitcoin-market-structure-signals-potential-sweep-before-upswing-details/)).

### 1.3 Per-timeframe approach

He does NOT publish 15m setups. His public posts skew HTF-heavy:

| Timeframe | What he uses it for |
|---|---|
| **1W / 1M** | The decision layer. "Weekly close above $80k invalidates my short." Monthly opens, monthly FVGs, monthly highs/lows. |
| **1D** | Bias and key-level mapping. Daily fair value gaps (FVG), daily POIs, 111-day SMA as trend confirmation. Says BTC "must hold above 111-day SMA to confirm trend reversal" ([Gate News April 2026](https://www.gate.com/news/detail/trader-killa-says-bitcoin-needs-to-hold-above-111-day-sma-to-confirm-trend-20528346)). |
| **4H** | Range structure, where he marks "ideal long zones" and supply pockets ($115k demand, $112-113.8k imbalance). |
| **1H** | LTF execution refinement — "LTF downtrend line break", liquidation cluster invalidation. |
| **15m / 5m** | Rarely referenced publicly (delegates this to ScalpX desk colleagues like Saint who run scalp setups). |

**Killa's emphasis:** he repeatedly says BTC has been **"mechanical"** for 2 years, dominated by clean ranges with corrections "lasting 2–3 weeks" ([@KillaXBT March 14 2026 quoted by BitcoinEthereumNews](https://bitcoinethereumnews.com/bitcoin/bitcoin-whale-activity-hits-six-year-high-as-retail-participation-stays-near-cycle-lows/)). HTF is where his edge lives.

### 1.4 Key indicators / signals (with quoted phrases)

This is the most useful section for the user's stack. KillaXBT's vocabulary maps almost 1:1 onto the OI/funding/CVD/fib dashboard:

- **Liquidation heatmaps (Coinglass-sourced).** Constantly references "liquidity clusters" on 7-day (LTF) and 30-day (HTF) views. Splits into "long-side liquidations between $X-Y" vs "short-side liquidations between $X-Y" and trades the asymmetry. Quote: *"BTC is trapped between long and short liquidation zones in both low and high time frames signaling a moment of market indecision"* ([NewsBTC June 2025](https://www.tradingview.com/news/newsbtc:cde896c5d094b:0-bitcoin-in-stalemate-with-liquidation-traps-on-both-sides-of-the-market/)).
- **Orderbook delta / CVD.** Direct quote (Oct 15, 2025): *"on this recent drop, orderbook delta has flipped positive. A sign that buyers are accumulating. Since september, every time delta has flipped green we have seen a push upwards on the HTF."* ([InvestX coverage](https://investx.fr/en/crypto-news/bitcoin-on-the-verge-of-exploding-to-new-ath-the-signal-that-never-fails/)).
- **Funding rate.** Uses negative funding + capitulation as a contrarian long trigger; uses sustained high positive funding as exhaustion warning. Earns funding fees as part of his short thesis ("If I'm right, I'll earn from both funding fees and the downside move").
- **Fair Value Gaps (FVG / "imbalance zones").** Heavily ICT-flavored vocabulary. *"daily fair value gap extending down to $113,355 ... such inefficiencies eventually get filled, as price retraces into the zone to rebalance order flow."* ([NewsBTC Sep 2025](https://www.tradingview.com/news/newsbtc:4ca45765c094b:0-bitcoin-tests-weekly-open-as-113-300-fair-value-gap-looms-what-it-means/)).
- **CME gaps.** Treats them as price magnets with a documented **98% historical fill rate** since BTC at $16k. Quote: *"since trading at $16,000, the Bitcoin market has seen 98% of weekend CME gaps filled."* ([XT.com](https://www.xt.com/en/blog/post/bitcoin-8-below-cme-gap-ahead-of-monthly-close-will-history-repeat)).
- **Weekly open / monthly open as pivots.** "Flipping the monthly open into support" is bullish; failing to hold is the trigger to fade. Quote: *"Bitcoin started the month on a strong technical footing, flipping the monthly open at $115,752 into support."* ([Bitcoinist Aug 2025](https://bitcoinist.com/bitcoin-bulls-in-control-120000-test-run-toward-ath)).
- **"Monthly open trap" / wick patterns.** *"Bitcoin historically tends to wick either up or down in a new month, forming one side of the monthly candle's wick."*
- **111-day SMA** as trend filter (mentioned April 2026).
- **Liquidity sweeps / "ruthless liquidity grab" / "stop hunts".** Standard SMC vocabulary. The double-sweep of last week's wick low is a recurring setup he calls.
- **Diminishing returns cycle model.** His original framework. The mathematical core: each successive BTC cycle's high-to-bottom multiple decays: 15.50x → 7.64x → 6.26x → 4.47x → projected **3.25x** for current cycle. He divides $126,100 by 3.25 to project a $38,800 cycle bottom.
- **Spot/perpetual divergence reasoning.** He is consistent about sourcing rallies: institutional spot accumulation = sustainable; futures-leverage-only rally = short-able. (Aligns 1:1 with the dashboard's spot vs perp CVD split.)

**Recurring phrases worth memorising:**
- *"Mechanical price action"*, *"market-maker orchestrated"*, *"textbook ranges"*
- *"Liquidity grab" / "double sweep" / "wick low"*
- *"Monthly open trap"*, *"weekly open as pivot"*
- *"CME gap as magnet"*
- *"Imbalance zone" / "FVG fill"*
- *"Diminishing cycle multiple"*
- *"My system / my framework / my data"* (he leans hard on quant/probabilistic framing, not vibes)

### 1.5 Entry/exit pattern examples (recent, dated)

1. **April 15 2026 — BTC swing short @ $74,688, SL $80k weekly close.** Stated as "final BTC swing short for the current cycle." On April 22, raised SL to **$83k** as price rallied. Currently underwater on the trade per Gate News April 23 ([CoinLive](https://www.coinlive.com/id/news-flash/1094321), [ChainCatcher](https://www.chaincatcher.com/en/article/2258782), [Phemex](https://phemex.com/news/article/trader-killa-shorts-bitcoin-at-74688-sets-stoploss-at-80000-73299)). **Lesson:** discipline on weekly-close invalidation, willingness to move SL up but not down.

2. **March 16 2026 — bearish thesis post.** *"We have 7 green consecutive daily candles, We pump over the weekend, We form a CME gap below, Directly into supply/liquidity, At the start of a new weekly open, And all of a sudden $BTC is bullish? Got it."* ([Coincu](https://coincu.com/markets/bitcoin-84000-cme-gap/)). Price subsequently dropped from ~$84k toward the mid-$70ks — thesis played out. **Lesson:** pattern-stacking — multiple bearish confluences (consecutive greens + weekend pump + CME gap below + supply zone + new weekly open) are how he builds short conviction.

3. **March 14 2026 — "easiest 2 years ever" post.** *"The past 2 years of trading $BTC have been some of the easiest ever. PA has been extremely mechanical and largely market maker orchestrated, with textbook ranges throughout. We've seen 2 years dominated by ranges, with corrections and impulsive moves typically lasting just 2–3 weeks."* ([BitcoinEthereumNews](https://bitcoinethereumnews.com/bitcoin/bitcoin-whale-activity-hits-six-year-high-as-retail-participation-stays-near-cycle-lows/)). **Lesson:** he assigns explicit duration constraints to corrections — useful for the user's swing planning.

4. **Oct 15 2025 — orderbook delta flip long signal.** Posted that delta flipped green during a drop and called for an upward push (BTC was at ~$112k). Followed by a meaningful HTF push. **Lesson:** uses spot CVD/orderbook delta flips as the trigger to fade weakness.

5. **Sep 19 2025 — Weekly open + FVG defense post.** Identified $115,219 weekly open as the pivot, with $113,355 daily FVG as the next downside target if lost. *"losing the weekly open would likely trigger a price decline to $113,355 because such inefficiencies eventually get filled."*

6. **Aug 9 2025 — Monthly open flip trade.** Called bullish bias because BTC flipped $115,752 monthly open into support; flagged $120k as the next 2-week liquidation magnet aligned with prior weekly open at $119,414. Called the path correctly into the late-summer rally toward $124k ATH.

7. **July 26 2025 — "Two scenarios" weekly playbook.** Scenario 1 (favored): higher low after sweeping liquidity at $116k. Scenario 2 (less likely): aggressive double sweep of $114,800 wick low. Invalidation: failure to hold above wick lows → drop to $112k–$113.8k imbalance. Classic example of his weekly post format.

### 1.6 Risk management

- **Position size:** 10–15% of portfolio per HTF swing.
- **Leverage:** 2.5–3x cross margin (HTF swings); 3–4x recommended for users (NEVER 10x even on 4–5% range setups).
- **Cross > isolated.** Quote: *"Cross margin allows me to absorb volatility without emotional reaction."*
- **Defined liquidation distance.** Sets liquidation 40%+ from entry. Treats the liquidation level as the actual stop, with the conventional SL as a softer trigger.
- **SL discipline by timeframe close.** Weekly-close-based invalidation for HTF swings (not intraday wicks). Will move SL UP as price moves against, but treats weekly close above SL as full invalidation.
- **R:R framing:** asymmetric — willing to risk 10–15% of capital to capture a 30–50% expected move.
- **Patience as edge.** Quote: *"Trading is about trusting your system and respecting your probabilities."* and *"My strategy is built on data, not hope."*

### 1.7 Frequency

- **~1–3 high-effort posts/day**, plus QT/replies. Heavier output around weekly/monthly opens.
- **Format:** mostly long-form market structure analysis with annotated chart screenshots. Not a high-frequency signal-caller.
- **Role:** **educator + setup-caller hybrid.** Sells signals indirectly via ScalpX subscription; X is the marketing/lead-gen funnel.

---

## 2. zorathzzz — `@zorathzzz`

### 2.1 Bio / background

**No evidence found.** Searches across Exa neural search, WebSearch (Google), Nitter mirrors (blocked by anti-bot), Threadreader, Rattibha, Typefully, twstalker, social-blade, web3.bio, and direct X fetch returned **zero** results matching this exact handle in a crypto-trading context. Closest hits were unrelated:
- A fantasy/D&D character "Zorath"
- A WoW character on Muradin server
- LoL summoners
- A devops tool `zorath-env`
- Farcaster handle `zoratrx` (different spelling, no trading content)

### 2.2 Trading style summary

**No evidence found.** Cannot characterise without verified posts.

### 2.3 Per-timeframe approach

**No evidence found.**

### 2.4 Key indicators / signals

**No evidence found.**

### 2.5 Entry/exit pattern examples

**No evidence found.**

### 2.6 Risk management

**No evidence found.**

### 2.7 Frequency

**No evidence found.**

### What to do about this gap

The handle may be:
1. **Spelt slightly differently** on the actual profile (e.g., `Zorath_zzz`, `zorathzz`, `zorath0x`, `zoraxbt`). Worth re-verifying the spelling by opening x.com manually.
2. **Private / protected account.** No public archives can scrape it.
3. **A small, recently-created account** with <500 followers and no third-party coverage.
4. **Recently renamed.** X handles can change; old archives may be under a previous name.

**Recommended next step for the user:** open the profile in a logged-in browser, screenshot the bio + pinned tweet + last 20 posts, and paste back. With those raw inputs the same study-guide structure can be filled in for zorathzzz in a follow-up pass.

---

## 3. Synthesis

### 3.1 What this user (fib + perp-metrics trader) should learn from KillaXBT

Most of KillaXBT's edge maps directly onto your existing dashboard. Concrete pickups:

- **Liquidation heatmap as a primary input, not an afterthought.** Coinglass 7-day vs 30-day heatmaps. Read both sides (long vs short clusters) and trade the asymmetry into the larger one. Your dashboard already has OI/funding — adding a Coinglass-style liquidation overlay would be the highest-leverage additional signal.
- **Spot CVD vs perp CVD divergence framing.** The user's stack already pulls CVD; Killa's actionable insight is *"flipping green during a drop = HTF buy signal"*. Code that as an alert: spot CVD slope > 0 while price slope < 0 over rolling 4H = candidate long.
- **Monthly/weekly open as fib-anchor.** The user uses fib retracements (0.7816 / 0.75 for BTC, 0.618/0.5/0.382/0.25 for everything else). KillaXBT's parallel concept is the **monthly open** as a flippable pivot. **Try anchoring fib swings to the prior monthly open or monthly high/low** rather than arbitrary swing points. This is a direct enhancement, not a replacement.
- **CME gap fills as a static target list.** 98% historical fill rate is too good to ignore. For BTC specifically, maintain a list of unfilled CME gaps and use them as TP magnets after a fib-retracement long fires.
- **Fair Value Gaps on the daily.** ICT-style 3-candle FVGs on the daily timeframe pair extremely well with fib golden zones. Often the FVG midpoint *is* the 0.5 / 0.618 of the impulse move that created it. Worth backtesting a "FVG midpoint + fib confluence" rule.
- **Cycle-decay as a portfolio-level overlay.** Killa's 3.25x current-cycle multiple is debatable, but the **principle** of weighting your gross long exposure by where you are in the cycle is sound. At minimum, gate your max long size on whether BTC monthly is making higher highs vs lower highs.
- **"Mechanical 2–3 week corrections" rule of thumb.** Use this as a duration filter — if a perceived "correction" has lasted >3 weeks, raise the probability that it's a trend change, not noise.

**Free resources he uses / endorses:**
- **Coinglass** (liquidation maps, OI, funding) — this is his primary data source.
- **CME futures chart** (for gaps) — TradingView ticker `CME:BTC1!`.
- His own X feed and the [OKX Feed](https://www.okx.com/en-ae/feed/post/57265338760384) re-publishes.
- ScalpX paid Discord/community (paid; not necessary for someone who already has their own framework).
- Implicitly draws on **ICT/Inner Circle Trader** vocabulary (FVG, OB, liquidity sweeps, OTE) — see [SignalWavesAI ICT guide](https://signalwavesai.com/articles/ict-trading-strategy) for the full lexicon. Notably ICT's **OTE entry zone is 0.62–0.79** which overlaps directly with the user's BTC fib levels of 0.75 and 0.7816.

**Books / accounts referenced (none directly cited by Killa publicly), but the methodology overlaps with:**
- ICT (Michael J. Huddleston) — order blocks, FVG, killzones
- Wyckoff method (accumulation/distribution phases)
- The "Diminishing Cycles" framework popularised by [Avramescu's BDRT](https://www.avramescu.net/bitcoins-diminishing-monthly-returns-a-decade-ahead/)

### 3.2 What to learn from zorathzzz

**No evidence found.** Cannot recommend until the account's content can be verified.

### 3.3 Side-by-side comparison

| Dimension | KillaXBT | zorathzzz |
|---|---|---|
| Public footprint | Very high (180k followers, frequent news quotes) | None found |
| Primary asset | BTC (≥95%) | Unknown |
| Time horizon | HTF swings (weeks–months) + weekly setup posts | Unknown |
| Core indicators | Liquidation maps, FVG, CME gaps, monthly/weekly opens, orderbook delta, 111-day SMA, cycle decay | Unknown |
| Posting frequency | 1–3 long-form posts/day | Unknown |
| Risk approach | 2.5–3x cross, 10–15% sized, weekly-close SL invalidation | Unknown |
| Monetisation | ScalpX paid signals + Bitunix affiliate | Unknown |

**Not a meaningful comparison until zorathzzz's content can be sourced.** Treating this as if it were a real comparison would mean inventing data.

### 3.4 Concrete "to become like KillaXBT" study path (ranked)

Tailored for someone who already has fib + OI + funding + CVD on Binance/Bybit:

1. **Add a Coinglass liquidation heatmap pane to the dashboard** (or open it in a side-by-side window). Read 7d and 30d simultaneously. Mark dense clusters as TP/SL targets. **This is the single biggest gap to close.**
2. **Add CME futures BTC chart and tag every weekend gap.** Maintain a "live CME gaps" list as TP candidates.
3. **Backtest fib levels anchored to the prior monthly open instead of arbitrary swings.** Compare hit-rate against the current implementation. Hypothesis: fib confluence with monthly open clusters produces tighter stops.
4. **Implement spot-CVD vs perp-CVD divergence alerting.** Trigger: rolling 4H spot CVD slope opposite to price slope. Killa explicitly trades this.
5. **Mark daily FVGs as a chart overlay** (3-candle imbalance gaps). Test rule: long when fib 0.5–0.618 zone overlaps an unfilled bullish daily FVG.
6. **Add 111-day SMA to BTC chart** as a binary trend filter. Below = no longs / reduce long size.
7. **Adopt the "weekly close" stop rule** for HTF swings — stop using intraday SLs for swings; use the weekly close above/below the invalidation level.
8. **Track every monthly open** as a flippable pivot. Above monthly open = bullish bias; below = bearish bias.
9. **Reduce leverage on small-range setups.** Killa's max-3-4x rule on 4–5% range setups is a reasonable guard against forced liquidations.
10. **Build a personal "scenarios" template.** Each Sunday evening, write your own "Scenario 1 / Scenario 2 / Invalidation" weekly plan using KillaXBT's format — discipline forcing function.

**Daily habits to copy:**
- Sunday evening: write the next week's scenario plan in two short paragraphs (favored + alternative + invalidation).
- Monday + Friday: check funding rate extremes and OI delta at session opens.
- Anytime BTC rallies on weekend: flag the resulting CME gap as a magnet.
- Monthly close: re-check whether monthly open flipped to support/resistance and rebias.

---

## Sources

### KillaXBT
- [Bitcoinist — Bulls In Control, $120k Test (Aug 2025)](https://bitcoinist.com/bitcoin-bulls-in-control-120000-test-run-toward-ath)
- [TradingView/NewsBTC — Liquidation Traps Both Sides (June 2025)](https://www.tradingview.com/news/newsbtc:cde896c5d094b:0-bitcoin-in-stalemate-with-liquidation-traps-on-both-sides-of-the-market/)
- [TradingView/NewsBTC — Ideal Long Zone, 2 Scenarios (July 2025)](https://www.tradingview.com/news/newsbtc:2b1b0a8bd094b:0-bitcoin-bulls-gain-traction-from-ideal-long-zone-2-scenarios-for-the-week-ahead/)
- [TradingView/NewsBTC — Weekly Open + FVG (Sept 2025)](https://www.tradingview.com/news/newsbtc:4ca45765c094b:0-bitcoin-tests-weekly-open-as-113-300-fair-value-gap-looms-what-it-means/)
- [TradingView/NewsBTC — Sweep Before Upswing (Nov 2025)](https://www.tradingview.com/news/newsbtc:55641d0e9094b:0-bitcoin-market-structure-signals-potential-sweep-before-upswing-details/)
- [InvestX — Orderbook Delta Flip (Oct 2025)](https://investx.fr/en/crypto-news/bitcoin-on-the-verge-of-exploding-to-new-ath-the-signal-that-never-fails/)
- [XT.com — CME Gap Fill 98% (Aug 2025)](https://www.xt.com/en/blog/post/bitcoin-8-below-cme-gap-ahead-of-monthly-close-will-history-repeat)
- [BitcoinEthereumNews — "Easiest 2 years" + Whale Activity (Mar 2026)](https://bitcoinethereumnews.com/bitcoin/bitcoin-whale-activity-hits-six-year-high-as-retail-participation-stays-near-cycle-lows/)
- [Coincu — $84k CME Gap Bearish Post (Mar 2026)](https://coincu.com/markets/bitcoin-84000-cme-gap/)
- [Yahoo Finance — Top Caller Now Bottom Caller (Feb 2026)](https://finance.yahoo.com/news/analyst-nailed-bitcoin-price-top-180733566.html)
- [TradingView/NewsBTC — Diminishing Cycle Bottom Math (April 2026)](https://www.tradingview.com/news/newsbtc:a5832a4ca094b:0-analyst-who-called-bitcoin-s-top-correctly-now-predicting-the-bottom/)
- [Bitcoinist — Diminishing Cycle Sets Bottom (April 2026)](https://bitcoinist.com/bitcoin-top-above-120000/)
- [CoinLive — SL Adjusted to $83k (April 22 2026)](https://www.coinlive.com/id/news-flash/1094321)
- [Phemex News — Shorted at $74,688, SL $80k (April 15 2026)](https://phemex.com/news/article/trader-killa-shorts-bitcoin-at-74688-sets-stoploss-at-80000-73299)
- [ChainCatcher — Shorted at $74,688 (April 15 2026)](https://www.chaincatcher.com/en/article/2258782)
- [RootData — $84k CME Gap analysis](https://www.rootdata.com/news/610934)
- [Gate News — 111-day SMA reversal call (April 23 2026)](https://www.gate.com/news/detail/trader-killa-says-bitcoin-needs-to-hold-above-111-day-sma-to-confirm-trend-20528346)
- [Phemex News — May 5 reversal pattern (May 1 2026)](https://phemex.com/news/article/trader-highlights-bitcoins-monthly-reversal-pattern-on-5th-77848)
- [OKX Feed — Cycles Update / My Plan post](https://www.okx.com/en-ae/feed/post/57265338760384)
- [BTCC ES — Rotational market mathematics writeup](https://www.btcc.com/es-ES/square/XRPX3/1533456)
- [PANews — Comparison of cycle-prediction methodologies (KillaXBT included)](https://www.panewslab.com/en/articles/019ce614-4cd9-746e-b3e9-a59444b0cdd3)
- [ScalpX — trading desk Killa is part of](https://scalpxtrades.com/)
- [Twicopy follower-graph snapshot of bio](https://twicopy.com/lifeof100x/following)
- [CryptoBenelux — long call at $104k (June 2025)](https://cryptobenelux.com/2025/06/02/bitcoin-zakt-na-recordhoogte-maar-analist-killaxbt-ziet-nieuwe-bullrun-long-bij-104-000/)

### Methodology context
- [SignalWavesAI — ICT Trading Strategy 2025](https://signalwavesai.com/articles/ict-trading-strategy)
- [Avramescu — Bitcoin Diminishing Monthly Returns](https://www.avramescu.net/bitcoins-diminishing-monthly-returns-a-decade-ahead/)
- [ChartWhisperer — CVD Guide](https://chartwhisperer.ca/blog/cumulative-volume-delta-cvd-crypto-trading-guide)
- [Kalena — CVD Bitcoin 14-month dataset](https://blog.kalena.ai/cumulative-volume-delta-bitcoin-what-14-months-of-btc-specific-data-revealed-about-the-indicator-most-traders-apply-wrong)
- [trdr.io — Spot vs Perp CVD documentation](https://docs.trdr.io/key-features-and-indicators/volume-indicators/cumulative-volume-delta-cvd)
- [BullCryptoSignals — Fibonacci Golden Zone + FVG Strategy](https://bullcryptosignals.com/blog/fibonacci-golden-zone-fair-value-gap-strategy/)
- [MindMathMoney — Golden Zone Fibonacci](https://www.mindmathmoney.com/articles/youve-been-using-fibonacci-trading-wrong-heres-the-golden-zone-strategy-that-actually-works)

### zorathzzz
**No verifiable sources found.** All search avenues exhausted (Exa neural, WebSearch, multiple Nitter mirrors, Threadreader, Rattibha, Typefully, twstalker, web3.bio, direct X fetch). Section left blank pending the user providing screenshots or a corrected handle spelling.
