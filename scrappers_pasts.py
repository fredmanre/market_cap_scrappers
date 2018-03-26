import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from lib.links20162018 import enlaces

# dataframe vacio
df = pd.DataFrame(columns=("Name",
                           "Market_Cap",
                           "Price",
                           "Volume(24h)",
                           "Circulating_Supply",
                           "date"))

# recorremos todos los años con sus respectivos meses
for year in enlaces:
    for month in enlaces[year]:
        enlace = enlaces[year][month]['link']
        fecha = enlaces[year][month]['date']
        # print(year, month, enlace)
        resp = requests.get("https://coinmarketcap.com/")
        html = resp.text
        soup = bs(html, "html.parser")
        # datos extraidos de coinmarketcap
        name = soup.find_all(class_="currency-name-container")
        market_cap = soup.find_all(class_="no-wrap market-cap text-right")
        price = soup.find_all(class_="price")
        volume_24 = soup.find_all(class_="volume")
        circ_sup = soup.find_all(class_="no-wrap text-right circulating-supply")
        date = fecha
        change_24 = soup.find_all(class_="no-wrap percent-change")
        # recorremos 5 monedas para cada año y cada mes
        for i in range(5):
            n = name[i].text
            mc = market_cap[i].text.replace("\n", "").replace(" ", "").replace("$", "")
            p = price[i].text.replace("$", "")
            v = volume_24[i].text.replace("$", "").replace(',', '')
            cs = circ_sup[i].text.split('\n')[2].replace(',', '')
            # df.loc[i] = n, mc, p, v, cs, date
            # dataframe temporal para almacenar una fila de datos
            new_df = pd.DataFrame([
                [n, mc, p, v, cs, date]],
                columns=("Name",
                         "Market_Cap",
                         "Price",
                         "Volume(24h)",
                         "Circulating_Supply",
                         "date"))
            # imprimimos la fila para verificarla
            print(new_df)
            # añadimos la fila al dataframe creado
            df.append(new_df, ignore_index=True)


# print(df)
# convertimos nuestro dataframe a csv
df.to_csv('marketcap_past.csv', mode='r+')
