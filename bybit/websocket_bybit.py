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
    return orderbook_data

ws.orderbook_stream(
    depth=50, # orderbook output goes up in $50 increments
    symbol=pair, 
    callback=receive_orderbook # sends message to function
)

# keep script alive
while True:
    time.sleep(0.0000000000000000000000001)