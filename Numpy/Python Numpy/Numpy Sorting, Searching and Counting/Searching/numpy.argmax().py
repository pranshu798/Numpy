# Python Program illustrating
# working of argmax()

import numpy as np

# Working on 2D array
array = np.arange(12).reshape(3, 4)
print("INPUT ARRAY : \n", array)

# No axis mentioned, so works on entire array
print("\nMax element : ", geek.argmax(array))

# returning Indices of the max element
# as per the indices
print(("\nIndices of Max element : "
       , np.argmax(array, axis=0)))
print(("\nIndices of Max element : "
       , np.argmax(array, axis=1)))