from pybit.unified_trading import HTTP

# calculate server response time
session = HTTP(testnet=False)
print(session.get_server_time())