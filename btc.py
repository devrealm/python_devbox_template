import ccxt

bybit = ({
    'enableRateLimit' : True,
    'apiKey' : '',
    'secret' : '',
})

print(bybit)


def get_bid_ask():

    bybit = ccxt.bybit()

    bybit.apiKey = ''
    bybit.secret = ''

    btc_bybit_book = bybit.fetch_order_book('BTCUSD') 
    print(btc_bybit_book)
    btc_bid = btc_bybit_book['bids'][0][0]
    btc_ask = btc_bybit_book['asks'][0][0]
    print(f'the best bid is {btc_bid} the best ask is {btc_ask}')

    return btc_bid, btc_ask

get_bid_ask()