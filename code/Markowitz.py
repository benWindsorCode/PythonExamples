import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Source: https://faculty.washington.edu/ezivot/econ424/portfolioTheoryMatrix.pdf

means = np.array([0.0427, 0.0015, 0.0285])
vars = np.array([0.1, 0.1044, 0.1411])

data = pd.DataFrame({'asset': ['MSFT', 'NORD', 'SBUX'], 'mean': means, 'var': vars, 'label': ['input', 'input', 'input']})

cov = np.array([
    [0.0100, 0.0018, 0.0011],
    [0.0018, 0.0109, 0.0026],
    [0.0011, 0.0026, 0.0199]
])


# Find min variance portfolio: w = (sigma^-1 1)/(1^T sigma^-1 1)
oneCol = np.reshape(np.ones(3), (3, 1))

numerator = np.dot(np.linalg.inv(cov), oneCol)
denominator = np.dot(np.transpose(oneCol), np.dot(np.linalg.inv(cov), oneCol))
minVarWeights = numerator/denominator

def portfolio_var(weights, cov):
    return np.dot(np.transpose(weights), np.dot(cov, weights))[0][0]

def portfolio_mean(weights, means):
    return np.dot(np.transpose(weights), np.reshape(means, (3, 1)))[0][0]

minVar = portfolio_var(minVarWeights, cov)
minMean = portfolio_mean(minVarWeights, means)

data = data.append({'asset': 'MIN-VAR', 'mean': minMean, 'var': minVar, 'label': 'min'}, ignore_index=True)

# Find min variance portfolio with specified mean, solving Az = b
def b_vec(meanVec, covMat):
    zeroLen = covMat.shape[0]
    concat = np.concatenate((np.zeros(zeroLen), [meanVec], [1]))
    return np.reshape(concat, (zeroLen+2, 1))

def A_mat(means, covMat):
    twoCov = 2*covMat
    size = covMat.shape[0]
    horizStacked = np.hstack((twoCov, np.reshape(means, (size,1)), np.reshape(np.ones(size), (size, 1))))
    meanRow = np.hstack((means, [0, 0]))
    oneRow = np.hstack((np.ones(size), [0, 0]))
    total = np.vstack((horizStacked, meanRow, oneRow))

    return total

def min_var_with_mean(mean, means, covMat):
    b = b_vec(mean, covMat)
    A = A_mat(means, covMat)

    return np.dot(np.linalg.inv(A), b)[0:covMat.shape[0]]

# Create min var portfolio with return matching MSFT
msftMean = 0.0427
msftWeights = min_var_with_mean(msftMean, means, cov)

msftMinVar = portfolio_var(msftWeights, cov)
msftMean = portfolio_mean(msftWeights, means)
data = data.append({'asset': 'MIN-VAR-MSFT', 'mean': msftMean, 'var': msftMinVar, 'label': 'min'}, ignore_index=True)

# Create min var portfolio with return matching SBUX
sbuxMean = 0.0285
sbuxWeights = min_var_with_mean(sbuxMean, means, cov)

sbuxMinVar = portfolio_var(sbuxWeights, cov)
sbuxMean = portfolio_mean(sbuxWeights, means)
data = data.append({'asset': 'MIN-VAR-SBUX', 'mean': sbuxMean, 'var': sbuxMinVar, 'label': 'min'}, ignore_index=True)

# Using linear combination of two frontier portfolios, msft and min var, we compute the efficient fronter with linear combinations of those
alphaSpace = np.linspace(-1, 1, 50)
for alpha in alphaSpace:
    frontierWeights = alpha*minVarWeights + (1-alpha)*msftWeights
    frontierVar = portfolio_var(frontierWeights, cov)
    frontierMean = portfolio_mean(frontierWeights, means)
    name = f"FRONTIER-{alpha:.3f}"
    data = data.append({'asset': name, 'mean': frontierMean, 'var': frontierVar, 'label': 'frontier' }, ignore_index=True)

# Show data
data.set_index('asset', inplace=True)

sns.scatterplot(data=data, x='var', y='mean', hue='label')
plt.show()
