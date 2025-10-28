import datetime
from robin import BUY, QUOTE
from areMarketsOpen import is_market_open
import os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print('today is', datetime.date.today())

# run this script every morning at market open

def main():
    if is_market_open():
        BUY('VOO', 5)

if __name__ == "__main__":
    main()