# Python program explaining
# numpy.count() function

import numpy as np

a = np.array(['python', 'with', 'pranshu'])

# counting a substring
print(np.char.count(a, 'pranshu'))

# counting a substring
print(np.char.count(a, 'with'))