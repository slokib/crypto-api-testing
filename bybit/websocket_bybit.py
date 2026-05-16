#import all needed SDK
import time
import pybit.unified_trading
from pybit.unified_trading import WebSocket
import bybit_symbols as b

# REPLACE b.xxx with what other pairs are available in the bybit_symbols file
pair = b.btc

# assign ws as Websocket with testnet disabled and channel type as linear futures
ws = WebSocket(
    testnet = False,
    channel_type= "linear"
)

ba_p = ba_q = bb_p = bb_q = None # declare the best ask, and best bid vars (price, quantity)

# add function to use to handle once orderbook data is received
def receive_orderbook(message):
    # global is used to bring in those vars from earlier
    global ba_p, ba_q, bb_q, bb_p
    if "data" not in message:
        return
    ba_p = message["data"]["a"][0][0] # since depth for the book is 1 theres only one list indexed at zero
    ba_q = message["data"]["a"][0][1]  
    bb_p = message["data"]["b"][0][0]
    bb_q = message["data"]["b"][0][1]

ws.orderbook_stream(
    depth=1, # how far up the ladder you want to go 1 for lowest ask and highest bid, 1000 for seeing far away orders
    symbol=pair, 
    callback=receive_orderbook # sends message to function
)

trades = [] # for storing trades
timestamp = symbol = side = size = price = direction = rest = None
def receive_recent_trades(message):
    global timestamp, symbol, side, size, price, direction, rest, trades
    if "data" not in message:
        return
    # loop through data as keys & values are inside a dictionary inside of a list
    for trade in message["data"]:
        # unpack dict values
        timestamp, symbol, side, size, price, direction, *rest = trade.values()
        # string is added to list
        trades.append(f"{side} trade on {symbol}: {size} @ {price}")
        # expected output: Buy trade on BTCUSDT: 3 @ 79000.0
        trades = trades[-7:] # limit list to 7 trades

ws.trade_stream(
    symbol=pair,
    callback=receive_recent_trades
)

l_price = None
def receive_ticker(message):
    if "data" not in message:
        return
    global l_price
    # extract just ticker data
    tickerdata = message["data"] 
    # get lastPrice value from data dictionary for the last traded price
    l_price = tickerdata["lastPrice"]

ws.ticker_stream(
    symbol=pair,
    callback=receive_ticker
)

# final outputs, run a loop thats waits until stream has come in and vars finally are assigned to smthing
while True:
    if ba_p is not None:
        # the \033 thing was by claude for formatting coz idk how to do it
        print(f"\033[K {pair}'s Last Traded Price: {l_price}")
        print(f"\033[K The best ask is {ba_p} with {ba_q} orders left")
        print(f"\033[K The best bid is {bb_p} with {bb_q} orders left")
        if trades is not None:
            # will loop through the last 7 trades, then reverse it so the most recent is first
            for t in reversed(trades[-7:]):
                print(f"\033[K {t}")
        total_lines = 3 + len(trades)
        print(f"\033[{total_lines}A", end="")
    # keep script running
    time.sleep(0.00000000000001)