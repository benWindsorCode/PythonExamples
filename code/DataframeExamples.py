import pandas as pd
import numpy as np

df1 = {'a': [1, 2, 3], 'b': [4, 2, 3]}
df1 = pd.DataFrame(df1)

print(df1)

df2 = pd.DataFrame(data=[[5, 6], [8, 9]], columns=['a', 'b'])

print(df2)

rowConcat = pd.concat([df1, df2])
print(rowConcat)

df3 = pd.DataFrame(data=[[5, 6], [8, 9]], columns=['c', 'd'])
colConcat = pd.concat([df1, df3], axis=1)
print(colConcat)

noNan = colConcat.dropna()
print(noNan)

filledNan = colConcat.fillna(method='ffill')
print(filledNan)

filledNan['rollingAvg'] = filledNan['b'].rolling(3).mean()
filledNan['rollingStd'] = filledNan['a'].rolling(3).std()

print(filledNan)

filledNan['new'] = pd.Series([1,3], index=[0,2])

print(filledNan)

filledNan.loc[3] = [1,2,3,4,5,6,7]
filledNan.loc[4] = [1,2,3,4,5,6,7]

print(filledNan)

print(filledNan.loc[3])

filledNan = filledNan.drop_duplicates()
print(filledNan)

filledNan.drop('new', inplace=True, axis=1)
print(filledNan)

for idx, row in filledNan.iterrows():
    print(f"row.a {row.a}")

ser1 = pd.Series([1, 3, 5, 7, 9])
ser2 = pd.Series([1, 4, 5, 9, 12])

union = pd.Series(np.union1d(ser1, ser2))
print(union)

inOneButNotTwo = ser1[~ser1.isin(ser2)]
print(inOneButNotTwo)