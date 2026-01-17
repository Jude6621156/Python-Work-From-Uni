import random
list1 = [random.randint(1, 10) for i in range(10)]
print(list1)
def pweez(l):
    b = 1
    for c in range(len(l)):
        for d in l:
            if b == d:
                b+=1
    return b

print(pweez(list1))
                
            
        
