# for selenium function
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# for BeautifulSoup function
import requests
from bs4 import BeautifulSoup
# for dict function
import datetime

# variables
path = "/usr/lib64/chromium/chromedriver"
now = datetime.datetime.now()

# insert n elements in a dict
def insert_into_list(name, symbol, market_cap, current_supply, resource):
    if current_supply is not None:
        current_supply = float(current_supply.replace(',', ''))
    else:
        current_supply = 0.00
    if market_cap is not None:
        market_cap = float(market_cap.replace(',', ''))
    else:
        market_cap = 0.00
    dict_ = {'name': name,
             'symbol': symbol,
             'marketcap_usd': market_cap,
             'current_supply': current_supply,
             'update_time': now,
             'resource': resource}
    return dict_


# to bring a manipulable web page with selenium and beatifulsoup
def extract_with_se(url, sleep):
    # chrome options
    ch_op = Options()
    ch_op.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=path, chrome_options=ch_op)
    driver.get(url)
    time.sleep(sleep)
    page = driver.page_source
    driver.quit()
    html = BeautifulSoup(page, 'html.parser')
    return html


# to bring a manipulable web page with beatifulsoup
def extract_with_bs(route):
    html = requests.get(route)
    soup = BeautifulSoup(html.text, 'html.parser')
    return soup


# converts a list of tuples into a dict
def convert_dict(list_):
    try:
        dict_ = dict(list_)
        return dict_
    except:
        print("object no convertible in dict")
        return
