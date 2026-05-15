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

while True:
    time.sleep(0.0000000000000000000000001)