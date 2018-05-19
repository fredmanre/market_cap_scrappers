from lib.functions import (insert_into_list,
                           extract_with_bs,
                           extract_with_se)

# empbty list
list_json = []


def storm():
    resource = 'https://etherscan.io/token/0xd0a4b8946cb52f0661273bfbc6fd0e0c75fc6433'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Storm',
                             'STORM',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def agi():
    resource = 'https://etherscan.io/token/0x8eb24319393716668d768dcec29356ae9cffe285#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('SingularityNET',
                             'AGI',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


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


def storj():
    resource = 'https://etherscan.io/token/Storj#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Storj',
                             'STORJ',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def gno():
    resource = 'https://etherscan.io/token/Storj#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Gnosis',
                             'GNO',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def mana():
    resource = 'https://etherscan.io/token/decentraland#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Decentraland',
                             'MANA',
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


def cvc():
    resource = 'https://etherscan.io/token/civic#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Civic',
                             'CVC',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def qsp():
    resource = 'https://etherscan.io/token/0x99ea4db9ee77acd40b119bd1dc4e33e1c070b80d#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Quantstamp',
                             'QSP',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def theta():
    resource = 'https://etherscan.io/token/0x3883f5e181fccaF8410FA61e12b59BAd963fb645#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('ThetaToken',
                             'THETA',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def mco():
    resource = 'https://etherscan.io/token/Monaco#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Monaco',
                             'MCO',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def ant():
    resource = 'https://etherscan.io/token/Aragon#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Aragon',
                             'ANT',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def rdn():
    resource = 'https://etherscan.io/token/0x255aa6df07540cb5d3d297f0d0d4d84cb52bc8e6#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('RaidenNetworkToken',
                             'RDN',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def san():
    resource = 'https://etherscan.io/token/SAN#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('SantimentNetworkToken',
                             'SAN',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def ppp():
    resource = 'https://etherscan.io/token/0xc42209aCcC14029c1012fB5680D95fBd6036E2a0#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('PayPie',
                             'PPP',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def wax():
    resource = 'https://etherscan.io/token/0x39Bb259F66E1C59d5ABEF88375979b4D20D98022#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('WAX',
                             'WAX',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def poe():
    resource = 'https://etherscan.io/token/0x0e0989b1f9b8a38983c2ba8053269ca62ec9b195#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Po.et',
                             'POE',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def gnx():
    resource = 'https://etherscan.io/token/0x6ec8a24cabdc339a06a172f8223ea557055adaa5#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Genaro Network',
                             'GNX',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def xpa():
    resource = 'https://etherscan.io/token/0x90528aeb3a2b736b780fd1b6c478bb7e1d643170#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('XPA',
                             'XPA',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def abt():
    resource = 'https://etherscan.io/token/0xb98d4c97425d9908e66e53a6fdf673acca0be986#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('ArcBlock',
                             'ABT',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def evn():
    resource = 'https://etherscan.io/token/0xd780ae2bf04cd96e577d3d014762f831d97129d0#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Envion',
                             'EVN',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def hpb():
    resource = 'https://etherscan.io/token/0x38c6a68304cdefb9bec48bbfaaba5c5b47818bb2#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('HighPerformanceBlockchain',
                             'HPB',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def nuls():
    resource = 'https://etherscan.io/token/0xb91318f35bdb262e9423bc7c7c2a3a93dd93c92c#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[0].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[0].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('HighPerformanceBlockchain',
                             'HPB',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def cs():
    resource = 'https://etherscan.io/token/0x46b9ad944d1059450da1163511069c718f699d31#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Credits',
                             'CS',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def edg():
    resource = 'https://etherscan.io/token/Edgeless#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Edgeless',
                             'EDG',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def adx():
    resource = 'https://etherscan.io/token/0x4470bb87d77b963a013db939be332f927f2b992e#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Adex',
                             'ADX',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def fsn():
    resource = 'https://etherscan.io/token/0xd0352a019e9ab9d757776f532377aaebd36fd541#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Fusion',
                             'FSN',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def vee():
    resource = 'https://etherscan.io/token/0x340d2bde5eb28c1eed91b2f790723e3b160613b7#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Blockv',
                             'VEE',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def lend():
    resource = 'https://etherscan.io/token/0x80fB784B7eD66730e8b1DBd9820aFD29931aab03#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('ETHLend',
                             'LEND',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def blz():
    resource = 'https://etherscan.io/token/0x5732046a883704404f284ce41ffadd5b007fd668#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Blezelle',
                             'BLZ',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def bix():
    resource = 'https://etherscan.io/token/0xb3104b4b9da82025e8b9f8fb28b3553ce2f67069#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('BiBoxToken',
                             'BIX',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def c20():
    resource = 'https://etherscan.io/token/0x26e75307fc0c021472feb8f727839531f112f317#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('CRYPTO20',
                             'c20',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def spank():
    resource = 'https://etherscan.io/token/0x42d6622dece394b54999fbd73d108123806f6a18#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('SpankChain',
                             'SPANK',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def rcn():
    resource = 'https://etherscan.io/token/0xf970b8e36e23f7fc3fd752eea86f8be8d83375a6#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('RipioCreditNetwork',
                             'RCN',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def jnt():
    resource = 'https://etherscan.io/token/0xa5fd1a791c4dfcaacc963d4f73c6ae5824149ea7#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('JibrelNetwork',
                             'JNT',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def data():
    resource = 'https://etherscan.io/token/0x0cf0ee63788a0849fe5297f3407f701e122cc023#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('StreamrDATAcoin',
                             'DATA',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def ost():
    resource = 'https://etherscan.io/token/0x2c4e8f2d746113d0696ce89b35f0d8bf88e0aeca#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('OST',
                             'OST',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def snm():
    resource = 'https://etherscan.io/token/0x983f6d60db79ea8ca4eb9968c6aff8cfa04b3c63#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('SONM',
                             'SNM',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def tel():
    resource = 'https://etherscan.io/token/0x85e076361cc813a908ff672f9bad1541474402b2#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Telcoin',
                             'TEL',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def amb():
    resource = 'https://etherscan.io/token/0x4dc3643dbc642b72c158e7f3d2ff232df61cb6ce#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Ambrosus',
                             'AMB',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def vibe():
    resource = 'https://etherscan.io/token/0xe8ff5c9c75deb346acac493c463c8950be03dfba#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[0].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[0].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('VIBE',
                             'VIBE',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def trac():
    resource = 'https://etherscan.io/token/0xaa7a9ca87d3694b5755f213b5d04094b8d0f0a6f#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('OriginTrail',
                             'TRAC',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def ast():
    resource = 'https://etherscan.io/token/0x27054b13b1b798b345b591a4d22e6562d47ea75a#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('AirSwap',
                             'AST',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def wings():
    resource = 'https://etherscan.io/token/0x667088b212ce3d06a1b553a7221E1fD19000d9aF#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Wings',
                             'WINGS',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def qrl():
    resource = 'https://etherscan.io/token/0x697beac28b09e122c4332d163985e8a73121b97f#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('QuantumResistantLedger',
                             'QRL',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def kick():
    resource = 'https://etherscan.io/token/0x697beac28b09e122c4332d163985e8a73121b97f#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('KickCoin',
                             'KICK',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def utnp():
    resource = 'https://etherscan.io/token/0x9e3319636e2126e3c0bc9e3134AEC5e1508A46c7#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Universa',
                             'UTNP',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def edo():
    resource = 'https://etherscan.io/token/0xced4e93198734ddaff8492d525bd258d49eb388e#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Eidoo',
                             'EDO',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def taas():
    resource = 'https://etherscan.io/token/Taas#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('TaaS',
                             'TAAS',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def appc():
    resource = 'https://etherscan.io/token/0x1a7a8bd9106f2b8d977e08582dc7d24c723ab0db#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('AppCoins',
                             'APPC',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def mln():
    resource = 'https://etherscan.io/token/Melon#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Melon',
                             'MLN',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def sngls():
    resource = 'https://etherscan.io/token/SNGLS#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('SingularDTV',
                             'SNGLS',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def itc():
    resource = 'https://etherscan.io/token/0x5e6b6d9abad9093fdc861ea1600eba1b355cd940#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[0].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[0].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('IoT',
                             'ITC',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def gto():
    resource = 'https://etherscan.io/token/0xc5bbae50781be1669306b9e001eff57a2957b09d#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Gifto',
                             'DTO',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def mgo():
    resource = 'https://etherscan.io/token/0x40395044Ac3c0C57051906dA938B54BD6557F212#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('MobileGo',
                             'MGO',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def ins():
    resource = 'https://etherscan.io/token/0x5b2e4a700dfbc560061e957edec8f6eeeb74a320#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('INSEcosystem',
                             'INS',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


def utk():
    resource = 'https://etherscan.io/token/0x70a72833d6bf7f508c8224ce59ea1ef3d0ea3a38#tokenInfo'
    soup = extract_with_bs(resource)
    market_cap = soup.find_all('tbody')[1].find_all('td')[5].text.split('$')[1]
    current = soup.find_all('tbody')[1].find_all('td')[8].text.split(' ')[0]
    dict_ = insert_into_list('Utrust',
                             'UTK',
                             market_cap,
                             current,
                             resource)
    list_json.append(dict_)


coins = [storm(), agi(), dtr(), storj(), gno(), mana(), cvc(), game(), enj(),
         sls(), sky(), ubq(), zen(), xas(), sphtx(), poa(), xby(), smt(),
         qsp(), theta(), mco(), ant(), rdn(), san(), ppp(), wax(), poe(),
         gnx(), xpa(), abt(), evn(), hpb(), nuls(), cs(), edg(), adx(), fsn(),
         vee(), lend(), blz(), bix(), c20(), spank(), rcn(), jnt(), data(),
         ost(), snm(), amb(), tel(), vibe(), trac(), ast(), wings(), qrl(),
         kick(), utnp(), edo(), taas(), appc(), mln(), sngls(), itc(), gto(),
         mgo(), ins(), utk()]


# print('currencies:', len(list_json))
print('currencies:', len(list_json))
for i in list_json:
    print(i['symbol'], i['marketcap_usd'],
          i['current_supply'], i['update_time'], end="\n")
