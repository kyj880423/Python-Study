from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt

yf.pdr_override()

sec= pdr.get_data_yahoo("005930.KS", '2018-05-04')
msft= pdr.get_data_yahoo("MSFT", '2018-05-04')


print(type(sec)) # Series 타입
print(sec['Close'])
print("##############")
print(sec.Close)
print("##############")

print(sec.Close.shift(1)) # sec.Close.shift(1) , sec['Close'].shift(1) 동일하네..


sec_dpc = ( sec.Close / sec.Close.shift(1) - 1) * 100
sec_dpc.iloc[0] = 0
print(sec_dpc.head())
msft_dpc = (msft.Close / msft.Close.shift(1) - 1) * 100
msft_dpc.iloc[0] = 0

print(sec.index)
print(sec_dpc)


plt.plot(sec.index, sec_dpc,'b', label='Samsung')
plt.plot(msft.index, msft_dpc, 'r--', label='MS')
plt.legend(loc='best')
plt.grid(True)
plt.show()





