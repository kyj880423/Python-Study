import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt
yf.pdr_override()

'''
점의 분포가 y = x인 직선 형태에 가까울 수록 직접적인 관계가 있다고 볼 수 있다.
'''

dow = pdr.get_data_yahoo("^DJI", "2000-01-04")
kospi = pdr.get_data_yahoo("^KS11", "2000-01-04")


print(len(dow)); print(len(kospi))

df = pd.DataFrame({'DOW': dow["Close"], "KOSPI" : kospi["Close"]})
print(df)


df = df.fillna(method='bfill') #nan를 뒤의 데이터로 덮어씀.
df = df.fillna(method='ffill') #마지막행의 nan가 있으면 이전의 데이터로 덮어씀.
print(df)




#d = (dow.Close / dow.Close.loc["2000-01-04"]) * 100
#k = (kospi.Close / kospi.Close.loc["2000-01-04"]) * 100

plt.figure( figsize=(9,5))



plt.scatter(df["DOW"], df["KOSPI"], marker=".")
plt.xlabel("Dow Jones Industrial Average")
plt.ylabel("KOSPI")
plt.grid(True)
#plt.legend(loc="best")
plt.show()
