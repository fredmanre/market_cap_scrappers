from lib.functions import (insert_into_list,
                           extract_with_bs,
                           extract_with_se)

# empbty list
list_json = []


def dtr():
    resource = 'https://etherscan.io/token/0xd234bf2410a0009df9c3c63b610c09738f18ccd7#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
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
        soup = extract_with_se(resource, 3)
        current = soup.find('td', id='ubiqAvailableSupply').text
        market_cap = soup.find('td', id='ubiqMarketcap').text.split('$')[1]
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


def sphtx():
    resource = 'https://etherscan.io/token/0x3833dda0aeb6947b98ce454d89366cba8cc55528#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('SophiaTX',
                             'SPHTX',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def  poa():
    resource = 'https://poaexplorer.com/'
    try:
        soup = extract_with_bs(resource)
        market_cap = soup.find_all('span')[7].text[1:]
        current = soup.find_all('span')[4].text
        dict_ = insert_into_list('POANetwork', 'POA', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass


def xby():
    resource = 'https://ethplorer.io/address/0x3833dda0aeb6947b98ce454d89366cba8cc55528'
    try:
        soup = extract_with_se(resource, 2)
        market_cap = None
        current = soup.find_all('span', class_="total-supply-usd")[0].text.split('\xa0')[1]
        dict_ = insert_into_list('XTRABYTES', 'XBY', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass


def smt():
    resource = 'https://etherscan.io/token/0x55f93985431fc9304077687a35a1ba103dc1e081#tokenInfo'
    try:
        soup = extract_with_bs(resource)
        market_cap = soup.find_all('tbody')[0].find_all('td')[5].text.split('$')[1]
        current = soup.find_all('tbody')[0].find_all('td')[8].text.split(' ')[0]
        dict_ = insert_into_list('SmartMesh', 'SMT', market_cap, current, resource)
        list_json.append(dict_)
    except:
        pass


coins = [dtr(), game(), enj(), sls(), sky(), ubq(),
         zen(), xas(), sphtx(), poa(), xby(), smt()]


# print('currencies:', len(list_json))
print('currencies:', len(list_json))
for i in list_json:
    print(i['symbol'],i['marketcap_usd'],i['current_supply'], i['update_time'], end="\n")
