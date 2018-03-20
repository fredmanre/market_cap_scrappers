import sys
# import psycopg2

from functions import (insert_into_list,
                       extract_with_bs,
                       extract_with_se)

# empbty list
list_json = []

def dtr():
    resource = 'https://www.tokens.net/'
    soup = extract_with_se(resource, 2)
    market_cap = soup.find('span', id='dtr_cap').text[1:]
    current = None
    dict_ = insert_into_list('DynamicTradingRights',
                             'DTR',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)
    
    
def game():
    resource = 'https://blockexplorer.gamecredits.com/home'
    try:
        soup = extract_with_se(resource, 2)
        divs = soup.find_all('div', class_='block-value dark-color')
        current = divs[5].text
        market_cap = None
        dict_ = insert_into_list('GameCredits', 'GAME', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass
        
        
def enj():
    resource = 'https://enjincoin.io/#market'
    try:
        soup = extract_with_se(resource, 2)
        market_cap = soup.find('span', class_='marketcap-usd').text[1:]
        current = soup.find('span', class_='circulating-supply').text
        dict_ = insert_into_list('EnjinCoin', 'ENJ', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass
    
def sls():
    resource = 'http://www.presstab.pw/phpexplorer/SLS/'
    try:
        soup = extract_with_bs(resource)
        td = soup.find_all('td')
        current = td[2].text
        market_cap = td[5].text[1:]
        dict_ = insert_into_list('SaluS', 'SLS', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass
        
        
def sky():
    resource = 'https://explorer.skycoin.net/app/blocks/1'
    try:
        soup = extract_with_se(resource, 2)
        span = soup.find_all('span', class_='-value')
        current = span[1].text
        market_cap = None
        dict_ = insert_into_list('Skycoin', 'SKY', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass
    

def ubq():
    resource = 'https://ubiqscan.io/assets/'
    try:
        soup = extract_with_se(resource, 2)
        current = soup.find('td', id='ubiqAvailableSupply').text
        market_cap = soup.find('td', id='ubiqMarketcap').text
        dict_ = insert_into_list('Ubiq', 'UBQ', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass


def zen():
    resource = 'https://zencash.com/'
    try:
        soup = extract_with_bs(resource)
        divs = soup.find_all('div', class_='stats-data')
        market_cap = None
        current = divs[1].text
        dict_ = insert_into_list('ZenCash', 'ZEN', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass
    
    
def xas():
    resource = 'https://explorer.asch.io/index.html'
    try:
        soup = extract_with_se(resource, 2)
        market_cap = soup.find('span', class_='shizhiNumber').text
        current = None
        dict_ = insert_into_list('Asch', 'XAS', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass
    
    
def spxtx():
    resource = 'https://www.sophiatx.com/es.html'
    try:
        soup = extract_with_se(resource, 2)
        current = soup.find('td', class_='stats_4').text.split(' ')[0]
        market_cap = soup.find('td', class_='stats_6').text.split(' ')[1]
        dict_ = insert_into_list('SophiaTX', 'SPHTX', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass
    
    
def  poa():
    resource = 'https://poaexplorer.com/'
    try:
        soup = extract_with_bs(resource)
        market_cap = soup.find_all('span')[6].text[1:]
        current = soup.find_all('span')[4].text
        dict_ = insert_into_list('POANetwork', 'POA', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass
    

def xby():
    resource = 'https://xtrabytes.global/'
    try:
        soup = extract_with_se(resource, 2)
        market_cap = soup.find('span', id='market_cap_usd').text
        current = soup.find('span', id='available_supply').text
        dict_ = insert_into_list('XTRABYTES', 'XBY', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass
    

def smt():
    resource = 'https://smartmesh.io/smt-token/'
    try:
        soup = extract_with_bs(resource)
        p = soup.find_all('p')
        market_cap = None
        current = p[3].text.split(' ')[2]
        dict_ = insert_into_list('SmartMesh', 'SMT', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass
        
        
coins = dtr(), game(), enj(), sls(), sky(), ubq(), zen(), xas(), spxtx(), poa(), xby(), smt()

for l in list_json:
    print(l, end='\n')