import random

print(['dp' + str(i) for i in range(1,11)])
print(random.randint(0,2))

category = ['cat1', 'cat2', 'cat3']


print([['cat1', 'cat2', 'cat3'][random.randint(0,2)] for _ in range(0,10)])