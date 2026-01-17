import random
list1 = []
for i in range(10):
    list1.append(random.randint(1, 100))

print(list1)
x = int(input('Pweez '))
def l(l, a):
    for b in range(len(list1)-1):
       counter = b+1
       while counter < len(l):
           if l[b] + l[counter] == a:
               return True
           else:
               counter+=1
    return False

print(l(list1, x))



