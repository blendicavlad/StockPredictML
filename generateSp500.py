import bs4 as bs
import datetime as dt
import os
import pickle
import pandas as pd
import pandas_datareader.data as web
import requests
import fix_yahoo_finance as yf
yf.pdr_override()

def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, "lxml")
    table = soup.find('table', {'class':'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)

    with open("sp500tickers.pickle", "wb") as f:
        pickle.dump(tickers, f)

    print(tickers)

    return tickers

#save_sp500_tickers()
def get_data_from_google(reload_sp500=False):
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open("sp500tickers.pickle", "rb") as f:
            tickers = pickle.load(f)
    if not os.path.exists('stck_dfs'):
        os.makedirs('stock_dfs')

    start = dt.datetime(2014,1,1)
    end = dt.datetime(2017,12,31)
    for ticker in tickers:
        print(ticker)
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            try:
                df = yf.download(ticker.replace('.', '-'), start, end)
                df.to_csv('stock_dfs/{}.csv'.format(ticker))
            except:
                print("Datareading error")
        else:
            print('Already have {}'.format(ticker))

#get_data_from_google()
