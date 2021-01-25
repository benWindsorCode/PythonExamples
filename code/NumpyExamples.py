import numpy as np

#Source: Numpy interview questions http://www.ezdev.org/view/numpy/6486

# Matrix product
identity = np.eye(2)  # 2x2 identity matrix
testMat = np.array([[2, 3], [4, 5]])

prod = np.dot(identity, testMat)
print(prod)

# Transpose
print(prod.T)

# Percentiles of data
sample = np.random.normal(5, 12, 500)
print(np.percentile(sample, 99))

# Extract sub array
threeByThree = np.reshape(np.random.normal(0, 1, 9), (3, 3))
print(threeByThree)
print(threeByThree[0:2,0:2])

# Array to list
normalList = threeByThree.tolist()
print(normalList)
flat = [x for y in normalList for x in y] # alternately use normalList.ravel() or normalList.flatten()
print(flat)

# Norm of two vectors ||a-b||
a = np.array([1, 2, 3])
b = np.array([2, 3, 4])
print(np.linalg.norm(a-b))

# Create array of zeroes
x = np.zeros((4, 3))
print(x)

y = np.ones((2,2,2))
print(y)

# Linspace
space = np.linspace(0,1,20)
print(space)

# Stack arrays vertically or horizontally
vertStack = np.vstack((a, b))
print(vertStack)
horizStack = np.hstack((a, b))
print(horizStack)

# Max element and max argument
newList = np.random.poisson(5, 50)
print(f"max: {np.amax(newList)}, index: {np.argmax(newList)}, proof: {newList[np.argmax(newList)]}")