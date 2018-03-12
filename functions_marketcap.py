import json
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# functions
from functions import (insert_into_list,
                       extract_with_bs,
                       extract_with_se)

# path and setup to gekkodriver needed for selenium(linux)
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


def btg():
    resource = 'https://btgexplorer.com/'
    soup = extract_with_se(resource, 2)
    span = soup.find(class_='b-market-cap-count ng-binding ng-scope').text
    market_cap = span.split('$')[1]
    dict_ = insert_into_list('BitcoinGold', 'BTG', market_cap, '', resource)
    list_json.append(dict_)


def zec():
    resource = 'https://explorer.zcha.in/'
    soup = extract_with_se(resource, 2)
    div = soup.find_all(class_='col-md-3 col-xs-6')[-2]
    div = div.find_all('div')[1].text
    market_cap = div.split('$')[1]
    dict_ = insert_into_list('Zcash', 'ZEC', market_cap, '', resource)
    list_json.append(dict_)


def bnb():
    resource = 'https://info.binance.com/currencies/binance-coin'
    soup = extract_with_bs(resource)
    strongs = soup.find_all('strong')
    market_cap = strongs[3].text
    current = strongs[5].text
    dict_ = insert_into_list('Binance', 'BNB', market_cap, current, resource)
    list_json.append(dict_)


def steem():
    resource = 'https://steemd.com/'
    soup = extract_with_bs(resource)
    table = soup.find_all(
        'table', class_='table table-condensed hash3 ultra-condensed')
    td = table[0].find_all('td')
    market_cap = (td[1].text).split('$')[1]
    current = (td[9].text).split(' ')[0]
    dict_ = insert_into_list('Steemit', 'STEEM', market_cap, current, resource)
    list_json.append(dict_)


def bcn():
    resource = 'https://bytecoin.org/'
    soup = extract_with_se(resource, 2)
    div = soup.find_all('div', class_='hero-content')
    div = div[0].find_all('div', class_='title')
    market_cap = (div[0].text).split('$')[1]
    dict_ = insert_into_list('Bytecoin', 'BCN', market_cap, '', resource)
    list_json.append(dict_)


def waves():
    resource = 'http://wavesgo.com/stats'
    soup = extract_with_se(resource, 2)
    spans = soup.find_all('span')
    market_cap = spans[4].text
    dict_ = insert_into_list('Waves', 'WAVES', market_cap, '', resource)
    list_json.append(dict_)


def ppt():
    resource = 'https://populous.co/'
    soup = extract_with_se(resource, 2)
    market_cap = soup.find_all('span', id='market-cap')[0].text
    current = soup.find_all('span', id='max-supply')[0].text
    dict_ = insert_into_list('Populous', 'PPT', market_cap, current, resource)
    list_json.append(dict_)


def kmd():
    resource = 'http://kmd.komodochainz.info/'
    soup = extract_with_se(resource, 2)
    current = soup.find_all('label', id='supply')[0].text
    market_cap = None
    dict_ = insert_into_list('Komodo', 'KMD', market_cap, current, resource)
    list_json.append(dict_)


def veri():
    resource = 'https://veritas.veritaseum.com/'
    soup = extract_with_se(resource, 2)
    market_cap = None
    current = soup.find_all('span', id='circulating-supply')[0].text
    dict_ = insert_into_list(
        'Veritaseum', 'VERI', market_cap, current, resource)
    list_json.append(dict_)


def ardr():
    resource = 'https://ardor.tools/charts/market/market_cap'
    soup = extract_with_se(resource, 6)
    span = soup.find_all('span')[-1].text
    market_cap = span.split('$')[-1]
    dict_ = insert_into_list('Ardor', 'ARDR', market_cap, '', resource)
    list_json.append(dict_)
    
    
def drgn():
    resource = 'https://dragonchain.com/'
    soup = extract_with_se(resource, 2)
    market_cap = None
    div = soup.find_all(class_='_2ZrCYUsUiY7oxie2nF3JQT')[0].text
    current = div.split(' ')[0]
    dict_ = insert_into_list('Dragonchain', 'DRGN', market_cap, current, resource)
    list_json.append(dict_)


def hsr():
    resource = 'http://explorer.h.cash/'
    soup = extract_with_bs(resource)
    em = soup.find_all('em', class_="fs-36 ff-g-black")[0].text
    market_cap = em.split('$')[1]
    dict_ = insert_into_list('Hshare', 'HSR', market_cap, '', resource)
    list_json.append(dict_)


def part():
    resource = 'https://explorer.particl.io/status'
    soup = extract_with_se(resource, 2)
    td = soup.find_all('td', class_='text-right ng-binding')
    market_cap = None
    current = (td[6].text).split(' ')[0]
    dict_ = insert_into_list('Particl', 'PART', market_cap, current, resource)
    list_json.append(dict_)
    
    
def zcoin():
    resource = 'https://explorer.zcoin.io/'
    soup = extract_with_se(resource, 2)
    current = soup.find_all('label', id='supply')[0].text
    market_cap = None
    dict_ = insert_into_list('Zcoin', 'XZC', market_cap, current, resource)
    list_json.append(dict_)
    
    
def gxs():
    resource = 'http://block.gxb.io/api/supply'
    soup = extract_with_bs(resource)
    data = json.loads(str(soup))
    market_cap = None
    current = str(data['circulating_supply'])
    dict_ = insert_into_list('GXChain', 'GXA', market_cap, current, resource)
    list_json.append(dict_)
    

def emc():
    resource = 'https://emercoin.com/en/rate'
    soup = extract_with_bs(resource)
    div = soup.find_all('div', class_='cost')
    market_cap = (div[0].find_all('span')[0].text).split(' ')[0]
    current = (div[2].find_all('span')[0].text).split(' ')[0]
    dict_ = insert_into_list('Emercoin', 'EMC', market_cap, current, resource)
    list_json.append(dict_)
    
    
def nxs():
    resource = 'http://nxsorbitalscan.com/supply'
    soup = extract_with_bs(resource)
    td = soup.find_all('td')
    current = (td[2].text).split(' ')[0]
    market_cap = (td[4].text).split(' ')[0]
    dict_ = insert_into_list('Nexus', 'nxs', market_cap, current, resource)
    list_json.append(dict_)
    

def maid():
    resource = 'http://omnichest.info/lookupsp.aspx?sp=3'
    soup = extract_with_bs(resource)
    markeet_cap = None
    current = soup.find_all('span', id='ltotaltokens')[0].text
    dict_ = insert_into_list('MaidSafeCoin', 'MAID', markeet_cap, current, resource)
    list_json.append(dict_)
    

functions = btc(), eth(), xlm(), dash(), xem(), usdt(),
lsk(), qtum(), btg(), zec(), bnb(), steem(), bcn(),
waves(), ppt(), kmd(), veri(), ardr(), hsr(), part(),
zcoin(), gxs(), emc(), nxs(), maid()
functions
print('currencies:', list_json)
