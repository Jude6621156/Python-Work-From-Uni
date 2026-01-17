list1 = ['bcdee', 'bcde', 'bcdef', ' ']
list2 = [0]
total1 = 0
for i in list1[0]:
    total1 += ord(i)
    list2.append(total1)

print(list2)
list3 = []

for a, b in enumerate(list1):
    total = 0
    if a == 0:
        pass
    
    else:
        try:
            for c, d in enumerate(b):                 
                if list2[c] == total:
                    total += ord(d)
                    if len(b) == c+1:
                        if list2[c+1] == total:
                            list3.append(total)
                            break                        
                        else:
                            total -= ord(d)
                            list3.append(total)
                            break
                else:
                    total -= ord(b[c-1])
                    list3.append(total)
                    break
                    
        except IndexError:
                    total -= ord(b[c-1])
                    list3.append(total)
                    break
            
small = total1 + 1
v = 0
try:
    for j in list3:
        if j < small:
            small = j
            v = j
    r = ''
    t = list1[0]
    x = 0
    while list2[x] < v:
        r += t[x]
        x+=1
    print(r)

    print(list3)
except IndexError:
    print('no common prefix')

    
            
