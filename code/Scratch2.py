from sklearn.datasets import load_boston
import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 15)

X, y = load_boston(return_X_y=True)
feature_names = load_boston().feature_names
print(load_boston().DESCR)
print(feature_names)
print(X[0])
print(y[0])


all_data = pd.DataFrame(X, columns=feature_names)
all_data['target'] = y
print(all_data.head())
print(all_data.describe() )
#sns.relplot(data=all_data.iloc[:, 0:5], hue='target')
#plt.show()

print(all_data.corr())

X_const = sm.add_constant(X)
print(X_const[0])
model = sm.OLS(y, X_const)
fitted = model.fit()
print(fitted.summary())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
sklearn_model = LinearRegression()
sklearn_model.fit(X_train, y_train)
y_pred = sklearn_model.predict(X_test)
print(r2_score(y_test, y_pred))

