import pandas as pd
import psycopg2
import math
import sys


def market_caps():
    """
    Script for get values in official pages over markets and current supply.
    :param function: get functions of market_cap
    :param list_json: returns a list with data refered of criptocurrencys
    """
    list_dict = pd.read_csv('marketcap_past.csv')
    dict_ = list_dict.to_dict('records')
    insert = "INSERT INTO m_pesos"
    fields = "(symbol, marketcap, current_supply, fuente, timestamp_real)"
    values = " VALUES(%s, %s, %s, %s, %s)"
    # connection to database
    try:
        conn = psycopg2.connect(
            "host='localhost' dbname='bita52_des' user='fredmanre' password='perrodeagua'")
        print('connected to DATABASE!')
    except:
        print('Something failed!')
    cur = conn.cursor()
    try:
        for js in dict_:
            if math.isnan(js['current_supply']):
                supply = 0.0
            else:
                supply = js['current_supply']
            cur.execute(insert + fields + values, (js['symbol'],
                                                   js['marketcap_usd'],
                                                   supply,
                                                   'www.coinmarketcap.com',
                                                   js['update_time']))
        print('data inserted with success!')
        conn.commit()
    #except:
    #    print('something fail in query!')
    finally:
        if conn:
            conn.close()
            print('database closed!')


def main():
    market_caps()


if __name__ == '__main__':
    main()