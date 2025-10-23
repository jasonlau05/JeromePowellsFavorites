import robin_stocks.robinhood as robin
import sys

lines = open('creds.txt').read().splitlines()
USER = lines[0]
PASS = lines[1]

login = robin.login(USER, PASS)

def QUOTE(ticker):
    r = robin.get_latest_price(ticker)
    print(ticker.upper() + ": $" + str(r[0]))

TICKER = sys.argv[1:][0].upper()
QUOTE(TICKER)

#logout = robin.robinhood.authentication.logout()