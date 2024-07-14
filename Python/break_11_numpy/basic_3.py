import numpy as np

first_a = np.array([1, 2, 3])
second_a = np.ones(3, dtype = int)

print(first_a)  # output: [1 2 3]
print(second_a) # output: [1 1 1]

# basic operations
print(first_a + second_a) # output: [2 3 4]
print(first_a - second_a) # output: [0 1 2]
print(second_a - first_a) # output: [0 -1 -2]
print(first_a * second_a * first_a) # output: [1 4 9]
print (second_a / first_a) # output: [1 0.5 0.333]

# broadcasting: multiplying an array with a scalar
# the scalar will be multiplied to whole array
print(5 * first_a) # output: [5 10 15]

new_a = 5 * (np.vstack((first_a, second_a)))

print(new_a)
# output:
# [[ 5 10 15]
#  [ 5  5  5]]


# to find maximum and minimum element of an arry
print(first_a.max()) # 3
print(first_a.min()) # 1
# sum of all the elements
print(first_a.sum()) # 1 + 2 + 3 = 6
print(new_a.sum())  # 45

# product of all the elements
print(first_a.prod()) # 1 * 2 * 3 = 6

# average of all the elements
print(first_a.mean()) # (1 + 2 + 3) / 3 = 2.0
print (new_a.mean()) # 7.5

# for 2d array, we can also specify for which column we want to apply aggregate functions
new_a = np.array([
    [1, 4, -2],
    [0, -1, 3],
    [3, 5, 5]
])

# to find minimum value within each column
print(new_a.min(axis = 0)) # output: [0 -1 -2]
# to find minimum value within each row
print(new_a.min(axis = 1)) # output: [-2 -1 3]