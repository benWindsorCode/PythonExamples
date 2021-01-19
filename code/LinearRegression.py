import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm

# y = 2x + 3
points = 30
x = list(range(points))
y = [ 2*i + 3 for i in x ]

d = { 'x' : x, 'y' : y }
data = pd.DataFrame(data=d)

data.plot()
plt.show()
