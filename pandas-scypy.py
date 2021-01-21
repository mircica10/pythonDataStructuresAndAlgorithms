from scipy.stats import hypergeom

"""
Example 1. Estimating the b parameter in the hypergeometric distribution. 
There is a batch of workpieces n=1000 pcs. After checking k=20 of them, a defective workpiece 
has been detected: x=1. Estimate the number of defective workpieces in the entire batch.
"""

n = 1000
k = 20
x = 1
lhx = 0.0
be = 0

for b in range(x, n - k + x):
    lh = hypergeom.pmf(x, n, b, k)
    if lh > lhx:
        be = b
        lhx = lh
print(f'be = {be}')

"""
Example 2. Estimating the n parameter in the hypergeometric distribution. 
It is required to estimate the amount of fish in the water body. 
To do this, b=50 fishes were caught with a net, marked and released back.
 After that, k=55 fishes were caught, of which x=3 turned out to be marked.
"""

b = 50
k = 55
x = 3
lh0 = 0.0
ne = b + k - x - 1
# function will increase to a max value, then decrease, hence the apparently endless loop
while True:
    lh = hypergeom.pmf(x, ne + 1, b, k)
    if lh < lh0:
        break
    else:
        lh0 = lh
        ne += 1

print(f'ne = {ne}')