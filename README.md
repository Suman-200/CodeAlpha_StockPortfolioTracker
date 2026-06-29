# 📈 Task 2 — Stock Portfolio Tracker

**CodeAlpha Python Programming Internship**
**Intern:** DARA.SUMAN &nbsp;|&nbsp; **ID:** CA/DF1/146755 &nbsp;|&nbsp; **Duration:** 20 June 2026 – 20 July 2026

---

## 📌 Project Overview

A **command-line Stock Portfolio Tracker** that lets users enter stock symbols and quantities, calculates total investment value using hardcoded market prices, and optionally saves results to a `.csv` or `.txt` file.

---

## 🧠 Key Concepts Used

| Concept | Where Used |
|---|---|
| Dictionary | Hardcoded stock prices & portfolio storage |
| Input / Output | User enters stock symbols & quantities |
| Basic Arithmetic | Price × Quantity = Value, total sum |
| File Handling (CSV) | `csv.DictWriter` saves portfolio to `.csv` |
| File Handling (TXT) | Plain-text report saved with `open()` |
| Functions | Modular design across 6+ functions |
| `datetime` module | Timestamp added to saved filenames |
| Error Handling | `try/except` for invalid numeric input |

---

## 📂 Project Structure

```
CodeAlpha_StockPortfolioTracker/
│
├── stock_tracker.py     ← Main application file
├── portfolio_*.csv      ← Auto-generated (after saving)
├── portfolio_*.txt      ← Auto-generated (after saving)
└── README.md            ← This file
```

---

## 🏦 Supported Stocks (Hardcoded Prices)

| Ticker | Company | Price (USD) |
|---|---|---|
| AAPL | Apple Inc. | $195.50 |
| TSLA | Tesla Inc. | $248.75 |
| GOOGL | Alphabet Inc. | $178.30 |
| MSFT | Microsoft Corp. | $415.20 |
| AMZN | Amazon.com Inc. | $192.60 |
| META | Meta Platforms | $530.10 |
| NVDA | NVIDIA Corp. | $875.40 |
| NFLX | Netflix Inc. | $645.80 |

---

## ▶️ How to Run

**Requirements:** Python 3.x (no external libraries needed)

```bash
python stock_tracker.py
```

---

## 🖥️ Sample Interaction

```
  Available stocks shown with prices...

  Enter your stocks below. Type 'done' when finished.

  Stock symbol (or 'done'): AAPL
  Quantity of AAPL: 10
  ✅  AAPL × 10 added to portfolio.

  Stock symbol (or 'done'): TSLA
  Quantity of TSLA: 5
  ✅  TSLA × 5 added to portfolio.

  Stock symbol (or 'done'): done

  ───────────────────────────────────────────────────────
  SYMBOL     QTY    PRICE (USD)     VALUE (USD)
  ───────────────────────────────────────────────────────
  AAPL        10         195.50        1,955.00
  TSLA         5         248.75        1,243.75
  ───────────────────────────────────────────────────────
  TOTAL INVESTMENT                  $    3,198.75
  ───────────────────────────────────────────────────────

  Save results? (csv / txt / both / no): both
  💾  Portfolio saved to: portfolio_20260629_142301.csv
  💾  Portfolio saved to: portfolio_20260629_142301.txt
```

---

## 📋 Task Requirements Checklist

- [x] User inputs stock names and quantity via console
- [x] Hardcoded dictionary defines stock prices
- [x] Total investment value calculated and displayed
- [x] Results saved to `.csv` file (optional)
- [x] Results saved to `.txt` file (optional)
- [x] Dictionary, input/output, arithmetic, file handling — all used
- [x] Multiple portfolio sessions supported

---

## 👤 Intern Details

| Field | Value |
|---|---|
| Name | DARA.SUMAN |
| Student ID | CA/DF1/146755 |
| Domain | Python Programming |
| Company | CodeAlpha |
| Period | 20 June 2026 – 20 July 2026 |

---

> **GitHub Repository:** `CodeAlpha_StockPortfolioTracker`  
> Upload this folder to GitHub with the exact repository name above as per CodeAlpha instructions.
