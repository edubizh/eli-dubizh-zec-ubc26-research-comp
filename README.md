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
A metrics-driven, non-consensus short: on the fundamentals this panel grades (value accrual, usage, comparables, holder economics), ZEC has not earned a top-ten valuation. An insider (F2Pool's Chun Wang) called the run a "narrative bid." ZEC generates negligible economic value, shields under a third of its own supply, trades at ~2× Monero's cap while doing *less* real private payment, and sits at an MVRV ~3.3 (average holder up ~240%). The bid is reflexive (short squeezes + a MicroStrategy-style treasury, Cypherpunk) and already rolling over post-NU7. Targets (6–12mo): Base $650 (~49% down), Deeper $450, acknowledged squeeze risk to $2,000. Regulation is treated as a secondary risk, not the thesis.

### Report structure (per competition memo)
Title page · Executive Summary · Project Overview · Investment Proposal · Conclusion · Appendix · References. 5-page main body max, excluding title page, appendix, and references.

### Data & provenance
Primary numbers are drawn from the **Blockworks Research** datasets (the official competition toolkit; REV = base + priority fees + MEV tips), including the Solana and Zcash Token Holder Reports, cross-checked against Messari, ZecStats, 21Shares, CoinGecko, and DeFiLlama. Price/cap as of early November 2026.

### Build
Compiled with LaTeX (TinyTeX or any TeX Live). From the repo root, run each command twice so the running headers settle:
```bash
# Solana long
pdflatex -output-directory report -jobname Solana_SOL_Long_Thesis_UBC2026 report/report.tex
# Zcash short
pdflatex -output-directory report -jobname Zcash_ZEC_Short_Thesis_UBC2026 report/short_zcash.tex
```
Each source is one self-contained file; charts are drawn in pgfplots; black, gray, and white theme with no dashes anywhere in the text.

### Files
- `report/report.tex` LaTeX source, Solana long thesis
- `report/Solana_SOL_Long_Thesis_UBC2026.pdf` the Solana long (Track 02)
- `report/short_zcash.tex` LaTeX source, Zcash short thesis
- `report/Zcash_ZEC_Short_Thesis_UBC2026.pdf` the Zcash short (Track 03)
- `Franklin Crypto Research Competiton Memo - UBC 2026 .pdf` the official competition rules
