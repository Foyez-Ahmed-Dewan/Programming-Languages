# to access NumPy and its functions we need to import it first

import numpy as np

    # rank = no of dimensions of an array
    # shape = size of each dimensions
    # dimensions are called axes

# to create a numpy array, we can use : np.array()
a = np.array([1, 2, 3])
print(a) # output: [1 2 3]

# to create an array with n number of zeros
a = np.zeros(4)
print(a) # output: [0. 0. 0. 0.]

# to create an array with n number of ones
a = np.ones(4)
print(a) # output: [1. 1. 1. 1.]

#to create an empty array with n elements: np.empty(n)
a = np.empty(4)
print(a) # the function empty creates an array whose initial content is random and depends on the state of the memory

# to create an array with a range of elements : np.arange(n) will gives [0 to n - 1]
a = np.arange(10)
print(a) #output: [0 1 2 ... 9]

a = np.arange(2, 10)
print(a) # output: [2 3 4 ... 9]

a = np.arange(2, 10, 2)
print(a) # output: [2 4 6 8]

# np.arange(start_pos, end_pos, step_size)
# by default, start_pos is 0 if not specified

# to create an array with values that are spaced linearly in a specified interval
a = np.linspace(2, 10, 6)
print(a)
    # output: [ 2.   3.6  5.2  6.8  8.4 10. ]
    # difference between each consecutive pair is equal

    # by default, data type is float
# we can explicitly specify which data type to use using `dtype` keyword
a = np.ones(2, dtype = np.int64)
print(a) # output: [1 1]

# to sort a numpy array, we can use: .sort()
a = np.array([4, 1, 5, 3, 2])
print(np.sort(a))   # [1 2 3 4 5]
print(a)            # [4 1 5 3 2]

a = np.sort(a)
print(a)            # [1 2 3 4 5]

# concatenate two numpy array: concatenate((x, y))
a = np.array([1, 2, 3])
b = np.array([2, 4, 5])
print(np.concatenate((a, b)))  #output: [1 2 3 2 4 5]

c = np.array([6, 7, 9])
print(np.concatenate((a, b, c))) #output: [1 2 3 2 4 5 6 7 9]

#
a = np.array([1, 2, 3])

print(a.ndim)   # dimension of an array = 1
print(a.size)   # size = no of elements of the array = 3
print(a.shape)  # size of each dimensions, returns a tuple = (3, )
print(a.shape[0]) # 3



