import random
list1 = []
for i in range(5):
    list1.append(random.randint(1, 5))
print(list1)

list2 = []
counter = 0
   
for a, b in enumerate(list1):
    x = 1
    counter = 0
    while counter < len(list1):
        if counter != a:
            x = x*list1[counter]
        counter+=1
    list2.append(x)

print(list2)
