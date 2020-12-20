a = [[1,2,4],[3,4,5]]

assert( len(a) == 2 )
assert( len(a[0]) == 3 )


# zip
a = [1,2]
b = [3,4]
c = zip(a,b)

for i in c:
    assert(i == (1,3))
    break

# list chained for
t = [i for i in b if any( (i + x) == 6 for x in b)]
assert(t == [3])

#count bool values
s = sum([True, True,False])
assert(s == 2)