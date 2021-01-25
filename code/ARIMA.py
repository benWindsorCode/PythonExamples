from pathlib import Path
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import statsmodels.api as sm
import requests
import pandas as pd
from io import BytesIO
import matplotlib.pyplot as plt
import seaborn as sns

data_path = 'data/wpi.csv'
if not Path(data_path).is_file():
    wpi1 = requests.get('https://www.stata-press.com/data/r12/wpi1.dta').content
    data = pd.read_stata(BytesIO(wpi1))
    data.index = data.t
    # Set the frequency
    data.index.freq = "QS-OCT"
    data.to_csv('data/wpi.csv')
else:
    print("Loading cached data")
    data = pd.read_csv('./data/wpi.csv')
    data.index = data.t
    data.index.freq = 'QS-OCT'

print(data.shape)
print(data.describe())

data.plot()
plot_acf(data['wpi'])
plot_pacf(data['wpi'])
plt.show()