# import pandas as pd
import time
import datetime
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# path and setup to gekkodriver needed for selenium
path = "/usr/lib64/chromium/chromedriver"
# list of scrappers
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
    

def xlm():
    # chrome options
    ch_op = Options()
    ch_op.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=path, chrome_options=ch_op)
    driver.get('https://stellarchain.io/')
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    market_cap = soup.find(id='market_cap_usd').text
    print(market_cap)
    dict_ = {'name': 'Stellar',
         'symbol': 'XLM',
         'marketcap_usd': market_cap,
         'current_supply': None,
         'update_time': datetime.datetime.now().timestamp(),
         'resource': 'https://etherscan.io/stat/supply'
        }
    list_json.append(dict_)

    

btc()
eth()
xlm()
print(list_json)
    
    
