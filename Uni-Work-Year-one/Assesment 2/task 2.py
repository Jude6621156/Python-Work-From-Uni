import random
list1 = [random.randint(-3, 3) for i in range(7)]
print(list1)
def l(list1):
    list2 = []
    for i in list1:
        flag = True
        for a in list2:
            if i == a:
                flag = False
        if flag == True:
            list2.append(i)
    print(list2)
    list4 = []
    for j in list2:
        for y in list2:
            for x in list2:
                if x != y:
                    if x!=j:
                        if j!= y:
                            list3 = []
                            if x+j+y == 0:
                                list3.append(x)
                                list3.append(j)
                                list3.append(y)
                                list4.append(list3)
    for a, b in enumerate(list4):
        total = 0
        counter = 0
        while counter < len(list4):
            total = 0
            if counter == a:
                pass
            else:
                for e in range(3):
                    for c in range(3):
                        if list4[counter][c]== b[e]:
                            total+=1
                if total == 3:
                    del list4[counter]
            counter += 1
    
    for a, b in enumerate(list4):
        total = 0
        counter = 0
        while counter < len(list4):
            total = 0
            if counter == a:
                pass
            else:
                for e in range(3):
                    for c in range(3):
                        if list4[counter][c]== b[e]:
                            total+=1
                if total == 3:
                    del list4[counter]
            counter += 1
    return list4

            
print(l(list1))

