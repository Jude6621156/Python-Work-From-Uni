import random
from functools import reduce
list2 = [i for i in range(1, 11)]
list1 = list(filter(lambda x: x%3==0, list2))




list1 = [i for i in range(1, random.randint(2, 5))]
print(list1)

a = reduce((lambda x, y : x*y), list1)

print(a)
