import requests

currency = "pln"
coinsList = None

def getCoinsList():
    global coinsList
    # {'id': '01coin', 'symbol': 'zoc', 'name': '01coin', 'platforms': {}}
    response = requests.get("https://api.coingecko.com/api/v3/coins/list?include_platform=true")
    if response.ok == True:
        print("response ok")
        data = response.json()
        print("Ilość kryptowalut:", len(data))
        coinsList = data
        

def findCoinBySymbol(symbol):
    symbol = symbol.lower().strip()
    for coin in coinsList:
        if coin["symbol"] == symbol:
            return coin

def getCoinLastMarketData(coinId):
    # marketData: {'bitcoin': {'pln': 111567, 'pln_market_cap': 2155405067539.3752,
    #  'pln_24h_vol': 269812166482.46234, 'pln_24h_change': 2.2485526453534925,
    #  'last_updated_at': 1678995065}}
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids="+coinId+"&vs_currencies="+currency+"&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true")
    if response.ok:
        data = response.json()
        return data
    else:
        return None
    
def getCoinPriceInCurrency(coinId, currency):
    currency = currency.lower().strip()
    marketData = getCoinLastMarketData(coinId)
    return marketData[coinId][currency]



getCoinsList()

btcData = findCoinBySymbol("btc")
print(btcData)

marketData = getCoinLastMarketData(btcData["id"])
print("marketData:", marketData)

coinPrice = getCoinPriceInCurrency(btcData["id"], currency)
print("Coin price in", currency, coinPrice)

print("\nWitamy w crypto exchange")

while True:
    cryptoSymbolToBuy = input("Wybierz symbol krypto do kupienia np. btc lub exit aby zakończyć: ")
    if cryptoSymbolToBuy == "exit":
        break
    coinData = findCoinBySymbol(cryptoSymbolToBuy)
    if coinData == None:
        print("Nie ma takiej kryptowaluty")
        continue

    coinPrice = getCoinPriceInCurrency(coinData["id"], currency)
    print("Cena:", str(coinData["id"]), coinPrice, currency)

    moneyToBuyCrypto = float(input("Ile chcesz przeznaczyć na zakup: "))
    boughtCrypto = moneyToBuyCrypto / coinPrice

    print("\nGratulacje, kupiłeś", boughtCrypto, cryptoSymbolToBuy)
