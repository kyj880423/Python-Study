import pandas as pd
df = pd.DataFrame({'KOSPI':[1915,1961,2026,2467,2041],
             'KOSDAQ' : [542,682,631,798,675]})
print(df)
print("#############################")
df = pd.DataFrame({'KOSPI':[1915,1961,2026,2467,2041],
             'KOSDAQ' : [542,682,631,798,675]},
                  index=[2014,2015,2016,2017,2018]
                  )
print(df)

print("#############################")

print(df.describe())
print("#############################")
print(df.info())

print("#############################")
print("#############################")
print("#############################")
kospi = pd.Series([1915,1961,2026,2467,2041], index=[2014,2015,2016,2017,2018], name="KOSPI")
kosdaq = pd.Series([542,682,631,798,675], index=[2014,2015,2016,2017,2018], name ="KOSDAQ")

df = pd.DataFrame({kospi.name : kospi, kosdaq.name:kosdaq})
print(df)