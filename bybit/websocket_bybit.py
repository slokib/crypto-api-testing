#import all needed SDK
import time
import pybit.unified_trading
from pybit.unified_trading import WebSocket
import bybit_symbols as b

# REPLACE b.btc with what other pairs are available in the bybit_symbols file
pair = b.sol

# assign ws as Websocket with testnet disabled and channel type as linear futures
ws = WebSocket(
    testnet = False,
    channel_type= "linear"
)

# add function to use to handle once orderbook data is received
def receive_orderbook(message):
    if "data" not in message:
        return
    
    orderbook_data = message["data"]
    orderbook_data_ask = message["data"]["a"] # all asks in the orderbook
    orderbook_data_bid = message["data"]["b"] # all bids in the orderbook
    print(orderbook_data)
    # returns a snapshot of orderbook, than additions to the orderbook after

ws.orderbook_stream(
    depth=50, # orderbook output goes up in $50 increments
    symbol=pair, 
    callback=receive_orderbook # sends message to function
)

def receive_recent_trades(message):
    if "data" not in message:
        return
    
    # loop through data as keys & values are inside a dictionary inside of a list
    for trade in message["data"]:
        # unpack dict values
        timestamp, symbol, side, size, price, direction, *rest = trade.values()
    print(f"{side} trade on {symbol}: {size} @ {price}")
    # expected output: Buy trade on BTCUSDT: 3 @ 79000.0

ws.trade_stream(
    symbol=pair,
    callback=receive_recent_trades
)

# keep script running
while True:
    time.sleep(0.0000000000000000000000001)