import random
list1 = [random.randint(-5, 5) for i in range(4)]
print(list1)
def l(list1):
    list3 = []
    list2 = []
    total = 0
    for a in list1:
        total+=a
    print(total)
    counter = len(list1) - 1
    while counter > -1:
        list2 = []
        total1 = 0
        for b in range(counter):
            list2.append(list1[b])
        for c in list2:
            total1 += c
        if total1 == total:
            return list2
        else:
            counter-=1
    counter = 1
    
    while counter < len(list1):
        list2 = []
        total1 = 0
        for d in range(counter, len(list1)-1):
            list2.append(list1[d])
        for e in list2:
            total1 += e
        if total1 == total:
            return list2
        else:
            counter += 1
    return list3

print(l(list1))

