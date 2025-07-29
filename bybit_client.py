from pybit.unified_trading import HTTP
from config import BYBIT_API_KEY, BYBIT_API_SECRET

client = HTTP(
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
)

def place_order(symbol, side, qty, entry_price):
    try:
        client.place_order(
            category="linear",
            symbol=symbol,
            side=side,
            orderType="Market",
            qty=qty,
            takeProfit=round(entry_price * 1.02, 4),
            stopLoss=round(entry_price * 0.985, 4),
        )
        return True
    except Exception as e:
        return str(e)
