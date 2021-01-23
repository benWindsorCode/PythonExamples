import pandas as pd
import numpy as np

# Useful pandas examples: https://www.javatpoint.com/python-pandas-interview-questions

# Creating a DataFrame from a dictionary
df1 = {'a': [1, 2, 3], 'b': [4, 2, 3]}
df1 = pd.DataFrame(df1)

print(df1)

# Creating a dataframe from a nested array
df2 = pd.DataFrame(data=[[5, 6], [8, 9]], columns=['a', 'b'])

print(df2)

# Concat one dataframe below the other, rows on top of rows
rowConcat = pd.concat([df1, df2])
print(rowConcat)

# Concat one dataframe side by side with the other, cols added on
df3 = pd.DataFrame(data=[[5, 6], [8, 9]], columns=['c', 'd'])
colConcat = pd.concat([df1, df3], axis=1)
print(colConcat)

# Drop any rows with nans
noNan = colConcat.dropna()
print(noNan)

# Backfill any rows with nans in
filledNan = colConcat.fillna(method='ffill')
print(filledNan)

# Calculate rolling mean and stddev
filledNan['rollingAvg'] = filledNan['b'].rolling(3).mean()
filledNan['rollingStd'] = filledNan['a'].rolling(3).std()

print(filledNan)

# Add a row from a series
filledNan['new'] = pd.Series([1, 3], index=[0, 2])

print(filledNan)

# Add a row by index
filledNan.loc[3] = [1, 2, 3, 4, 5, 6, 7]

filledNan.loc[4] = [1, 2, 3, 4, 5, 6, 7]

print(filledNan)

# Locate a row by index
print(filledNan.loc[3])

# Drop the duplicate row that was added
filledNan = filledNan.drop_duplicates()
print(filledNan)

# Dop a whole column in place, so filledNan is updated
filledNan.drop('new', inplace=True, axis=1)
print(filledNan)

# Iterate over the dataframe
for idx, row in filledNan.iterrows():
    print(f"row.a {row.a}")

# Union two series
ser1 = pd.Series([1, 3, 5, 7, 9])
ser2 = pd.Series([1, 4, 5, 9, 12])

union = pd.Series(np.union1d(ser1, ser2))
print(union)

# Names in series one but not in series two
inOneButNotTwo = ser1[~ser1.isin(ser2)]
print(inOneButNotTwo)

# Convert the series to dataframe
print(inOneButNotTwo.to_frame())

# Add column using an array
filledNan['new2'] = [4, 3, 2, 5]
print(filledNan)

numpyConverted = filledNan.to_numpy(dtype=None, copy=False)
print(numpyConverted)

# Requires openpyxl, commenting out to not write a file every run
# filledNan.to_excel('test.xlsx')

s = pd.Series([1, 3, 23.2, 0, 9, 87, 3, 9.9], name='AAPL.OQ')
print(s.describe())

time_index = pd.date_range('21Jan20', periods=len(s), freq='D')
s.index = time_index

# If we want the third row, we should use iloc rather than s[2], as the index of s may itself be integers out of order
print(s.iloc[3])
print(s['22Jan20'])
print(s[~(s>np.mean(s))])
