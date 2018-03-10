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
now = datetime.datetime.now().timestamp()
    
    
def insert_into_list(name, symbol, market_cap, current_supply, resource):
    if len(current_supply) > 0:
        current_supply = current_supply
    else:
        current_supply = None
    dict_ = {
            'name': name,
             'symbol': symbol,
             'marketcap_usd': market_cap,
             'current_supply': current_supply,
             'update_time': now,
             'resource': resource
            }
    return dict_


def extract_with_se(url):
    # chrome options
    ch_op = Options()
    ch_op.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=path, chrome_options=ch_op)
    driver.get(url)
    time.sleep(2)
    html = driver.page_source
    driver.quit()
    return html


def extract_with_bs(route):
    html = requests.get(route)
    soup = BeautifulSoup(html.text, 'html.parser')
    return soup