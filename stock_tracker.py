"""
CodeAlpha Python Programming Internship
Task 2: Stock Portfolio Tracker
Intern: DARA.SUMAN | ID: CA/DF1/146755
"""

import csv
import os
from datetime import datetime

# ─────────────────────────────────────────
#  Hardcoded stock prices (USD)
# ─────────────────────────────────────────
STOCK_PRICES: dict[str, float] = {
    "AAPL":  195.50,   # Apple Inc.
    "TSLA":  248.75,   # Tesla Inc.
    "GOOGL": 178.30,   # Alphabet Inc.
    "MSFT":  415.20,   # Microsoft Corp.
    "AMZN":  192.60,   # Amazon.com Inc.
    "META":  530.10,   # Meta Platforms
    "NVDA":  875.40,   # NVIDIA Corp.
    "NFLX":  645.80,   # Netflix Inc.
}

DIVIDER = "─" * 55


def print_header() -> None:
    print("\n" + "=" * 55)
    print("      📈  Stock Portfolio Tracker — CodeAlpha")
    print("=" * 55)


def show_available_stocks() -> None:
    """Display all supported tickers with their current prices."""
    print(f"\n  {'Ticker':<8} {'Company / Price (USD)':>42}")
    print(f"  {DIVIDER}")
    labels = {
        "AAPL": "Apple Inc.",
        "TSLA": "Tesla Inc.",
        "GOOGL": "Alphabet Inc.",
        "MSFT": "Microsoft Corp.",
        "AMZN": "Amazon.com Inc.",
        "META": "Meta Platforms",
        "NVDA": "NVIDIA Corp.",
        "NFLX": "Netflix Inc.",
    }
    for ticker, price in STOCK_PRICES.items():
        print(f"  {ticker:<8} {labels[ticker]:<30} ${price:>8.2f}")
    print()


def get_portfolio() -> dict[str, int]:
    """
    Interactively collect stock symbols and quantities from the user.
    Returns a dict  {symbol: quantity}.
    """
    portfolio: dict[str, int] = {}
    print("\n  Enter your stocks below.")
    print("  Type 'done' when finished.\n")

    while True:
        symbol = input("  Stock symbol (or 'done'): ").strip().upper()

        if symbol == "DONE":
            if not portfolio:
                print("  ⚠  You haven't added any stocks yet. Please add at least one.\n")
                continue
            break

        if symbol not in STOCK_PRICES:
            print(f"  ⚠  '{symbol}' is not in our price list. Available tickers shown above.\n")
            continue

        try:
            qty_raw = input(f"  Quantity of {symbol}: ").strip()
            qty = int(qty_raw)
            if qty <= 0:
                raise ValueError
        except ValueError:
            print("  ⚠  Please enter a positive whole number for quantity.\n")
            continue

        if symbol in portfolio:
            portfolio[symbol] += qty
            print(f"  ✅  Added {qty} more shares of {symbol} (total: {portfolio[symbol]}).\n")
        else:
            portfolio[symbol] = qty
            print(f"  ✅  {symbol} × {qty} added to portfolio.\n")

    return portfolio


def calculate_portfolio(portfolio: dict[str, int]) -> list[dict]:
    """Return a list of rows with symbol, qty, price, and value."""
    rows = []
    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * qty
        rows.append({"symbol": symbol, "qty": qty, "price": price, "value": value})
    return rows


def display_portfolio(rows: list[dict]) -> float:
    """Print a formatted portfolio table and return total investment."""
    total = sum(r["value"] for r in rows)

    print(f"\n  {DIVIDER}")
    print(f"  {'SYMBOL':<8} {'QTY':>6} {'PRICE (USD)':>14} {'VALUE (USD)':>14}")
    print(f"  {DIVIDER}")
    for r in rows:
        print(f"  {r['symbol']:<8} {r['qty']:>6} {r['price']:>14.2f} {r['value']:>14.2f}")
    print(f"  {DIVIDER}")
    print(f"  {'TOTAL INVESTMENT':>30}   ${total:>12.2f}")
    print(f"  {DIVIDER}\n")

    return total


def save_to_csv(rows: list[dict], total: float) -> None:
    """Save the portfolio summary to a timestamped CSV file."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"portfolio_{timestamp}.csv"

    with open(filename, "w", newline="") as csvfile:
        fieldnames = ["Symbol", "Quantity", "Price_USD", "Value_USD"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            writer.writerow({
                "Symbol":    r["symbol"],
                "Quantity":  r["qty"],
                "Price_USD": f"{r['price']:.2f}",
                "Value_USD": f"{r['value']:.2f}",
            })
        # Totals row
        writer.writerow({
            "Symbol":    "TOTAL",
            "Quantity":  "",
            "Price_USD": "",
            "Value_USD": f"{total:.2f}",
        })

    print(f"  💾  Portfolio saved to: {filename}\n")


def save_to_txt(rows: list[dict], total: float) -> None:
    """Save the portfolio summary to a timestamped plain-text file."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"portfolio_{timestamp}.txt"

    with open(filename, "w") as f:
        f.write("CodeAlpha — Stock Portfolio Tracker\n")
        f.write(f"Generated: {datetime.now().strftime('%d %B %Y  %H:%M:%S')}\n")
        f.write(f"Intern: DARA.SUMAN  |  ID: CA/DF1/146755\n")
        f.write("=" * 55 + "\n")
        f.write(f"{'SYMBOL':<10} {'QTY':>6} {'PRICE':>12} {'VALUE':>14}\n")
        f.write("-" * 55 + "\n")
        for r in rows:
            f.write(f"{r['symbol']:<10} {r['qty']:>6} {r['price']:>12.2f} {r['value']:>14.2f}\n")
        f.write("=" * 55 + "\n")
        f.write(f"{'TOTAL INVESTMENT':>40}  ${total:>12.2f}\n")

    print(f"  💾  Portfolio saved to: {filename}\n")


def main() -> None:
    print_header()
    show_available_stocks()

    while True:
        portfolio = get_portfolio()
        rows = calculate_portfolio(portfolio)
        total = display_portfolio(rows)

        # Ask user if they want to save
        save_choice = input("  Save results? (csv / txt / both / no): ").strip().lower()
        if save_choice in ("csv", "both"):
            save_to_csv(rows, total)
        if save_choice in ("txt", "both"):
            save_to_txt(rows, total)

        again = input("  Track another portfolio? (yes / no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\n  Thank you for using the Stock Portfolio Tracker! 📊\n")
            break


if __name__ == "__main__":
    main()
