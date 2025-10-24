import pandas as pd
import pandas_market_calendars as mcal
from datetime import datetime
import pytz

def is_market_open():

    # check date here    
    nyse = mcal.get_calendar('XNYS') 
    
    market_tz = pytz.timezone('America/Chicago')
    now = datetime.now(market_tz)
    
    schedule = nyse.schedule(start_date=now, end_date=now)
    
    if schedule.empty:
        return False, "closed for weekend or holiday"

    market_open = schedule.iloc[0].market_open.tz_convert(market_tz)
    market_close = schedule.iloc[0].market_close.tz_convert(market_tz)

    # check time here
    if market_open <= now < market_close:
        return True, "lock in broski"
    else:
        return False, f"this isnt a casino, go touch grass"

is_open, status_message = is_market_open()

if is_open:
    print('market open')
else:
    print('market closed')