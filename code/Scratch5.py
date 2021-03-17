import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.DataFrame({'a': [1, 3, 5, 9, 12], 'b': [2, 7, 12, 90, 21], 'c': [ 'red', 'red', 'white', 'white', 'white']})

grouped = data.groupby(['c']).agg({'a': [np.sum, np.max], 'b': np.sum})
print(grouped)

y = np.array([1, 12, 28, 19])
x = np.array([[2,3], [3,4], [4,5], [5,6]])

x_const = sm.add_constant(x)

print(f"Y: {y}\nX:{x_const}")

model = sm.OLS(y, x_const)
output = model.fit()
print(output.summary())

X_train, X_test, y_train, Y_test = train_test_split(x, y)

model2 = LinearRegression()
model2.fit(x, y)