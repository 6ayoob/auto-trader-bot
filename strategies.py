def momentum_strategy(price_data, rsi):
    if rsi < 30 and price_data['volume_change_15m'] > 1.5:
        return "BUY"
    elif rsi > 70:
        return "SELL"
    return "HOLD"

def swing_strategy(price_data, rsi, ma20, ma50, market_cap):
    if 30 < rsi < 50 and price_data['price'] > ma20 and price_data['price'] > ma50 and market_cap > 10_000_000:
        return "BUY"
    elif rsi > 70:
        return "SELL"
    return "HOLD"
