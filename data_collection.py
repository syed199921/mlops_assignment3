import requests
import csv
import os
from datetime import datetime

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {"vs_currency": "usd", "per_page": 10, "page": 1} 

response = requests.get(url, params=params)
data = response.json()

filename = "raw_crypto_data.csv"
fieldnames = ['timestamp', 'id', 'symbol', 'current_price', 'market_cap', 'total_volume',
              'price_change_percentage_24h', 'circulating_supply']

write_header = not os.path.exists(filename)

with open(filename, "a", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    if write_header:
        writer.writeheader()

    for coin in data:
        writer.writerow({
            'timestamp': datetime.utcnow().isoformat(),
            'id': coin['id'],
            'symbol': coin['symbol'],
            'current_price': coin['current_price'],
            'market_cap': coin['market_cap'],
            'total_volume': coin['total_volume'],
            'price_change_percentage_24h': coin['price_change_percentage_24h'],
            'circulating_supply': coin['circulating_supply']
        })

print("Live crypto data fetched and logged.")
