from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt
yf.pdr_override()


dow = pdr.get_data_yahoo("^DJI", "2000-01-04")
kospi = pdr.get_data_yahoo("^KS11", "2000-01-04")



d = (dow.Close / dow.Close.loc["2000-01-04"]) * 100
k = (kospi.Close / kospi.Close.loc["2000-01-04"]) * 100

plt.figure( figsize=(9,5))



plt.plot(dow.index, d, "r--", label="Dow Jones Industrial")
plt.plot(kospi.index, k, 'b', label="KOSPI")
plt.grid(True)
plt.legend(loc="best")
plt.show()
