import random

print(['dp' + str(i) for i in range(1,11)])
print(random.randint(0,2))

category = ['cat1', 'cat2', 'cat3']


print([['cat1', 'cat2', 'cat3'][random.randint(0,2)] for _ in range(0,10)])

aggs = [("height", "min"), ("height", "max"), ("weight", "mean")]

print([{"_".join(agg): agg for agg in aggs}])



def rank_simple(vector):
    return sorted(range(len(vector)), key=vector.__getitem__)

print(rank_simple([9,1,3,2]))

