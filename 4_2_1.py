import pandas as pd
pd.set_option('display.max_row', 2000)

krx_list = pd.read_html("상장법인목록 (1).xls")[0]
krx_list.종목코드 = krx_list.종목코드.map('{:06d}'.format)

df = krx_list.sort_values(by='종목코드')


#print(df)

print(df[df["회사명"].str.contains('카카오')])
#print(df.filter(like="삼성", axis=1))


from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

'''
URL 오픈시 일별 시세가 조회되지않는다. BeautifulSoap를 통해 리턴받은 html은 아래와 같은 페이지를 리턴한다. 왜일까
방문하시려는 페이지의 주소가 잘못 입력되었거나,
페이지의 주소가 변경 혹은 삭제되어 요청하신 페이지를 찾을 수 없습니다.
입력하신 주소가 정확한지 다시 한번 확인해 주시기 바랍니다.

SSL을 추가하면 되지않을까 했는데 결과는 똑같았다.
import ssl
context = ssl._create_unverified_context()

SSL 문제는 아니고 header에 usergent 속성을 주니 파싱가능한 html 텍스트가 리턴은 가능
하지만 내부 데이터는 없다.
'''







headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
}

#payload = {'as_epq': 'James Clark', 'tbs':'cdr:1,cd_min:01/01/2015,cd_max:01/01/2015', 'tbm':'nws'}

code = "035720" #카카오
#url = "https://finance.naver.com/item/sise_day.nhn?code={code}&page=1".format(code=code)
url = "https://finance.naver.com/item/sise_day.nhn?code=035720&page=1"

r = requests.get(url, headers=headers)
html = BeautifulSoup(r.text, "lxml")
print(html)
pgrr = html.find("td", class_="pgRR")
# 왜 None가 리턴될까?
if pgrr == None:
    print("Nothing")
else:
    print(pgrr.a['href'])
s = str(pgrr.a["href"]).split("=")
last_page = s[-1]

print(last_page)



df = pd.DataFrame()
sise_url = "https://finance.naver.com/item/sise_day.nhn?code=035720"
for page in range(1, int(last_page) + 1):
    page_url = "{}&page={}".format(sise_url, page)
    print(page_url)
    dd = pd.read_html(page_url, header=0)[0]
    df = df.append(dd)

df.dropna()

df.to_csv("sise_kakao.csv")




