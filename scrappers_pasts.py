import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from lib.links20162018 import enlaces
from nametosym import get_data

# dataframe empty
df = pd.DataFrame(columns=("name",
                           "symbol",
                           "marketcap_usd",
                           "price",
                           "volume(24h)",
                           "current_supply",
                           "update_time"))

sym = get_data(200)

# recorremos todos los años con sus respectivos meses
for year in enlaces:
    for month in enlaces[year]:
        enlace = enlaces[year][month]['link']
        fecha = enlaces[year][month]['date']
        # print(year, month, enlace)
        resp = requests.get("https://coinmarketcap.com/")
        html = resp.text
        soup = bs(html, "html.parser")
        # data extract from coinmarketcap
        name = soup.find_all(class_="currency-name-container")
        market_cap = soup.find_all(class_="no-wrap market-cap text-right")
        price = soup.find_all(class_="price")
        volume_24 = soup.find_all(class_="volume")
        circ_sup = soup.find_all(class_="no-wrap text-right circulating-supply")
        date = fecha
        # we travel coins for earch year and each month
        print(year, month)
        for i in range(100):
            n = name[i].text
            s = sym[n]
            mc = market_cap[i].text.replace("\n", "").replace(" ", "").replace("$", "")
            p = price[i].text.replace("$", "")
            v = volume_24[i].text.replace("$", "").replace(',', '')
            cs = circ_sup[i].text.split('\n')[2].replace(',', '')
            print(n, s, mc, p, v, cs)
            # df.loc[i] = n, mc, p, v, cs, date
            # temporary dataframe to save a row data
            new_df = pd.DataFrame([
                [n, s, mc, p, v, cs, date]],
                columns=("name",
                         "symbol",
                         "marketcap_usd",
                         "price",
                         "volume(24h)",
                         "current_supply",
                         "update_time"))
            # print the row to verify
            # print(new_df)
            # add the row in to created dataframe
            df = pd.concat([df, new_df])

df.set_index('date', inplace=True)
df.sort_index(inplace=True)
print(df)
# we convert our dataframe in csv
df.to_csv('marketcap_past.csv', mode="w+")
list_dict = df.read_csv('marketcap_past.csv')
dict_ = list_dict.to_dict('records')
