import robin_stocks.robinhood as robin
import sys

lines = open('creds.txt').read().splitlines()
USER = lines[0]
PASS = lines[1]

login = robin.login(USER, PASS)

def QUOTE(ticker):
    r = robin.get_latest_price(ticker)
    print(ticker.upper() + ": $" + str(r[0]))

def BUY(ticker, amt):
    r = robin.order_buy_fractional_by_price(ticker, amt)
    print(r)

def SELL(ticker, amt):
    r = robin.order_sell_fractional_by_price(ticker, amt)
    print(r)

#logout = robin.robinhood.authentication.logout()