# import pandas as pd
import requests
from bs4 import BeautifulSoup
import datetime


list_json = []


def btc():
    html = requests.get('https://bitcoincharts.com/bitcoin/')
    soup = BeautifulSoup(html.text, 'html.parser')
    td = soup.find_all('td')
    values = td[13]
    list_ = []
    for i in values:
        list_.append(i)
    market = list_[0]
    string = str(market)
    items = string.split()
    market_cap = items[0]
    dict_ = {'name': 'Bitcoin',
             'symbol': 'BTC',
             'marketcap_usd': market_cap,
             'current_supply': None,
             'update_time': datetime.datetime.now().timestamp(),
             'resource': 'https://bitcoincharts.com/bitcoin/'
            }
    list_json.append(dict_)

    

def eth():
    html = requests.get('https://etherscan.io/stat/supply')
    soup = BeautifulSoup(html.text, 'html.parser')
    spans = soup.find_all('span')
    market_cap = spans[3].string
    dict_ = {'name': 'Ethereum',
             'symbol': 'ETH',
             'marketcap_usd': market_cap,
             'current_supply': None,
             'update_time': datetime.datetime.now().timestamp(),
             'resource': 'https://etherscan.io/stat/supply'
            }
    list_json.append(dict_)
    


btc()
eth()
print(list_json)
    
    
