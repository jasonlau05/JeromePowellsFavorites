import datetime
import yfinance as yf

from robin import BUY, QUOTE, SELL

# watchlist
TICKERS = ["AAPL", "MSFT", "NVDA", "AMZN", "BX", "INTC", "PG", "SNY"]
BUY_AMOUNT = 25.00
DAYS_BEFORE = 1

print('             today is', datetime.date.today())

def next_earnings(ticker):
    t = yf.Ticker(ticker)
    df = t.get_earnings_dates(limit=5)
    if df is None or df.empty:
        return None
    for idx in df.index:
        d = idx.date() if hasattr(idx, "date") else idx
        if d >= datetime.date.today():
            return d
    return None

def main():
    today = datetime.date.today()
    target_date = today + datetime.timedelta(days=DAYS_BEFORE)

    for ticker in TICKERS:
        d = next_earnings(ticker)
        if not d:
            print(f"{ticker}: no upcoming earnings found.")
            continue

        if d == target_date:
            print(f"bought ${BUY_AMOUNT} of {ticker}")
            BUY(ticker, BUY_AMOUNT)
        else:
            print(f"{ticker}: skipping - next earnings on {d}")

if __name__ == "__main__":
    main()
