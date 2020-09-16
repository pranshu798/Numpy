# Python program explaining
# numpy.rfind() function

import numpy as np

a = np.array(['python', 'with', 'pranshu'])

# counting a substring
print(np.char.rfind(a, 'pranshu'))

# counting a substring
print(np.char.rfind(a, 'with'))