import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

# Y = 3a + 2b + 9
points = 300
a = list(range(points))
b = [7.3*i for i in list(range(points))]
rand = np.random.normal(1, 12, points)
Y = [3*a[i] + 2*b[i] + rand[i] for i in list(range(points))]

X = {'a': a, 'b': b}
X = pd.DataFrame(X)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y)

model = LinearRegression()
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

print(f"R2: {r2_score(Y_test, Y_pred)}, MSE: {mean_squared_error(Y_test, Y_pred)}")
print(f"Intercept: {model.intercept_}, Coeffs: {model.coef_}")

preds = pd.DataFrame({'Y_true': Y_test, 'Y_pred': Y_pred})
preds.plot(y=['Y_true', 'Y_pred'])

plt.show()


