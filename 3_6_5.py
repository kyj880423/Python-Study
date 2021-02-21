import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt
from scipy import stats
yf.pdr_override()

'''

'''

dow = pdr.get_data_yahoo("^DJI", "2000-01-04")
kospi = pdr.get_data_yahoo("^KS11", "2000-01-04")

df = pd.DataFrame({'DOW': dow["Close"], "KOSPI" : kospi["Close"]})
df = df.fillna(method='bfill') #nan를 뒤의 데이터로 덮어씀.
df = df.fillna(method='ffill') #마지막행의 nan가 있으면 이전의 데이터로 덮어씀.

regr = stats.linregress(df["DOW"], df["KOSPI"])
print(regr)

'''
LinregressResult(
slope=0.07775357537860755,  기울기
intercept=446.43436416883014, y절편 
rvalue=0.7673955035136132, 
pvalue=0.0, 
stderr=0.0008779807266173847)

Y의 기대치는 
E(Y) = b + bx = 410.43 + 0.07 * x

따라서 임의의 X값이 주어질 경우 이에 해당하는 Y 값을 예측할 수 있다.
'''
