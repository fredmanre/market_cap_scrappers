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
        dict_ = insert_into_list('GameCredits', 'GAME', markket_cap, current, resource)
        list_json.append(game)
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
        