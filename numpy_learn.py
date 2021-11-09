"""
import array

L = list(range(10))
A = array.array('i', L)
print(A)
"""

import numpy as np
np.array([1,2,3,4,5])
# upcast
a = np.array([3.2, 6, 54.3])
#print(a)
# specific cast
a = np.array([3.2, 6, 54.3], dtype='int')
#print(a)
a = 
