# UBC 2026 — Franklin Crypto Research Competition
## Solana (SOL) — Long Thesis · Track 02 (Market Cap Over $250M)

**Thesis in one line:** The market pays ~27× revenue for execution quality (Hyperliquid); Solana's October 21, 2026 **Alpenglow** upgrade makes it the only $50B-scale base layer that can credibly claim it — and the re-rating is not yet priced.

### Submission
- **Deadline:** November 9, 2026, 11:59 PM ET
- **Submit via:** Google Form — https://docs.google.com/forms/d/e/1FAIpQLSdeYdyU_AWRAw5o5F5myFWyxsbtSQDvz_ZLMYGU2EIWIwgDHw/viewform
- **Deliverable:** `report/Solana_SOL_Long_Thesis_UBC2026.pdf` (5-page main body; title page, appendix, and references excluded per rules)
- **Downstream:** finalists announced Nov 16; live pitch (5 min + 5 min Q&A) at UT Austin Nov 20.

### Report structure (per competition memo)
Title page · Executive Summary · Project Overview · Investment Proposal · Conclusion · Appendix · References.

### The argument
1. **Reframe the scarce resource.** Blockspace is abundant and commoditized; *execution quality* (uptime, sub-second deterministic finality, low landed-tx failure) is the value-accruing factor. The market already prices it — Hyperliquid trades at ~27× protocol revenue.
2. **The catalyst.** Alpenglow shipped Oct 21, 2026 as a one-slot, zero-downtime consensus hot-swap (a first for any live chain): finality ~12.8s → ~150ms target, "20+20" fault model, ~30 months of 100% uptime.
3. **The fundamentals fit the judges' lens.** #1 app revenue for 9 straight quarters (~$299M Q3'26, +48% QoQ), #1 DEX volume, ~$16.8B stablecoins (ATH), REV inflecting +48% QoQ.
4. **Honest valuation.** Concede ~175× on network REV (a broken denominator in abundant blockspace — ETH >1,000×); re-anchor on price-to-app-revenue (~44×, re-accelerating) and the execution re-rating.
5. **Targets (12–18mo):** Bear $55 (−38%), Base $160 (+80%), Bull $290 (+226%).

### Data & provenance
Primary numbers are drawn from the **Blockworks Research "Blockchains" dataset** (the official competition toolkit; REV = base + priority fees + MEV tips), cross-checked against Blockworks' Solana Q3 2026 Token Holder Report, Anza, Messari, 21Shares, and DeFiLlama. Price/cap as of early November 2026.

### Build
```bash
npm install          # puppeteer (HTML → PDF)
node report/render.js  # regenerates report/Solana_SOL_Long_Thesis_UBC2026.pdf
```
Source: `report/report.html` (self-contained — inline CSS and SVG charts). `render.js` prints it to Letter PDF via headless Chrome.

### Files
- `report/report.html` — report source (design, copy, charts)
- `report/render.js` — PDF renderer
- `report/Solana_SOL_Long_Thesis_UBC2026.pdf` — the submission
- `Franklin Crypto Research Competiton Memo - UBC 2026 .pdf` — official competition rules
