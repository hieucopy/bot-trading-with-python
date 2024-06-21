import ccxt
import pandas as pd
import time
import datetime
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from algo import process
exchange = ccxt.binance({
    'apiKey': "83AMhDA41WWBFpeGjrkCJInS6jlj71oiTomFJwVAtzUJDZcLYhVYME4WP0PsegPm",
    'secret': '8nzRpOZB5KMXpX1V5LhbU04zPXL7W8fWVwU07pgVENx7r2PX94eWpQuvGABW6cWR',
})

        
exchange.set_sandbox_mode(True)

from select_coin import input
coin=input()
pair=coin+'/USDT'
print(pair)  

x=[]
y=[]
fig, ax = plt.subplots(figsize=(10, 6))
line, = ax.plot(x, y, linestyle='-', marker='o')
i=1
ax.set_title('Biểu đồ thay đổi sổ dư')
ax.set_xlabel('Thời gian')
ax.set_ylabel('Giá trị')
def update(frame):
    global i
    i=i+1
    x.append(i)
    y.append(process(exchange))
    line.set_data(x,y)
    ax.relim()
    
    ax.autoscale_view()  
    return line
ani = animation.FuncAnimation(fig, update, interval=60000)
# Hiển thị biểu đồ
plt.tight_layout()
plt.show()


 