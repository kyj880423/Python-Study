import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import io

pd.set_option('display.max_row', 2000)

krx_list = pd.read_html("상장법인목록 (1).xls")[0]
krx_list.종목코드 = krx_list.종목코드.map('{:06d}'.format)

df = krx_list.sort_values(by='종목코드')


print(df[df["회사명"].str.contains('카카오')])



last_page = 523
headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
}


df = pd.DataFrame()
sise_url = "https://finance.naver.com/item/sise_day.nhn?code=035720"
for page in range(1, int(last_page) + 1):
    page_url = "{}&page={}".format(sise_url, page)
    print(page_url)

    r = requests.get(page_url, headers=headers)
    dd = pd.read_html(io.StringIO(r.text), header=0)[0]
    df = df.append(dd)

df.dropna()

df.to_csv("sise_kakao.csv")




