import array
import numpy as np
import time
from scipy import special


print_create_lists = False
print_array_attributess = False
print_array_slicing = False
print_array_reshaping = False
print_array_concatenate = False
print_array_split = False
print_universal_functions = True


########################
# numpy create lists
########################

# classic array in python
L = list(range(10))
a_classic_array = array.array('i', L)
if print_create_lists:
    print(f'classic array: {a_classic_array}')

np.array([1,2,3,4,5])
# upcast
a_cast = np.array([3.2, 6, 54.3])
if print_create_lists:
    print(f'a_cast: {a_cast}')

# specific cast
a_specific_cast = np.array([3.2, 6, 54.3], dtype='int')
if print_create_lists:
    print(f'a_specific_cast: {a_specific_cast}')

# lists of lists
a_lists_of_list = np.array([range(i, i + 3) for i in [2, 4 ,6] ])
if print_create_lists:
    print(f'list of lists {a_lists_of_list}')

# inti array with 0
a_zeros = np.zeros(10, dtype=int)
if print_create_lists:
    print(f'init array zero: {a_zeros}') 

# init array with 1
a_ones = np.ones((3, 5), dtype=int)
if print_create_lists:
    print(f'init array one:{a_ones}')

# init array with float
a_float = np.full((3,5), 3.14)
if print_create_lists:
    print(f'init array 3.14 {a_float}')

# init array with a liniar sequence
a_sequence = np.arange(0, 20, 2)
if print_create_lists:
    print(f'init sequence:\n {a_sequence}')

# init array evenly distributed
a_liniar_distributed = np.linspace(0, 1, 20)
if print_create_lists:
    print(f'init sequence evenly:\n {a_liniar_distributed}')

# init array random values between 0 nad 1
a_random = np.random.random((2,2))
if print_create_lists:
    print(f'random array:\n {a_random}')

# init array with values in a certain range
a_random_int = np.random.randint(0, 10, (2,3))
if print_create_lists:
    print(f'random integers with range: \n {a_random_int}')

# init random array from standard distribution
a_random_normal_dist = np.random.normal(0, 1, (2,2))
if print_create_lists:
    print(f'random normal distribution: \n {a_random_normal_dist}')

# create identity matrix
a_identity_matrix = np.eye(2,3, dtype=int)
if print_create_lists:
    print(f'identity matrix:\n {a_identity_matrix}')

# create random array with whatever is in memory at that time
a_rand = np.empty(2)
if print_create_lists:
    print(f'array with memory values at that time {a_rand}')

#################################
# numpy attributes
#################################
np.random.seed(0)

x1 = np.random.randint(10, size=6)
x2 = np.random.randint(10, size=(3,4))
x3 = np.random.randint(10, size=(3,4,5))

if print_array_attributess:
    print(f'x3 ndim: {x3.ndim}')
    print(f'x3 shape: {x3.shape}')
    print(f'x3 size: {x3.size}')
    print(f'x3 data type: {x3.dtype}')
    print(f'x3 item size: {x3.itemsize} bytes')
    print(f'x3 sum of item sizes {x3.nbytes} bytes')
    print(f'first element 1d array {x1[0]}')
    print(f'last element 1d {x1[-1]}')
    print(f'first elemenet 2d array {x2[0, 0]}')



x = np.arange(10)
if print_array_slicing:
    print(f'initial 1d array: {x}')
    print(f'first 5 elements: {x[:5]} ')
    print(f'elements after index 5: {x[5:]}')
    print(f'middles subarray: {x[4:7]}')
    print(f'every other element: {x[::2]}')
    print(f'every other element, starting at index 1 {x[1::2]}')
    print(f'all elements reversed {x[::-1]}')
    print(f'reversed every other elements after index 5: {x[5::-2]}')
    
    print(f'initiel 2d array: \n {x2}')
    print(f'2 rows, 3 columns: \n {x2[:2,:3]}')
    print(f'all rows, every other column:??? \n {x2[:,::2]}')
    print(f'reverse strings together:\n {x2[::-1,::-1]}')

    print(f'access single column:\n {x2[:, 0]}')
    print(f'acces single row:\n {x2[0, :]}')

    print(f'copy array: \n {x2.copy()}')


#######################
# array reshape
#######################

x = np.array([1,2,3])
if print_array_reshaping:
    print(f'initial array {x}')
    print(f'row vector via newaxis {x[np.newaxis, :]}')
    print(f'column vector via reshape: \n {x.reshape(3, 1)}')
    print(f'column vector via new axis: \n {x[:, np.newaxis]}')

#########################
# array concatenante
#########################

x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
z = np.array([99, 99, 99])
grid = np.array([[9, 7, 8], [6, 5, 4]])
t = np.array([[99], [99]])

if print_array_concatenate:
    print(f'add 2 vectors {np.concatenate([x, y])}')
    print(f'add 3 vectors {np.concatenate([x, y, z])}')
    print(f'add matrixes along the first axis \n {np.concatenate([grid, grid])}')
    print(f'add matrixes along the second axis \n {np.concatenate([grid, grid], axis = 1)}')
    print(f'add matrixes different dimensions vertically \n {np.vstack([x, grid])}')
    print(f'add matrixes different dimensions horizontaly \n {np.hstack([grid, t])}')

########################
# array split
########################

x = np.array([1,2,3,99,99,3,2,1])
x1, x2, x3 = np.split(x, [3, 5])
grid = np.arange(16).reshape((4, 4))
upper, lower = np.vsplit(grid, [2])
left, right = np.hsplit(grid, [2])
if print_array_split:
    print(f' array before {x}')
    print(f' array split in 3 x1 = {x1}, x2 = {x2}, x3 = {x3}')
    print(f' before split \n {grid}')
    print(f'after vertical split \n {upper} \n and \n {lower}')
    print(f'after horizontally split \n {left} \n and \n {right}')

#########################
# universal functions
#########################


if print_universal_functions:
    def compute_reciprocals(values):
        output = np.empty(len(values))
        for i in range(len(values)):
            output[i] = 1.0 / values[i]
        return output
    
    values = np.random.randint(1, 100, size = 150000)
    start_of_f1 = time.time()
    compute_reciprocals(values)
    start_of_f2 = time.time()
    reciprocals = (1.0 / values)
    end = time.time()
    print(f'first function ran for {start_of_f2 - start_of_f1} and the second for {end - start_of_f2}')
    print(f' universal function work between vectors also: \n {np.arange(5) / np.arange(1,6)}')
    x = np.arange(9).reshape(3,3)
    print (f'power works ok \n {x ** 2 }')

    x = np.arange(5)
    print(f'original array: {x}')
    print(f'adding 5 to the the whole array {x + 5}')
    print(f'adding 5 without wrapper  {np.add(x,5)}')
    print(f'power 2 the whole array {x ** 2}')
    
    x = np.array([4 - 4j, 3 + 1j])
    print(f'absolute of array of complex numbers {np.abs(x)}')

    theta = np.linspace(0, np.pi, 3)
    print(f'trigonometric functions theta = {theta}')
    print(f'sin(theta) = {np.sin(theta)}')
    print(f'cos(theta) = {np.cos(theta)}')
    print(f'tan(theta) = {np.tan(theta)}')

    x = [-1, 0, 1]
    print(f'invers trigonometric functions x = {x}')
    print(f'arcsin(x) = {np.arcsin(x)}')
    print(f'arccos(x) = {np.arccos(x)}')
    print(f'arctan(x) = {np.arctan(x)}')

    x = [1, 2, 3]
    print(f'exponets functions x = {x}')
    print(f'e^x = {np.exp(x)}')
    print(f'2^x = {np.exp2(x)}')
    print(f'3^x = {np.power(3, x)}')

    x = [1, 2, 4, 10]
    print(f'logaritmic functions {x}')
    print(f'ln(x) = {np.log(x)}')
    print(f'log2(x) = {np.log2(x)}')
    print(f'log10(x) = {np.log10(x)}')

    x = [0, 0.001, 0.01, 0.1]
    print(f'exp and log for small values x = {x}') 
    print(f'exp(x) - 1 = {np.expm1(x)}')
    print(f'log(1 + x) = {np.log1p(x)}')

    x = [1, 5, 10]
    print(f'array for gamma functions x = {x}')
    print(f'gamma(x) = {special.gamma(x)}')
    print(f'ln|gamma(x) = {special.gammaln(x)}')
    print(f'beta(x, 2) = {special.beta(x, 2)}')

    x = np.array([0, 0.3, 0.7, 1.0])
    print(f'error function (integral of gauss) for x = {x} ')
    print(f'erf(x) = {special.erf(x)}')
    print(f'erfc(x) = {special.erfc(x)}')
    print(f'erfinv(x) = {special.erfinv(x)}')


    
