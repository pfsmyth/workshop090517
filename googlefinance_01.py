from googlefinance import getQuotes
import json
print(json.dumps(getQuotes(['MSFT', 'AAPL']), indent=2))
