// Fib Tracker — frontend
// Reads ../data/state.json (committed by GitHub Actions every 5 min) and renders
// the selected coin/exchange/timeframe with candles, fib lines, and live stats.

const STATE_URL = "../data/state.json";
const TIMEFRAMES = ["15m", "30m", "1h", "4h", "1D", "1W"];

const ui = {
  coin: "BTC",
  exchange: "binance",
  tf: "1h",
};

let state = null;
let chart = null;
let candleSeries = null;
let priceLines = [];

async function loadState() {
  const r = await fetch(STATE_URL + "?t=" + Date.now(), { cache: "no-store" });
  if (!r.ok) throw new Error("state fetch failed");
  state = await r.json();
}

function fmtUsd(n) {
  if (n == null || isNaN(n)) return "—";
  if (n >= 1e9) return "$" + (n / 1e9).toFixed(2) + "B";
  if (n >= 1e6) return "$" + (n / 1e6).toFixed(2) + "M";
  if (n >= 1e3) return "$" + (n / 1e3).toFixed(2) + "K";
  return "$" + n.toFixed(2);
}
function fmtPct(n) {
  if (n == null || isNaN(n)) return "—";
  return (n * 100).toFixed(4) + "%";
}
function fmtNum(n) {
  if (n == null || isNaN(n)) return "—";
  return n.toLocaleString(undefined, { maximumFractionDigits: 2 });
}
function fmtTime(ts) {
  if (!ts) return "—";
  return new Date(ts).toLocaleString();
}

function buildCoinTabs() {
  const row = document.getElementById("coin-tabs");
  const coins = Object.keys(state?.coins || {});
  // Preserve order from a known list, then append any extras.
  const order = ["BTC", "ETH", "SOL", "TAO", "ZEC", "ENA", "LTC", "HYPE"];
  const ordered = order.filter(c => coins.includes(c)).concat(coins.filter(c => !order.includes(c)));
  row.innerHTML = "";
  for (const c of ordered) {
    const b = document.createElement("button");
    b.textContent = c;
    if (c === ui.coin) b.classList.add("active");
    b.onclick = () => { ui.coin = c; ensureExchangeAvailable(); render(); };
    row.appendChild(b);
  }
}

function buildTfToggle() {
  const wrap = document.getElementById("tf-toggle");
  wrap.innerHTML = "";
  for (const tf of TIMEFRAMES) {
    const b = document.createElement("button");
    b.textContent = tf;
    if (tf === ui.tf) b.classList.add("active");
    b.onclick = () => { ui.tf = tf; render(); };
    wrap.appendChild(b);
  }
}

function bindExchangeToggle() {
  document.querySelectorAll("#exchange-toggle button").forEach(btn => {
    btn.onclick = () => {
      ui.exchange = btn.dataset.x;
      document.querySelectorAll("#exchange-toggle button").forEach(b =>
        b.classList.toggle("active", b === btn));
      render();
    };
  });
}

function ensureExchangeAvailable() {
  // If current exchange has no data for selected coin, fall back to the other.
  const node = state?.coins?.[ui.coin];
  if (!node) return;
  if (!node[ui.exchange]) {
    const other = ui.exchange === "binance" ? "bybit" : "binance";
    if (node[other]) {
      ui.exchange = other;
      document.querySelectorAll("#exchange-toggle button").forEach(b =>
        b.classList.toggle("active", b.dataset.x === ui.exchange));
    }
  }
}

function ensureChart() {
  if (chart) return;
  const el = document.getElementById("chart");
  chart = LightweightCharts.createChart(el, {
    layout: { background: { color: "#151821" }, textColor: "#e6e8ee" },
    grid:   { vertLines: { color: "#1d212c" }, horzLines: { color: "#1d212c" } },
    timeScale: { timeVisible: true, secondsVisible: false, borderColor: "#232733" },
    rightPriceScale: { borderColor: "#232733" },
    crosshair: { mode: 0 },
    autoSize: true,
  });
  candleSeries = chart.addCandlestickSeries({
    upColor: "#2ecc71", downColor: "#e74c3c",
    borderUpColor: "#2ecc71", borderDownColor: "#e74c3c",
    wickUpColor: "#2ecc71", wickDownColor: "#e74c3c",
  });
  window.addEventListener("resize", () => chart.applyOptions({}));
}

function clearPriceLines() {
  for (const pl of priceLines) candleSeries.removePriceLine(pl);
  priceLines = [];
}

function render() {
  buildCoinTabs();
  buildTfToggle();

  const node = state?.coins?.[ui.coin]?.[ui.exchange];
  // Disable the exchange button if the current coin doesn't have it.
  document.querySelectorAll("#exchange-toggle button").forEach(b => {
    const has = state?.coins?.[ui.coin]?.[b.dataset.x];
    b.disabled = !has;
  });

  document.getElementById("updated").textContent =
    state?.updated_ts ? "updated " + fmtTime(state.updated_ts) : "no data yet";

  if (!node) {
    document.getElementById("s-oi").textContent = "—";
    document.getElementById("s-funding").textContent = "—";
    document.getElementById("s-next").textContent = "—";
    document.getElementById("s-cvd").textContent = "—";
    document.getElementById("s-price").textContent = "—";
    document.querySelector("#fills-table tbody").innerHTML = "";
    return;
  }

  document.getElementById("s-oi").textContent = fmtUsd(node.oi_usd);
  const f = node.funding_rate;
  const fEl = document.getElementById("s-funding");
  fEl.textContent = fmtPct(f);
  fEl.className = f > 0 ? "pos" : (f < 0 ? "neg" : "");
  document.getElementById("s-next").textContent = fmtTime(node.next_funding_ts);
  document.getElementById("s-cvd").textContent = fmtNum(node.cvd);
  document.getElementById("s-price").textContent = fmtNum(node.mark_price);

  ensureChart();
  const tfNode = node.timeframes?.[ui.tf];
  if (!tfNode || !tfNode.candles) {
    candleSeries.setData([]);
    clearPriceLines();
    document.querySelector("#fills-table tbody").innerHTML = "";
    return;
  }

  candleSeries.setData(tfNode.candles.map(c => ({
    time: Math.floor(c.ts / 1000),
    open: c.o, high: c.h, low: c.l, close: c.c,
  })));

  clearPriceLines();
  const filledRatios = new Set((tfNode.filled || []).map(x => x.ratio));
  if (tfNode.levels) {
    for (const [ratio, price] of Object.entries(tfNode.levels)) {
      const isFilled = filledRatios.has(parseFloat(ratio));
      priceLines.push(candleSeries.createPriceLine({
        price,
        color: isFilled ? "#f5c518" : "#4f8cff",
        lineWidth: isFilled ? 2 : 1,
        lineStyle: isFilled ? 0 : 2, // solid if filled, dashed if open
        axisLabelVisible: true,
        title: `fib ${ratio}${isFilled ? " ✓" : ""}`,
      }));
    }
  }

  // Swing line: draw start and end as price lines too
  if (tfNode.swing_start && tfNode.swing_end) {
    priceLines.push(candleSeries.createPriceLine({
      price: tfNode.swing_start.price, color: "#8a93a6",
      lineWidth: 1, lineStyle: 1, axisLabelVisible: false,
      title: `swing ${tfNode.swing_start.kind}`,
    }));
    priceLines.push(candleSeries.createPriceLine({
      price: tfNode.swing_end.price, color: "#8a93a6",
      lineWidth: 1, lineStyle: 1, axisLabelVisible: false,
      title: `swing ${tfNode.swing_end.kind}`,
    }));
  }

  // Fills table
  const tbody = document.querySelector("#fills-table tbody");
  tbody.innerHTML = "";
  const ratiosSorted = Object.keys(tfNode.levels || {})
    .map(parseFloat).sort((a, b) => b - a);
  for (const r of ratiosSorted) {
    const price = tfNode.levels[r];
    const fill = (tfNode.filled || []).find(x => x.ratio === r);
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${r}</td>
      <td>${fmtNum(price)}</td>
      <td class="${fill ? "tag-filled" : "tag-open"}">${fill ? "FILLED" : "open"}</td>
      <td>${fill ? fmtTime(fill.ts) : "—"}</td>
    `;
    tbody.appendChild(tr);
  }
}

document.getElementById("refresh").onclick = async (e) => {
  e.preventDefault();
  await loadState();
  render();
};

(async () => {
  bindExchangeToggle();
  try {
    await loadState();
  } catch (e) {
    console.error(e);
    state = { coins: {} };
  }
  render();
  // Auto-refresh every 60s in the browser (state file refreshes every 5 min on the server)
  setInterval(async () => {
    try { await loadState(); render(); } catch (e) { console.error(e); }
  }, 60_000);
})();
