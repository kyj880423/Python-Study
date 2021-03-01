import pandas as pd
import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt


df = pd.read_csv("sise_kakao.csv")
df = df.dropna()
df = df.iloc[0:30]
df.sort_values(by="날짜")

plt.title("Celltrion (Close)")
plt.xticks(rotation=45)
plt.plot(df["날짜"], df["종가"], "co-")
plt.grid(color="gray", linestyle="--")
plt.show()


