import numpy as np

a = np.array([1,2,3,4])
print(f"a             : {a}")
# negate elements of a
b = -a
print(f"b = -a        : {b}") # output: [-1 -2 -3 -4]

# sum all elements of a, returns a scalar
b = np.sum(a)
print(f"b = np.sum(a) : {b}")

b = np.mean(a)
print(f"b = np.mean(a): {b}")

b = a**2
print(f"b = a**2      : {b}")

# binary operator : + , -
b = np.array([-1,-2, 3, 4])
print(f"Binary operators work element wise: {a + b}")
# this to work correctly, the vectors must be of the same size

# multiply a by a scalar
b = 5 * a
print(f"b = 5 * a : {b}")

# size of the array
print(a.shape[0]) # 4

# dot product
a = np.array([1, 2, 3, 4])
b = np.array([-1, 4, 3, 2])
c = np.dot(a, b)

print(f"Dot product of {a} and {b} is: {c}")

# to delete an array
del (a)

# X = m * n dimension = 3 * 2
# W = 1 * n dimension = 1 * 2
X = np.array ([
    [1, 2],
    [3, 4],
    [5, 6]
])

W = np.array([2, 4])

for i in range (3):
    print(W * X[i])

########## matrices
# shape(x, y) is used to create a matrix of order : x * y
a = np.zeros((1, 5))    # no of row = 1, element = 5
print(f"a shape = {a.shape}, a = {a}")
print(a.ndim)

a = np.zeros((2, 1))    # no of row = 2, no of ele. in each row = 1
print(f"a shape = {a.shape}, a = {a}")
print(a.ndim)

a = np.random.random_sample((1, 1)) # no of row = 1, no of ele. in each row = 1
print(f"a shape = {a.shape}, a = {a}")

a = np.random.random_sample((3, 4)) # no of row = 3, element in each row = 4
print(a)

# to access an element
print(a[2][1])
print(a[2, 1])  # (2, 1)th element

#to access a row
print(a[1]) # 2nd row

# to reshape an array into matrices
a = np.arange(6).reshape(-1, 2)
print(a)

"""
here, np.arange(6) generates a 1 dimensional array with 6 elements
then, reshape(-1, 2): reshapes the array into 2 dimensional array with 2 columns.
    '-1' indicates number of rows should be calculated based on size of the original array and the no of columns specified 
"""

#vector 2-D slicing operations
a = np.arange(20).reshape(-1, 10)
print(f"a = \n{a}")

#access 5 consecutive elements (row_number, start:stop:step)
print("a[0, 2:7:1] = ", a[0, 2:7:1], ",  a[0, 2:7:1].shape =", a[0, 2:7:1].shape, "a 1-D array")

#access 5 consecutive elements (start:stop:step) from all the rows
print("a[:, 2:7:1] = \n", a[:, 2:7:1], ",  a[:, 2:7:1].shape =", a[:, 2:7:1].shape, "a 2-D array")

# access all elements
print("a[:,:] = \n", a[:,:], ",  a[:,:].shape =", a[:,:].shape)

# access all elements in one row (very common usage)
# array_name [row_number, : ]
# array_name [row_number]
print("a[1,:] = ", a[1,:], ",  a[1,:].shape =", a[1,:].shape, "a 1-D array")
# same as
print("a[1]   = ", a[1],   ",  a[1].shape   =", a[1].shape, "a 1-D array")

###
a = np.array([1, 2, 3])
print(a.shape[0]) # 3

a = np.array(
    [
        [1, 2, 3, 4],
        [4, 5, 6, 7],
        [8, 9, 10, 11]
    ]
)

print(a.shape[0])  # 3
print(a[0].shape[0]) # 4

r, c = a.shape

print (f"row = {r} : col = {c}")

a = np.zeros((4, ))
print(a)
