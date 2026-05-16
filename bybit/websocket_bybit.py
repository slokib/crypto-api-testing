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
    global ba_p, ba_q, bb_q, bb_p # global is used to bring in those vars from earlier
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
        trades.append(f"{side} trade on {symbol}: {size} @ {price}") # string is added to list
        trades = trades[-7:] # limit list to 7 trades
    #print(f"{side} trade on {symbol}: {size} @ {price}")
    # expected output: Buy trade on BTCUSDT: 3 @ 79000.0

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
    # \r means go back to start of line, end means stay on the same line,
    # so previous line is overwritten
    #print(f"\r{pair}'s Last Traded Price: {l_price}", end="")

ws.ticker_stream(
    symbol=pair,
    callback=receive_ticker
)

# final outputs, run a loop thats waits until stream has come in and vars finally are assigned to smthing
while True:
    if ba_p is not None:
        for t in trades[-7:]: # list created from before, will loop though all
            print(f"\033[K {t}") # will print as many trades as it can before the limit below is hit
        print(f"\033[K {pair}'s Last Traded Price: {l_price}")
        print(f"\033[K The best ask is {ba_p} with {ba_q} orders left") # the \033 thing was by claude smh
        print(f"\033[K The best bid is {bb_p} with {bb_q} orders left")
        total_lines = 3 + len(trades)
        print(f"\033[{total_lines}A", end="") # Change the number before the 'A' for how many lines you are printing
    time.sleep(0.00000000000001)

# keep script running
while True:
    time.sleep(0.0000000000000000000000001)