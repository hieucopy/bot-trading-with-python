import ccxt 
import pandas as pd
import time
import datetime
from matplotlib import pyplot as plt
import matplotlib.animation as animation


from select_coin import input
coin=input()
pair=coin+'/USDT'
print(pair)     


def process(exchange):

    def tongsodu():
        balance= exchange.fetch_balance()
        btc_balance= balance['total'][coin]
        usdt=balance['total']['USDT']
        return usdt+(btc_balance-1)*price
    
    def sell():
        order = exchange.create_market_sell_order(pair,quantity)
        print("sell", quantity, 'btc/usd at price ', price,'at',  df.iloc[4]['timestamp'] )
        print(tongsodu())

    def buy():
        order = exchange.create_market_buy_order(pair,quantity)
        print("buy", quantity, 'btc/usd at price ', price,'at',  df.iloc[4]['timestamp'] )
        print(tongsodu())
    x =exchange.fetch_ohlcv(pair,timeframe='1m', limit = 5)
    df=pd.DataFrame(x,columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp']=df["timestamp"].apply(lambda x:datetime.datetime.fromtimestamp(x/ 1000))
    price=df.iloc[4]['close']
    price
    trade_size=1000
    quantity=1000/price
    balance= (exchange.fetch_balance())
    avgprice= df['close'].mean()
    if (price>avgprice) :
        sell()
    else:
        buy()
    return tongsodu()