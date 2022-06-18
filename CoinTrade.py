import xlwings, pandas, requests
#import python-binance
#from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

wb1 = xlwings.Book('C:\\Users\\Naveen Kumar\\OneDrive - RxLogix\\Documents\\PersoMe\\Invest\\CoinTrade.xlsx').sheets('WazirX')
wb2 = xlwings.Book('C:\\Users\\Naveen Kumar\\OneDrive - RxLogix\\Documents\\PersoMe\\Invest\\CoinTrade.xlsx').sheets('Binance')


while True:
    ##r1 = requests.get('https://api.wazirx.com/api/v2/tickers')
    r1 = requests.get('https://api.wazirx.com/api/v2/market-status')
    r2 = requests.get('https://api.binance.com/api/v1/ticker/allPrices')
    #prices = client.get_all_tickers()
    
    wb1.range('a1').options(pandas.DataFrame, index = False).value = pandas.json_normalize(r1.json() , 'markets')
    #wb2.range('a1').options(pandas.DataFrame, index = False).value = pandas.json_normalize(prices.json())  was create for API

    wb2.range('a1').options(pandas.DataFrame, index = False).value = pandas.json_normalize(r2.json())
    
    
