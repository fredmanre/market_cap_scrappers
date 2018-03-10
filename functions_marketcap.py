import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# functions
from functions import (insert_into_list,
                       extract_with_bs,
                       extract_with_se)
# for dict function

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
    dict_ = insert_into_list(
        'Bitcoin',
        'BTC', market_cap,
        '',
        resource='https://bitcoincharts.com/bitcoin/')
    list_json.append(dict_)


def eth():
    resource = 'https://etherscan.io/stat/supply'
    soup = extract_with_bs(resource)
    spans = soup.find_all('span')
    market_cap = spans[3].string
    dict_ = insert_into_list('Ethereum',
                             'ETH',
                             market_cap,
                             '',
                             resource)
    list_json.append(dict_)


def xlm():
    resource = 'https://stellarchain.io/'
    # chrome options
    soup = extract_with_se(resource, 2)
    market_cap = soup.find(id='market_cap_usd').text
    dict_ = insert_into_list('Stellar', 'XLM', market_cap, '', resource)
    list_json.append(dict_)


def dash():
    resource = 'https://www.dash.org/network/#section-exchanges'
    soup = extract_with_se(resource, 2)
    market_cap = soup.find(id='marketcap_count').text
    dict_ = insert_into_list('Dash', 'DASH', market_cap, '', resource)
    list_json.append(dict_)


def xem():
    resource = 'https://nem.io/es/inversores/'
    soup = extract_with_bs(resource)
    div = soup.find_all(class_="network-value")[3].text
    string = str(div)
    items = string.split()
    market_cap = items[0]
    dict_ = insert_into_list('NEM', 'XEM', market_cap, '', resource)
    list_json.append(dict_)


def usdt():
    resource = 'https://wallet.tether.to/transparency'
    html = extract_with_se(resource, 4)
    td = html.find_all(class_='bold')[0].text
    market_cap = td.split('$')[1]
    dict_ = insert_into_list('Tether', 'USDT', market_cap, '', resource)
    list_json.append(dict_)


def lsk():
    resource = 'https://explorer.lisk.io/'
    soup = extract_with_se(resource, 2)
    span = soup.find_all(class_='supply')
    market_cap = None
    current = ((span[0].text).split(':'))[1].strip()  # current_supply
    dict_ = insert_into_list('Lisk', 'LSK', market_cap, current, resource)
    list_json.append(dict_)


def qtum():
    resource = 'https://explorer.qtum.org/'
    soup = extract_with_se(resource, 2)
    div = soup.find_all('div', class_='label ng-binding')
    current = ((div[1].text).split(' '))[0]
    market_cap = ((div[8].text).split(' '))[0]
    dict_ = insert_into_list('Qtum', 'QTUM', market_cap, current, resource)
    list_json.append(dict_)

qtum()
print(list_json)
