# UBC 2026 — Franklin Crypto Research Competition

Two candidate entries, by Eli Dubizh (Boiler Blockchain, Purdue University). Schools may submit multiple teams, so we may enter one or both as separate Boiler Blockchain submissions.

| Entry | Track | Direction | Deliverable |
|---|---|---|---|
| **Solana (SOL)** | 02, Market Cap Over $250M | Long | `report/Solana_SOL_Long_Thesis_UBC2026.pdf` |
| **Zcash (ZEC)** | 03, Market Cap Over $1B | Short | `report/Zcash_ZEC_Short_Thesis_UBC2026.pdf` |

### Submission
- **Deadline:** November 9, 2026, 11:59 PM ET
- **Submit via:** Google Form — https://docs.google.com/forms/d/e/1FAIpQLSdeYdyU_AWRAw5o5F5myFWyxsbtSQDvz_ZLMYGU2EIWIwgDHw/viewform
- **Downstream:** finalists announced Nov 16; live pitch (5 min + 5 min Q&A) at UT Austin Nov 20.

### Entry 1 — Solana (SOL), Long
The market pays ~27× revenue for execution quality (Hyperliquid); Solana's October 21, 2026 **Alpenglow** upgrade (one-slot, zero-downtime consensus swap; ~12.8s → ~150ms finality) makes it the only $50B-scale base layer that can credibly claim it, and the re-rating is not yet priced. Concede ~175× on network REV (a broken denominator in abundant blockspace); re-anchor on price-to-app-revenue (~44×, re-accelerating, #1 chain for 9 quarters) plus the execution re-rating. Targets (12–18mo): Bear $55, Base $160, Bull $290.

### Entry 2 — Zcash (ZEC), Short
A metrics-driven, non-consensus short built to beat two valuation lenses at once. On **network revenue** (the Blockworks REV metric) Zcash earned ~$204K of fees in all of Q3 2026 against a ~$21B cap, roughly 25,000× revenue where productive chains sit near 40×. On the **monetary-premium / store-of-value** lens it is a worse Bitcoin: its supply was unverifiable for years after the Orchard counterfeiting flaw, the ECC founding team left in Jan 2026, issuance runs ~3.3% with a 12% dev-fund cut, and privacy is optional (~29% shielded). F2Pool's Chun Wang called the run a "narrative bid." It trades at ~1.8× Monero's cap while doing less real private payment, and the bid is reflexive (levered longs plus a Winklevoss-backed treasury, Cypherpunk, ~1.9% of supply at a ~$342 cost). Targets (6–12mo): Base $650 (~46% down, ≈ Monero's cap), Deeper $450 (~63%), acknowledged squeeze risk to $2,000. Regulation is a secondary risk, not the thesis.

### Report structure (per competition memo)
Title page · Executive Summary · Project Overview · Investment Proposal · Conclusion · Appendix · References. 5-page main body max, excluding title page, appendix, and references.

### Data & provenance
Primary numbers are drawn from the **Blockworks Research** datasets (the official competition toolkit; REV = the dollar value of all transaction fees), including the Solana and Zcash Token Holder Reports. The Zcash charts and figures run on a small, reproducible, free-tier pipeline in `scripts/` that pulls market data from CoinGecko into dated CSVs in `data/`, cross-checked against the Blockworks market series. Price/cap as of early November 2026.

### Build
Compiled with LaTeX (TinyTeX or any TeX Live). From the repo root, run each command twice so the running headers settle:
```bash
# Solana long
pdflatex -output-directory report -jobname Solana_SOL_Long_Thesis_UBC2026 report/report.tex
# Zcash short
pdflatex -output-directory report -jobname Zcash_ZEC_Short_Thesis_UBC2026 report/short_zcash.tex
```
Charts are drawn in pgfplots; black, gray, and white theme with no dashes anywhere in the text. The Zcash figures read real data from `data/`; refresh it any time with `python3 scripts/fetch_market_data.py && python3 scripts/build_chart_data.py` (free, no API key).

### Files
- `report/report.tex` LaTeX source, Solana long thesis
- `report/Solana_SOL_Long_Thesis_UBC2026.pdf` the Solana long (Track 02)
- `report/short_zcash.tex` LaTeX source, Zcash short thesis
- `report/Zcash_ZEC_Short_Thesis_UBC2026.pdf` the Zcash short (Track 03)
- `scripts/fetch_market_data.py` pulls free CoinGecko market data into `data/`
- `scripts/build_chart_data.py` turns the price history into chart-ready data for the report
- `data/` frozen, dated CSVs: market history, current prices, and key figures with sources
- `Franklin Crypto Research Competiton Memo - UBC 2026 .pdf` the official competition rules
