import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt
from scipy import stats
yf.pdr_override()

'''

'''

dow = pdr.get_data_yahoo("^DJI", "2000-01-04")
print(dow)
kospi = pdr.get_data_yahoo("^KS11", "2000-01-04")
print(kospi)
df = pd.DataFrame({'X': dow["Close"], "Y" : kospi["Close"]})
df = df.fillna(method='bfill') #nan를 뒤의 데이터로 덮어씀.
df = df.fillna(method='ffill') #마지막행의 nan가 있으면 이전의 데이터로 덮어씀.

regr = stats.linregress(df.X, df.Y)
print(regr);
regr_line = f'Y ={ regr.slope:.2f} * X + {regr.intercept: .2f}' # 범례식에 회귀식을 표시하는 레이블 문자'

plt.figure(figsize=(7,7))
plt.plot(df.X, df.Y, '.') #산점도를 작은 원으로 나타낸다.
plt.plot(df.X, regr.slope * df.X + regr.intercept, 'r')
plt.legend(['DOW x KOSPI', regr_line])
plt.show()