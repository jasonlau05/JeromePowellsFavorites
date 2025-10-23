import robin_stocks as robin

lines = open('creds').read().splitlines()
USER = lines[0]
PASS = lines[1]

login = robin.robinhood.authentication.login(USER, PASS)