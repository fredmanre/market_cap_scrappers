import sys
import psycopg2


def market_caps():
    """
    Script for get values in official pages over markets and current supply.
    :param function: get functions of market_cap
    :param list_json: returns a list with data refered of criptocurrencys
    """
    insert = "INSERT INTO weight"
    fields = "(name, symbol, marketcap, current_supply, price, source, last_update)"
    values = " VALUES(%s, %s, %s, %s, %s, %s, %s)"
    # connection to database
    try:
        conn = psycopg2.connect(
            "host='localhost' dbname='marketcap_scrapper_test' user='' password=''")
        print('connected to DATABASE!')
    except:
        print('Something failed!')
    # loads all functions and add in list_json
    from functions_marketcap import functions, list_json
    functions
    list_ = list_json
    cur = conn.cursor()
    try:
        for cripto in list_:
            cur.execute(insert + fields + values, (
                cripto['name'],
                cripto['symbol'],
                str(cripto['marketcap_usd']),
                str(cripto['current_supply']),
                None,
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


market_caps()
        