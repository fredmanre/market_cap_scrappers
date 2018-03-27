# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 10:34:10 2018

@author: arnaldo
"""

import requests
import json


def get_data(cant):
    resource = "https://api.coinmarketcap.com/v1/ticker/?limit="
    r = requests.get(resource+"{}".format(cant))
    coins = r.json()
    names_to_sym = {}
    for coin in coins:
        names_to_sym[coin['name']] = coin['symbol']

    return names_to_sym


def main():
    print(get_data(100))

if __name__ == '__main__':
    main()