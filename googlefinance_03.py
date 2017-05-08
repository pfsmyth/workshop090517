from googlefinance import getQuotes
import json

fw = open('c:/data/Nasdaq.csv', 'a')
cline = ""

x = json.dumps(getQuotes(['MSFT', 'AAPL']))
x = json.loads(x)

for x in x:
    cline = ""
    cline = cline + x["StockSymbol"] + "," 
    cline = cline + x["Index"] + "," 
    cline = cline + x["LastTradeDateTime"] + "," 
    cline = cline + x["LastTradePrice"] + "," 
    cline = cline + x["LastTradeDateTimeLong"] + "," 
    cline = cline + x["LastTradeWithCurrency"] + "\n" 
    fw.write(cline)
    #print(cline)
fw.close()
