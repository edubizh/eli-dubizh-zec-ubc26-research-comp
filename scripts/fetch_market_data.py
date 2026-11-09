#!/usr/bin/env python3
"""
Fetch free, public market data for the Zcash short thesis.

Sources (all free, no API key required):
  - CoinGecko public API: price, market cap and daily history for ZEC and XMR.

Writes dated CSVs into ../data so every figure in the report is reproducible
and can be refreshed before submission. Authoritative fundamentals that
CoinGecko does not carry (network REV, shielded supply) are pulled separately
from Blockworks and recorded in data/key_figures.csv.

Usage:
    python3 scripts/fetch_market_data.py
"""

import csv
import json
import os
import time
import urllib.request
from datetime import datetime, timezone

API = "https://api.coingecko.com/api/v3"
COINS = {"zcash": "ZEC", "monero": "XMR"}
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")


def get(url):
    """Simple GET with a browser-like header and one retry on rate limit."""
    for attempt in range(2):
        req = urllib.request.Request(url, headers={"User-Agent": "research-comp/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as err:
            if err.code == 429 and attempt == 0:
                time.sleep(20)
                continue
            raise
    return None


def write_csv(name, header, rows):
    os.makedirs(DATA_DIR, exist_ok=True)
    path = os.path.join(DATA_DIR, name)
    with open(path, "w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(header)
        writer.writerows(rows)
    print("wrote %s (%d rows)" % (os.path.relpath(path), len(rows)))


def fetch_current():
    ids = ",".join(COINS)
    data = get("%s/simple/price?ids=%s&vs_currencies=usd"
               "&include_market_cap=true&include_24hr_vol=true" % (API, ids))
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    rows = []
    for coin, symbol in COINS.items():
        d = data.get(coin, {})
        rows.append([today, symbol,
                     d.get("usd"), d.get("usd_market_cap"), d.get("usd_24h_vol")])
    write_csv("market_current.csv",
              ["as_of", "symbol", "price_usd", "market_cap_usd", "volume_24h_usd"], rows)


def fetch_history(coin, symbol):
    # The free CoinGecko tier serves up to 365 days of daily history without a key.
    data = get("%s/coins/%s/market_chart?vs_currency=usd&days=365&interval=daily"
               % (API, coin))
    prices = {int(ts // 1000): price for ts, price in data.get("prices", [])}
    caps = dict((int(ts // 1000), cap) for ts, cap in data.get("market_caps", []))
    rows = []
    for ts in sorted(prices):
        day = datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d")
        rows.append([day, round(prices[ts], 4), round(caps.get(ts, 0), 2)])
    write_csv("%s_market_history.csv" % symbol.lower(),
              ["date", "price_usd", "market_cap_usd"], rows)


def main():
    fetch_current()
    for coin, symbol in COINS.items():
        time.sleep(8)  # stay under the free rate limit
        fetch_history(coin, symbol)


if __name__ == "__main__":
    main()
