import array
import numpy as np

print_all = True

# classic array in python
L = list(range(10))
a_classic_array = array.array('i', L)
if print_all:
    print(f'classic array: {a_classic_array}')

np.array([1,2,3,4,5])
# upcast
a_cast = np.array([3.2, 6, 54.3])
if print_all:
    print(f'a_cast: {a_cast}')

# specific cast
a_specific_cast = np.array([3.2, 6, 54.3], dtype='int')
if print_all:
    print(f'a_specific_cast: {a_specific_cast}')

# lists of lists
a_lists_of_list = np.array([range(i, i + 3) for i in [2, 4 ,6] ])
if print_all:
    print(f'list of lists {a_lists_of_list}')