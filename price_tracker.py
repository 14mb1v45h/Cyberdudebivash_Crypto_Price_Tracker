import requests
import pandas as pd

def fetch_prices(coins):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(coins)}&vs_currencies=usd&include_market_cap=true&include_24hr_change=true"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rows = []
        for coin in coins:
            if coin in data:
                rows.append({
                    'Coin': coin.upper(),
                    'Price (USD)': data[coin]['usd'],
                    'Market Cap (USD)': data[coin]['usd_market_cap'],
                    '24h Change (%)': data[coin]['usd_24h_change']
                })
        df = pd.DataFrame(rows)
        print(df.to_string(index=False))
    else:
        print("API request failed.")

if __name__ == "__main__":
    coins = ['bitcoin', 'ethereum', 'solana', 'ripple', 'cardano']
    fetch_prices(coins)