import random
list1 = [random.randint(1, 10) for i in range(10)]
list2 = [random.randint(1, 10) for i in range(10)]
print(list1)
print(list2)
def zap(list1, list2):
    #list3 = []
    list4 = [(list1[i], list2[a]) for i in range(len(list1)) for a in range(len(list2)) if i == a]
    #list3.append(list4)
    #for i in range(len(list1)):
    #    for a in range(len(list2)):
     #       if i == a:
      #          list4 = [list1[i], list2[a]]
       #         list3.append(list4)

    return list4

print(zap(list1, list2))
