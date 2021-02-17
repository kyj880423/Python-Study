import pandas as pd
s = pd.Series( [0.0, 3.6, 2.0, 5.8, 4.2, 8.0])
print(s)


ser = pd.Series([6.7, 4.2], index=[6.8, 8.0])
s = s.append(ser)
print(s)

print("##########################")
print(s.iloc[:])


s = s.drop(8.0)
print(s)

print(s.describe())