// Fib Tracker — frontend
// Reads data/state.json (committed by GitHub Actions every 5 min) and renders
// the selected coin/exchange/timeframe with candles, fib lines, swing line,
// fill markers, and an optional CVD indicator pane.

const STATE_URL = "data/state.json";
const TIMEFRAMES = ["15m", "30m", "1h", "4h", "1D", "1W"];
const LWC = LightweightCharts;

const ui = {
  coin: "BTC",
  exchange: "binance",
  tf: "1h",
  showCvd: false,
};

let state = null;

// Price chart
let chart = null;
let candleSeries = null;
let priceLines = [];
let swingSeries = null;

// CVD chart
let cvdChart = null;
let cvdSeries = null;

async function loadState() {
  const r = await fetch(STATE_URL + "?t=" + Date.now(), { cache: "no-store" });
  if (!r.ok) throw new Error("state fetch failed");
  state = await r.json();
}

const fmtUsd = n => n == null || isNaN(n) ? "—"
  : n >= 1e9 ? "$" + (n / 1e9).toFixed(2) + "B"
  : n >= 1e6 ? "$" + (n / 1e6).toFixed(2) + "M"
  : n >= 1e3 ? "$" + (n / 1e3).toFixed(2) + "K"
  : "$" + n.toFixed(2);
const fmtPct = n => n == null || isNaN(n) ? "—" : (n * 100).toFixed(4) + "%";
const fmtNum = n => n == null || isNaN(n) ? "—" : n.toLocaleString(undefined, { maximumFractionDigits: 2 });
const fmtTime = ts => !ts ? "—" : new Date(ts).toLocaleString();

function buildCoinTabs() {
  const row = document.getElementById("coin-tabs");
  const coins = Object.keys(state?.coins || {});
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

function bindCvdToggle() {
  const btn = document.getElementById("cvd-toggle");
  btn.onclick = () => {
    ui.showCvd = !ui.showCvd;
    btn.classList.toggle("active", ui.showCvd);
    btn.textContent = ui.showCvd ? "− CVD" : "+ CVD";
    document.getElementById("cvd-wrap").style.display = ui.showCvd ? "block" : "none";
    if (ui.showCvd) renderCvd();
  };
}

function ensureExchangeAvailable() {
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

function ensurePriceChart() {
  if (chart) return;
  const el = document.getElementById("chart");
  chart = LWC.createChart(el, {
    layout: { background: { color: "#151821" }, textColor: "#e6e8ee" },
    grid:   { vertLines: { color: "#1d212c" }, horzLines: { color: "#1d212c" } },
    timeScale: { timeVisible: true, secondsVisible: false, borderColor: "#232733" },
    rightPriceScale: { borderColor: "#232733", autoScale: true },
    crosshair: { mode: 0 },
    autoSize: true,
  });
  candleSeries = chart.addCandlestickSeries({
    upColor: "#2ecc71", downColor: "#e74c3c",
    borderUpColor: "#2ecc71", borderDownColor: "#e74c3c",
    wickUpColor: "#2ecc71", wickDownColor: "#e74c3c",
  });
}

function ensureCvdChart() {
  if (cvdChart) return;
  const el = document.getElementById("cvd-chart");
  cvdChart = LWC.createChart(el, {
    layout: { background: { color: "#151821" }, textColor: "#e6e8ee" },
    grid:   { vertLines: { color: "#1d212c" }, horzLines: { color: "#1d212c" } },
    timeScale: { timeVisible: true, secondsVisible: false, borderColor: "#232733" },
    rightPriceScale: { borderColor: "#232733", autoScale: true },
    crosshair: { mode: 0 },
    autoSize: true,
  });
  cvdSeries = cvdChart.addLineSeries({
    color: "#4f8cff", lineWidth: 2, priceLineVisible: false, lastValueVisible: true,
  });
}

function clearOverlays() {
  for (const pl of priceLines) candleSeries.removePriceLine(pl);
  priceLines = [];
  if (swingSeries) {
    chart.removeSeries(swingSeries);
    swingSeries = null;
  }
  candleSeries.setMarkers([]);
}

function renderPriceChart(node, tfNode) {
  ensurePriceChart();

  // 1. Candles — set first so the time axis is established.
  const candles = (tfNode.candles || []).map(c => ({
    time: Math.floor(c.ts / 1000),
    open: c.o, high: c.h, low: c.l, close: c.c,
  }));
  candleSeries.setData(candles);

  clearOverlays();

  // 2. Fib horizontal price lines.
  const filledRatios = new Set((tfNode.filled || []).map(x => x.ratio));
  if (tfNode.levels) {
    for (const [ratio, price] of Object.entries(tfNode.levels)) {
      const isFilled = filledRatios.has(parseFloat(ratio));
      priceLines.push(candleSeries.createPriceLine({
        price,
        color: isFilled ? "#f5c518" : "#4f8cff",
        lineWidth: isFilled ? 2 : 1,
        lineStyle: isFilled ? 0 : 2, // solid when filled, dashed when open
        axisLabelVisible: true,
        title: `fib ${ratio}${isFilled ? " ✓" : ""}`,
      }));
    }
  }

  // 3. Diagonal swing line from start pivot → end pivot (the "fib drag").
  if (tfNode.swing_start && tfNode.swing_end && candles.length > 0) {
    const firstCandleTime = candles[0].time;
    const lastCandleTime  = candles[candles.length - 1].time;
    const startTime = Math.max(Math.floor(tfNode.swing_start.ts / 1000), firstCandleTime);
    const endTime   = Math.min(Math.floor(tfNode.swing_end.ts   / 1000), lastCandleTime);
    if (endTime > startTime) {
      swingSeries = chart.addLineSeries({
        color: "#8a93a6", lineWidth: 2, lineStyle: 2,
        priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false,
      });
      swingSeries.setData([
        { time: startTime, value: tfNode.swing_start.price },
        { time: endTime,   value: tfNode.swing_end.price },
      ]);
    }
  }

  // 4. Markers on candles where fills happened (only those within the visible window).
  if (tfNode.filled && candles.length > 0) {
    const firstTime = candles[0].time;
    const lastTime  = candles[candles.length - 1].time;
    const direction = tfNode.direction;
    const markers = (tfNode.filled || [])
      .filter(f => !f.backfilled)  // don't mark historical seed fills
      .map(f => ({
        time: Math.floor(f.ts / 1000),
        position: direction === "up" ? "belowBar" : "aboveBar",
        color: "#f5c518",
        shape: direction === "up" ? "arrowUp" : "arrowDown",
        text: `${f.ratio}`,
      }))
      .filter(m => m.time >= firstTime && m.time <= lastTime)
      .sort((a, b) => a.time - b.time);
    if (markers.length) candleSeries.setMarkers(markers);
  }

  // 5. CRITICAL: re-enable autoScale + fitContent so switching coin/tf rescales.
  chart.priceScale("right").applyOptions({ autoScale: true });
  chart.timeScale().fitContent();
}

function renderCvd() {
  if (!ui.showCvd) return;
  ensureCvdChart();
  const node = state?.coins?.[ui.coin]?.[ui.exchange];
  const hist = node?.cvd_history || [];
  cvdSeries.setData(hist.map(p => ({
    time: Math.floor(p.ts / 1000),
    value: p.cvd,
  })));
  cvdChart.priceScale("right").applyOptions({ autoScale: true });
  cvdChart.timeScale().fitContent();
}

function render() {
  buildCoinTabs();
  buildTfToggle();

  const node = state?.coins?.[ui.coin]?.[ui.exchange];
  document.querySelectorAll("#exchange-toggle button").forEach(b => {
    b.disabled = !state?.coins?.[ui.coin]?.[b.dataset.x];
  });

  document.getElementById("updated").textContent =
    state?.updated_ts ? "updated " + fmtTime(state.updated_ts) : "no data yet";

  if (!node) {
    ["s-oi","s-funding","s-next","s-cvd","s-price"].forEach(id =>
      document.getElementById(id).textContent = "—");
    document.querySelector("#fills-table tbody").innerHTML = "";
    return;
  }

  document.getElementById("s-oi").textContent = fmtUsd(node.oi_usd);
  const fEl = document.getElementById("s-funding");
  fEl.textContent = fmtPct(node.funding_rate);
  fEl.className = node.funding_rate > 0 ? "pos" : (node.funding_rate < 0 ? "neg" : "");
  document.getElementById("s-next").textContent  = fmtTime(node.next_funding_ts);
  document.getElementById("s-cvd").textContent   = fmtNum(node.cvd);
  document.getElementById("s-price").textContent = fmtNum(node.mark_price);

  const tfNode = node.timeframes?.[ui.tf];
  if (!tfNode || !tfNode.candles) {
    ensurePriceChart();
    candleSeries.setData([]);
    clearOverlays();
    document.querySelector("#fills-table tbody").innerHTML = "";
    return;
  }

  renderPriceChart(node, tfNode);
  if (ui.showCvd) renderCvd();

  // Fills table
  const tbody = document.querySelector("#fills-table tbody");
  tbody.innerHTML = "";
  const ratios = Object.keys(tfNode.levels || {}).map(parseFloat).sort((a, b) => b - a);
  for (const r of ratios) {
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
  bindCvdToggle();
  try { await loadState(); }
  catch (e) { console.error(e); state = { coins: {} }; }
  render();
  setInterval(async () => {
    try { await loadState(); render(); } catch (e) { console.error(e); }
  }, 60_000);
})();
