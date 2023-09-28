import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_sp500_tickers():
    res = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    soup = BeautifulSoup(res.content, "lxml")
    table = soup.find_all("table")[0]
    df = pd.read_html(str(table))
    tickers = list(df[0].Symbol)
    return tickers


tickers = get_sp500_tickers()


def get_history(ticker):
    pass


for ticker in tickers:
    get_history(ticker)
