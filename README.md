# Zcash (ZEC) Short Thesis

Franklin Crypto Research Competition, University Blockchain Conference 2026.

```
Name:          Eli Dubizh
Organization:  Purdue University
Competition:   Franklin Crypto Research Competition, UBC 2026
Track:         Short, Market Cap Over $1B
Asset:         Zcash (ZEC)
Direction:     Short
Date:          November 2026
Contact:       ed200419@gmail.com
Report:        report/Zcash_ZEC_Short_Thesis_UBC2026.pdf
```

### Thesis
Zcash melted up into a top ten market cap on narrative, not fundamentals. Over the past year the whole network earned about $712,000 in fees against a roughly $20 billion valuation. Hyperliquid carries about the same market cap and earned $895 million in fees over the same stretch, more than a thousand times as much. Same price, a thousand times the business. The bid is reflexive, so we are short.

| Scenario | ZEC price | Return to the short |
| --- | --- | --- |
| Short entry | ~$1,170 | |
| Base target | ~$650 | +44% |
| Squeeze risk | ~$2,000 | (71%) |

Base case is roughly Monero parity, over a 6 to 12 month horizon.

### Data and reproducibility
Every figure is built from free, public data. Pricing and fees from DefiLlama, CoinMetrics, CoinGecko, and Artemis; network revenue from the Blockworks Zcash Token Holder Report; the Orchard disclosure from Allium.

```bash
# pull and build the chart data (no API key required)
python3 scripts/fetch_market_data.py
python3 scripts/build_chart_data.py
python3 scripts/compute_volatility.py
```

Frozen data lives in `data/`. The report is one self contained LaTeX file with pgfplots charts.

```bash
# build the PDF (run twice so the running headers settle)
pdflatex -output-directory report -jobname Zcash_ZEC_Short_Thesis_UBC2026 report/short_zcash.tex
```

### Files
- `report/short_zcash.tex` report source
- `report/Zcash_ZEC_Short_Thesis_UBC2026.pdf` the report
- `scripts/` free data fetch and transform scripts
- `data/` frozen, dated CSVs with sources
- `Franklin Crypto Research Competiton Memo - UBC 2026 .pdf` the competition rules

### AI
- handoff count (opus 4.8) = 2
