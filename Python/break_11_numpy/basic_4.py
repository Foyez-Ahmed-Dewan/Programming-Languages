import numpy as np

# 1D array
one_dim_arr = np.array([1, 2, 3, 4, 5, 6])

# Multidimensional array using reshape()
multi_dim_arr = np.reshape(
                    one_dim_arr, # the array to be reshaped
                    (2,3) # dimensions of the new array
                )
# Print the new 2-D array with two rows and three columns
print(multi_dim_arr)
"""
[[1 2 3]
 [4 5 6]]
"""
print(multi_dim_arr[1][2]) # output: 6
print(multi_dim_arr[1, 2]) # output: 6