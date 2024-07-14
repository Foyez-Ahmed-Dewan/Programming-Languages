import numpy as np


data = np.array([1, 2, 3, 4, 5])
# indexing : 0 based
print(data[1]) # output: 2
print(data[-1]) # output: 5

#slicing operations
a = np.arange(10)
print(f"a        = {a}")

#access 5 consecutive elements (start:stop:step)
c = a[2:7:1];     print("a[2:7:1] = ", c)

# access 3 elements separated by two
c = a[2:7:2];     print("a[2:7:2] = ", c)

# access all elements index 3 and above
c = a[3:];        print("a[3:]    = ", c)

# access all elements below index 3
c = a[:3];        print("a[:3]    = ", c)

# access all elements
c = a[:];         print("a[:]     = ", c)

"""
a        = [0 1 2 3 4 5 6 7 8 9]
a[2:7:1] =  [2 3 4 5 6]
a[2:7:2] =  [2 4 6]
a[3:]    =  [3 4 5 6 7 8 9]
a[:3]    =  [0 1 2]
a[:]     =  [0 1 2 3 4 5 6 7 8 9]
"""

#2d array
a = np.array([[1 , 2, 3, 4, 10], [5, 6, 7, 8, 2], [9, 10, 11, 12, 1]])

print(a.ndim)   # output: 2
print(a.size)   # output: 5 * 3 = 15
print(a.shape)  # output: (3, 5)

# If you want to select values from your array that fulfill certain conditions, it’s straightforward with NumPy.
# print all the elements that is less than 5
print(a[a < 5]) # output: [1 2 3 4 2 1]
# all elements that is not equal to 1
print(a[a != 1]) # output: [ 2  3  4 10  5  6  7  8  2  9 10 11 12]
# all elements that are divisible by 2
print(a[a % 2 == 0]) # output:[ 2  4 10  6  8  2 10 12]
# all elements that is greater than 2 and less than 8
print(a[(a > 2) & (a < 6)]) # output: [3 4 5]



# create a new array from an existing array, we can use slicing method
a = np.array([1,  2,  3,  4,  5,  6,  7,  8,  9, 10])

new_a = a[0 : len(a)]
print(new_a)    # output: [ 1  2  3  4  5  6  7  8  9 10]

new_a = a[4 : 9]
print(new_a) # output: [5 6 7 8 9]

# we can stack two existing array, both vertically and horizontally
a1 = np.array([[1, 1], [2, 2]])
a2 = np.array([[3, 3], [4, 4]])

# stack two array vertically
new_a = np.vstack((a1, a2))
print(new_a)

# output:
# [[1 1]
#  [2 2]
#  [3 3]
#  [4 4]]

# stack two array horizontally
new_a = np.hstack((a1, a2))
print(new_a)

#output:
# [[1 1 3 3]
#  [2 2 4 4]]

# to splits an array into several smaller arrays
new_aa = np.hsplit(new_a, 4)
print(new_aa)

"""
[array([[1],[2]]), 
array([[1],[2]]), 
array([[3],[4]]), 
array([[3],[4]])]
"""


