from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

sec= pdr.get_data_yahoo('005930.KS', '2018-05-04')
msft= pdr.get_data_yahoo('MSFT', '2018-05-04')



import matplotlib.pyplot as plt

plt.plot(sec.index,sec.Close,'b', label='Samsung')
plt.plot(msft.index , msft.Close, 'r--', label='MS')
plt.legend(loc='best')
plt.show()





