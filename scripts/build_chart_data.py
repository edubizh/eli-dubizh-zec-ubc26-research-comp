#!/usr/bin/env python3
"""
Turn the raw daily price history into a small, chart-ready file for the report.

Reads data/zec_market_history.csv and writes data/zec_price_chart.csv with a
numeric decimal-year x column (so pgfplots can plot it without a date library),
sampled weekly to keep the line clean. Run after fetch_market_data.py.
"""

import csv
import os
from datetime import datetime

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
SRC = os.path.join(DATA_DIR, "zec_market_history.csv")
OUT = os.path.join(DATA_DIR, "zec_price_chart.csv")


def decimal_year(date_str):
    d = datetime.strptime(date_str, "%Y-%m-%d")
    start = datetime(d.year, 1, 1)
    end = datetime(d.year + 1, 1, 1)
    return d.year + (d - start).total_seconds() / (end - start).total_seconds()


def main():
    with open(SRC) as handle:
        rows = list(csv.DictReader(handle))

    sampled = rows[::7]
    if rows and sampled[-1] is not rows[-1]:
        sampled.append(rows[-1])

    out_rows = []
    for row in sampled:
        price = float(row["price_usd"])
        cap = float(row["market_cap_usd"])
        out_rows.append([round(decimal_year(row["date"]), 4), round(price, 2), round(cap / 1e9, 3)])

    with open(OUT, "w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["t", "price", "marketcap_bn"])
        writer.writerows(out_rows)
    print("wrote %s (%d rows), price range %.0f to %.0f"
          % (os.path.relpath(OUT), len(out_rows),
             min(r[1] for r in out_rows), max(r[1] for r in out_rows)))


if __name__ == "__main__":
    main()
