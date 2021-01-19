import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm

# Start with data in DataFrame
# y = 2x + 3
points = 100
x = list(range(points))
y = [ 2*i + 3 for i in x ]

d = { 'x' : x, 'y' : y }
data = pd.DataFrame(data=d)

# Split out data for statsmodels
exog = sm.add_constant(data.x)
endog = data.y

model = sm.OLS(endog, exog)
fit = model.fit()

print(fit.summary())

data.plot(y='y')
plt.show()