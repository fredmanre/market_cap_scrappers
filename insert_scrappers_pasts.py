import psycopg2
import pandas as pd

def market_caps():
    """
    Script for get values in official pages over markets and current supply.
    :param function: get functions of market_cap
    :param list_json: returns a list with data refered of criptocurrencys
    """
    insert = "INSERT INTO m_pesos"
    fields = "(symbol, marketcap, current_supply, fuente, timestampfield)"
    values = " VALUES(%s, %s, %s, %s, %s)"
    # connection to database
    try:
        conn = psycopg2.connect(
            "host='localhost' dbname='bita52_des' user='fredmanre' password='perrodeagua'")
        print('connected to DATABASE!')
    except:
        print('Something failed!')
    cur = conn.cursor()
    # file .csv with data of the past 
    list_dict = pd.read_csv('marketcap_past.csv')
    dict_ = list_dict.to_dict('records')
    # cur.execute("select symbol, id_m_criptomoneda from m_criptomoneda")
    # b = cur.fetchall()
    # c = dict(b)  # id_m_criptomoneda from m_criptomoneda
    # loads all functions and add in list_json
    try:
        for cripto in list_:
            cur.execute(insert + fields + values, (
                cripto['symbol'],
                cripto['marketcap_usd'],
                cripto['current_supply'],
                cripto['resource'],
                cripto['update_time']))
        print('data inserted with success!')
        conn.commit()
    except:
        print('something failed in query!')
        sys.exit(1)
    finally:
        if conn:
            conn.close()
            print('database closed!')


def main():
    market_caps()


if __name__ == '__main__':
    main()