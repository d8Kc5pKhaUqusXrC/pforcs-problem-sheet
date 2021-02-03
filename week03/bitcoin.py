# bitcoin.py
# This program prints the current Bitcoin price
# author: Mark Brislane

import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
returnedData = requests.get(url)
bitCoinDict: dict = returnedData.json()

# Loop through the dict, printing the Currency Code & Rate (2 decimal places) for ech entry
for currency in bitCoinDict['bpi'].items():
    print(currency[1]['code'] + " " + "{:.2f}".format(currency[1]['rate_float']))
