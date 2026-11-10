#!/usr/bin/env python3
"""
Compare annualized price volatility across assets.

Peers (BTC, ETH, XMR) and a Zcash cross-check are computed from the daily price
histories in data/ (standard realized vol: stdev of daily log returns, annualized
by sqrt(365)). Zcash's published 30/90-day annualized volatility series is ingested
from an Artemis export and saved to data/zec_volatility.csv.

Run after fetch_market_data.py.
"""

import csv
import math
import os

DATA = os.path.join(os.path.dirname(__file__), "..", "data")
DOWNLOADS = os.path.expanduser("~/Downloads")


def read_prices(sym):
    path = os.path.join(DATA, "%s_market_history.csv" % sym)
    seen = {}
    for row in csv.DictReader(open(path)):
        seen[row["date"]] = float(row["price_usd"])  # dedupe by date, keep last
    return [price for _, price in sorted(seen.items())]


def ann_vol(prices, window):
    p = prices[-(window + 1):]
    rets = [math.log(p[i] / p[i - 1]) for i in range(1, len(p)) if p[i - 1] > 0]
    if len(rets) < 2:
        return None
    mean = sum(rets) / len(rets)
    var = sum((r - mean) ** 2 for r in rets) / (len(rets) - 1)
    return math.sqrt(var) * math.sqrt(365) * 100


def artemis_series(name):
    rows = list(csv.reader(open(os.path.join(DOWNLOADS, name))))[1:]
    return {r[0]: float(r[1]) * 100 for r in rows if len(r) == 2}


def main():
    compare = []
    for sym in ["zec", "xmr", "btc", "eth"]:
        prices = read_prices(sym)
        compare.append([sym.upper(), round(ann_vol(prices, 30), 1), round(ann_vol(prices, 90), 1)])

    with open(os.path.join(DATA, "volatility_compare.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["asset", "vol_30d_pct", "vol_90d_pct"])
        w.writerows(compare)

    print("Annualized volatility, computed from daily prices (trailing window):")
    for row in compare:
        print("  %-4s 30d %6.1f%%   90d %6.1f%%" % (row[0], row[1], row[2]))

    # Ingest Zcash's own Artemis volatility series and cross-check the latest value.
    try:
        v30, v90 = artemis_series("30-Day ANN Volatility.csv"), artemis_series("90-Day ANN Volatility.csv")
        dates = sorted(v90)
        with open(os.path.join(DATA, "zec_volatility.csv"), "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["date", "vol_30d_pct", "vol_90d_pct"])
            for d in dates:
                w.writerow([d, round(v30.get(d, 0), 1) or "", round(v90[d], 1)])
        print("Artemis ZEC latest: 30d %.1f%%  90d %.1f%% (cross-check vs computed above)"
              % (v30[dates[-1]], v90[dates[-1]]))
        print("wrote data/zec_volatility.csv")
    except FileNotFoundError:
        print("Artemis export not found in ~/Downloads; skipped zec_volatility.csv")

    print("wrote data/volatility_compare.csv")


if __name__ == "__main__":
    main()
