import numpy as np

a = np.array(
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [3, 4, 5, 0]
    ]
)

# mean of each column
mu = np.mean(a, axis = 0)
print(mu)

print(a - mu)

# standard deviation of each column
sigma = np.std(a, axis = 0)
print(sigma)

# mean of each row
mu = np.mean(a, axis = 1)
print(mu)

##
x = np.arange(0, 5, 1)

X = np.c_[x, x**2, x**3]
print(X)

















