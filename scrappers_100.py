import json
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# functions
from lib.functions import (insert_into_list,
                           extract_with_bs,
                           extract_with_se)

# path and setup to gekkodriver needed for selenium(linux)
path = "/usr/lib64/chromium/chromedriver"
# list of scrappers
list_json = []

# 7H5PCG22WPH37HUIMTD1TKK6HHN4ZAGYSA
# functions to scrappers in official web pages.
def btc():
    try:
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
        current = (td[12].text).split(' ')[0]
        market_cap = items[0]
        dict_ = insert_into_list(
            'Bitcoin',
            'BTC', market_cap,
            current,
            resource='https://bitcoincharts.com/bitcoin/')
        list_json.append(dict_)
    except:
        pass


def eth():
    try:
        resource = 'https://etherscan.io/stat/supply'
        soup = extract_with_bs(resource)
        spans = soup.find_all('span')
        current = spans[3].string
        market_cap = spans[5].string
        dict_ = insert_into_list('Ethereum',
                                 'ETH',
                                 market_cap,
                                 current,
                                 resource)
        list_json.append(dict_)
    except:
        pass


def eos():
    resource = 'https://etherscan.io/token/EOS#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('eos',
                             'EOS',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def ven():
    resource = 'https://etherscan.io/token/0xd850942ef8811f2a866692a623011bde52a462c1#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('VeChain',
                             'VEN',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def omg():
    resource = 'https://etherscan.io/token/OmiseGo#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('OmiseGo',
                             'OMG',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def snt():
    resource = 'https://etherscan.io/token/StatusNetwork#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Status',
                             'SNT',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def mkr():
    resource = 'https://etherscan.io/token/Maker#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[0].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[0].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Maker',
                             'MKR',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def rhoc():
    resource = 'https://etherscan.io/token/0x168296bb09e24a88805cb9c33356536b980d3fc5#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('RChain',
                             'RHOC',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def wtc():
    resource = 'https://etherscan.io/token/0xb7cb1c96db6b22b0d3d9536e0108d062bd488f74#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Waltonchain',
                             'WTC',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def rep():
    resource = 'https://etherscan.io/token/REP#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Augur',
                             'REP',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def ae():
    resource = 'https://etherscan.io/token/0x5ca9a71b1d01849c0a95490cc00559717fcf0d1d'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Aeternity',
                             'AE',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def zrx():
    resource = 'https://etherscan.io/token/ZRX#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('0x',
                             'ZRK',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def btm():
    resource = 'https://etherscan.io/token/0xcb97e65f07da24d46bcdd078ebebd7c6e6e3d750#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Bytom',
                             'BTM',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def xlm():
    try:
        resource = 'https://stellarchain.io/'
        # chrome options
        soup = extract_with_se(resource, 2)
        current = None
        market_cap = soup.find(id='market_cap_usd').text
        dict_ = insert_into_list('Stellar', 'XLM', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass


def dash():
    try:
        resource = 'https://www.dash.org/network/#section-exchanges'
        soup = extract_with_se(resource, 2)
        current = None
        market_cap = soup.find(id='marketcap_count').text
        dict_ = insert_into_list('Dash', 'DASH', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass


def xem():
    try:
        resource = 'https://nem.io/es/inversores/'
        soup = extract_with_bs(resource)
        div = soup.find_all(class_="network-value")[3].text
        string = str(div)
        items = string.split()
        current = None
        market_cap = items[0]
        dict_ = insert_into_list('NEM', 'XEM', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass


def usdt():
    try:
        resource = 'https://wallet.tether.to/transparency'
        html = extract_with_se(resource, 4)
        td = html.find_all(class_='bold')[0].text
        current = None
        market_cap = td.split('$')[1]
        dict_ = insert_into_list('Tether', 'USDT', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass


def lsk():
    try:
        resource = 'https://explorer.lisk.io/'
        soup = extract_with_se(resource, 2)
        span = soup.find_all(class_='supply')
        market_cap = None
        current = ((span[0].text).split(':'))[1].strip()  # current_supply
        dict_ = insert_into_list('Lisk', 'LSK', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass


def qtum():
    try:
        resource = 'https://explorer.qtum.org/'
        soup = extract_with_se(resource, 4)
        div = soup.find_all('div', class_='label ng-binding')
        current = ((div[1].text).split(' '))[0]
        market_cap = ((div[8].text).split(' '))[0]
        dict_ = insert_into_list('Qtum', 'QTUM', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass


def btg():
    try:
        resource = 'https://btgexplorer.com/'
        soup = extract_with_se(resource, 2)
        span = soup.find(class_='b-market-cap-count ng-binding ng-scope').text
        current = None
        market_cap = span.split('$')[1]
        dict_ = insert_into_list('BitcoinGold', 'BTG', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass


def zec():
    try:
        resource = 'https://explorer.zcha.in/'
        soup = extract_with_se(resource, 2)
        div = soup.find_all(class_='col-md-3 col-xs-6')[-2]
        div = div.find_all('div')[1].text
        current = None
        market_cap = div.split('$')[1]
        dict_ = insert_into_list('Zcash', 'ZEC', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass


def bnb():
    try:
        resource = 'https://info.binance.com/currencies/binance-coin'
        soup = extract_with_bs(resource)
        strongs = soup.find_all('strong')
        market_cap = strongs[3].text
        current = (strongs[5].text).split(' ')[0]
        dict_ = insert_into_list('Binance', 'BNB', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass


def steem():
    try:
        resource = 'https://steemd.com/'
        soup = extract_with_bs(resource)
        divs = soup.find_all('div', class_='val')
        market_cap = divs[0].text.split('$')[1].split('@')[0]
        market_cap = ''.join(market_cap)
        current = ''.join(divs[6].text.split(' ')[0].split(','))
        dict_ = insert_into_list('Steemit', 'STEEM', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass


def bcn():
    try:
        resource = 'https://chainradar.com/bcn/blocks'
        soup = extract_with_bs(resource)
        td = soup.find_all('td', class_='info-data')
        current = ''.join(td[1].text.split("'"))
        market_cap = None
        dict_ = insert_into_list('Bytecoin', 'BCN', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass


def waves():
    try:
        resource = 'http://wavesgo.com/stats'
        soup = extract_with_se(resource, 2)
        spans = soup.find_all('span')
        current = None
        market_cap = spans[4].text
        dict_ = insert_into_list('Waves', 'WAVES', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass


def ppt():
    try:
        resource = 'https://populous.co/'
        soup = extract_with_se(resource, 2)
        market_cap = soup.find_all('span', id='market-cap')[0].text
        current = soup.find_all('span', id='max-supply')[0].text
        dict_ = insert_into_list('Populous', 'PPT', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass


def kmd():
    try:
        resource = 'http://kmd.komodochainz.info/'
        soup = extract_with_se(resource, 2)
        current = soup.find_all('label', id='supply')[0].text
        market_cap = None
        dict_ = insert_into_list('Komodo', 'KMD', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass


def veri():
    try:
        resource = 'http://veritas.veritaseum.com/'
        soup = extract_with_se(resource, 2)
        market_cap = None
        current = soup.find_all('span', id='circulating-supply')[0].text
        dict_ = insert_into_list(
            'Veritaseum', 'VERI', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass


def ardr():
    try:
        resource = 'https://ardor.tools/charts/market/market_cap'
        soup = extract_with_se(resource, 6)
        span = soup.find_all('span')[-1].text
        current = None
        market_cap = span.split('$')[-1]
        dict_ = insert_into_list('Ardor', 'ARDR', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass


def drgn():
    try:
        resource = 'https://dragonchain.com/'
        soup = extract_with_se(resource, 2)
        market_cap = None
        div = soup.find_all(class_='_2ZrCYUsUiY7oxie2nF3JQT')[0].text
        current = div.split(' ')[0]
        dict_ = insert_into_list('Dragonchain', 'DRGN', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass


def hsr():
    try:
        resource = 'http://explorer.h.cash/'
        soup = extract_with_bs(resource)
        em = soup.find_all('em', class_="fs-36 ff-g-black")[0].text
        current = None
        market_cap = em.split('$')[1]
        dict_ = insert_into_list('Hshare', 'HSR', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass


def part():
    try:
        resource = 'https://explorer.particl.io/status'
        soup = extract_with_se(resource, 2)
        td = soup.find_all('td', class_='text-right ng-binding')
        market_cap = None
        current = (td[6].text).split(' ')[0]
        dict_ = insert_into_list('Particl', 'PART', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass


def xzc():
    try:
        resource = 'https://explorer.zcoin.io/'
        soup = extract_with_se(resource, 2)
        current = soup.find_all('label', id='supply')[0].text
        market_cap = None
        dict_ = insert_into_list('Zcoin', 'XZC', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass


def gxs():
    try:
        resource = 'http://block.gxb.io/api/supply'
        soup = extract_with_bs(resource)
        data = json.loads(str(soup))
        market_cap = None
        current = str(data['circulating_supply'])
        dict_ = insert_into_list('GXChain', 'GXS', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass


def emc():
    try:
        resource = 'https://emercoin.com/en/rate'
        soup = extract_with_bs(resource)
        div = soup.find_all('div', class_='cost')
        market_cap = (div[0].find_all('span')[0].text).split(' ')[0]
        current = (div[2].find_all('span')[0].text).split(' ')[0]
        dict_ = insert_into_list('Emercoin', 'EMC', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass


def nxs():
    try:
        resource = 'http://nxsorbitalscan.com/supply'
        soup = extract_with_bs(resource)
        td = soup.find_all('td')
        current = (td[5].text).split(' ')[0]
        market_cap = (td[7].text).split(' ')[0]
        dict_ = insert_into_list('Nexus', 'NXS', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass


# caida
def maid():
    try:
        resource = 'https://www.omniexplorer.info/asset/3'
        soup = extract_with_bs(resource)
        market_cap = None
        current = soup.find_all('span', id='ltotaltokens')[0].text
        dict_ = insert_into_list(
            'MaidSafeCoin', 'MAID', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass


def pay():
    resource = 'https://etherscan.io/token/TenXPay#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('TenX',
                             'PAY',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def req():
    resource = 'https://etherscan.io/token/0x8f8221afbb33998d8584a2b05749ba73c37a938a#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('RequestNetwork',
                             'REQ',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def srn():
    resource = 'https://etherscan.io/token/0x68d57c9a1c35f63e2c83ee8e49a64e9d70528d25#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('SIRILabsToken',
                             'SRN',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def eng():
    resource = 'https://etherscan.io/token/0xf0ee6b27b759c9893ce4f094b49ad28fd15a23e4#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Enigma',
                             'ENG',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def cnd():
    resource = 'https://etherscan.io/token/0xd4c435f5b09f855c3317c8524cb1f586e42795fa#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Cindicator',
                             'CND',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def plr():
    resource = 'https://etherscan.io/token/0xe3818504c1b32bf1557b16c238b2e01fd3149c17#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Pillar',
                             'PLR',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def gvt():
    resource = 'https://etherscan.io/token/0x103c3a209da59d3e7c4a89307e66521e081cfdf0#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('GenesisVision',
                             'GVT',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


# gxs(), maid(),
functions = [
            btc(), eth(), eos(), ven(), omg(), snt(), mkr(), xlm(), dash(),
            xem(), usdt(), lsk(), qtum(), btg(), zec(), bnb(), steem(), bcn(),
            waves(), ppt(), kmd(), ardr(), drgn(), hsr(), part(), rhoc(),
            wtc(), ae(), zrx(), rep(), xzc(), emc(), nxs(), veri(), btm(),
            pay(), req(), srn(), eng(), cnd(), plr(), gvt()]


# functions
print('currencies:', len(list_json))
for i in list_json:
    print(i['symbol'], i['marketcap_usd'],
          i['current_supply'], i['update_time'], end="\n")
