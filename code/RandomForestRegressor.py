from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split, RepeatedKFold, GridSearchCV
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', 20)

(data, target) = load_diabetes(return_X_y=True, as_frame=True)

total = pd.concat([data, target], axis=1)

#sns.pairplot(data=total)
#plt.show()

print(f"Cols: {total.columns}, Types: {total.dtypes}")
print(total.head(5))

X_train, X_test, Y_train, Y_test = train_test_split(data, target)
grid = {'randomforestregressor__n_estimators': [100, 200, 300, 400, 500, 600, 700], 'pca__n_components': [3, 4, 5]}

model = make_pipeline(PCA(), RandomForestRegressor())
print(f"params: {model.get_params().keys()}")
cross_val = RepeatedKFold(n_splits=4, n_repeats=2, random_state=1)
search = GridSearchCV(model, grid, scoring='neg_mean_absolute_error', cv=cross_val)
search.fit(X_train, Y_train)
print(search.best_params_)

# Output of the grid search was pca 5 components, random forest 600 estimators
model = make_pipeline(PCA(n_components=5), RandomForestRegressor(n_estimators=600))
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)
print(f"R2: {r2_score(Y_test, Y_pred)}, MSE: {mean_squared_error(Y_test, Y_pred)}")