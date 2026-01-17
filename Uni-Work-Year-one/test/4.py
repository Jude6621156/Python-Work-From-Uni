words = ["chocolate", "chicken", "soup", "potatoes", "beef", "lox", "beef"]
fifth_letter = []
for w in words:
    try:
        fifth_letter.append(w[4])
    except IndexError:
        pass
print(fifth_letter)

def get_value(values, index):
    try:
        return values[index]
    except IndexError:
        return None
my_list = ['a', 'b', 'c']
print(get_value(my_list, 1))
print(get_value(my_list, 4))

import numpy as np
from numpy import unravel_index
array1 = np.random.randint(0, 10, (10, 5))
print(array1)
def hmean():
    x = np.mean(array1, axis = 0)
    y = max(x)
    print(np.where(x == y)[0])
    print(x)
#hmean()


print('PWEEZ')

p = np.loadtxt('input.csv', delimiter=",")
m = unravel_index(p.argmax(), p.shape)
print(m)
print(p)
print(p[17, 42])
 
