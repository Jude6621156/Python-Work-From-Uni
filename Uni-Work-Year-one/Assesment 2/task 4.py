import random

list1 = [random.randint(1, 5) for i in range(5)]
print(list1)
def calculate_odd_even(list1):
    totalo = 0
    totale = 0
    for i in list1:
        if i%2 == 0:
            totale+=i
        else:
            totalo+=i
    return (totalo, totale)

print(calculate_odd_even(list1))
        
