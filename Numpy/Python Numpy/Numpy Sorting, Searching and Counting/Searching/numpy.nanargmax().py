# Python Program illustrating
# working of nanargmax()

import numpy as np

# Working on 1D array
array = [np.nan, 4, 2, 3, 1]
print("INPUT ARRAY 1 : \n", array)

array2 = np.array([[geek.nan, 4], [1, 3]])

# returning Indices of the max element
# as per the indices ingnoring NaN
print(("\nIndices of max in array1 : "
       , np.nanargmax(array)))

# Working on 2D array
print("\nINPUT ARRAY 2 : \n", array2)
print(("\nIndices of max in array2 : "
       , np.nanargmax(array2)))

print(("\nIndices at axis 1 of array2 : "
       , np.nanargmax(array2, axis=1)))
