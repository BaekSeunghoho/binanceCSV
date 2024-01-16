import ccxt 
import time
import datetime


api_key = 'mFPnaCjxx55x7xw5HD6tj4ALs4ZMgPei65juuGFgcM3u99gnM4ykmpluieYgDTBi' # mFPnaCjxx55x7xw5HD6tj4ALs4ZMgPei65juuGFgcM3u99gnM4ykmpluieYgDTBi
secret  = 'WXWparosoCCH6hni2of8nUM1R8Si5ukTbN94uAgknVSeWzrnDSzDbhmhygOFOtd3' # WXWparosoCCH6hni2of8nUM1R8Si5ukTbN94uAgknVSeWzrnDSzDbhmhygOFOtd3

binance = ccxt.binance(config={
    'apiKey': api_key, 
    'secret': secret,
    'enableRateLimit': True,
    'options': {
        'defaultType': 'future'
    }
})

symbol = "BTC/USDT"

while True: 
    btc = binance.fetch_ticker(symbol)
    now = datetime.datetime.now()
    print(now, btc['last'])
    time.sleep(1)