import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

s = pd.Series([1,3,2,4])
x = pd.DataFrame({'a': [1,2,3,4], 'b':[6,7,8,9], 's':s, 'cat': ['A', 'A', 'B', 'A']})
print(x)

k = x[1:]
print(k)

# Note here, k.loc[0] doesn't work because the index of k starts from 1, whereas iloc does work
print(k.iloc[0])

print(pd.get_dummies(x))

y = np.array([[1,3,4],[3,5,6],[1,8,2]])
print(y)

# Get first two elems of left most col
print(y[:2,2:])

sym = np.array([[1,2,3],[2,9,90],[3,90,12]])
print(sym)
print(np.linalg.eig(sym))
print(sym.transpose() == sym)

sample = np.random.normal(5, 12, 12000)
print(stats.normaltest(sample))