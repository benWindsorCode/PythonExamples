import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
from sklearn.linear_model import LinearRegression, HuberRegressor
from sklearn.model_selection import train_test_split

x = np.arange(300)
noise = np.random.normal(0.2, 12, 300)

# Create line with some outliers thrown in as well as noise
y = [3*i + noise[i] + random.choice([0, 0, 0, 0, 400, -250, 0, 0, 150, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1000]) for i in x]

# X values should be of the form of an array of arrays
x_points = [[i] for i in x]

linear_model = LinearRegression()
linear_model.fit(x_points, y)
pred = linear_model.predict(x_points)

huber_model = HuberRegressor()
huber_model.fit(x_points, y)
pred_huber = huber_model.predict(x_points)

data = pd.DataFrame(data={'x': x, 'y': y, 'pred': pred, 'pred_huber': pred_huber})

# NOTE: BUG where if you do plot() above the linear model fit then it breaks!
data[['y', 'pred', 'pred_huber']].plot()
plt.show()
