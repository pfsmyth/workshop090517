from googlefinance import getQuotes
import json
xx = json.dumps(getQuotes(['MSFT', 'AAPL']))

print(type(xx))
#print(xx)

xx = json.loads(xx)

print(type(xx))
#print(xx)

for x in xx:
    print(x["StockSymbol"], 
          x["Index"],
          x["LastTradeDateTime"], 
          x["LastTradePrice"],
          x["LastTradeTime"],
          x["LastTradeDateTimeLong"],
          x["LastTradeWithCurrency"]         
         )
