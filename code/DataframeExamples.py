import pandas as pd

df1 = {'a': [1, 2, 3], 'b': [4, 2, 3]}
df1 = pd.DataFrame(df1)

print(df1)

df2 = pd.DataFrame(data=[[5, 6], [8, 9]], columns=['a', 'b'])

print(df2)

rowConcat = pd.concat([df1, df2])
print(rowConcat)

colConcat = pd.concat([df1, df2], axis=1)
print(colConcat)