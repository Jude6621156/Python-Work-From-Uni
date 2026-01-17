list1 = ['bcdee', 'bcde', 'bcdef', 'bcdes']
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
            print('PWEEEZEZ')
            for c, d in enumerate(b):
                print('b', b, 'd', d, 'l', list2[c], 't', total)
                 
                if list2[c] == total:
                    total += ord(d)
                    print('pweez')
                    if len(b) == c+1:
                        print('Pweeeeez')
                        if list2[c+1] == total:
                            list3.append(total)
                            print('sewious')
                            break
                        
                        else:
                            total -= ord(d)
                            list3.append(total)
                            print('sewious2')
                            break
                else:
                    total -= ord(b[c-1])
                    list3.append(total)
                    print('pweez is sewious', total)
                    break
                    
        except IndexError:
                    total -= ord(b[c-1])
                    list3.append(total)
                    print('sewious24')
                    break
            
small = total1 + 1
v = 0
try:
    for j in list3:
        print('pweez :D', j, small)
        if j < small:
            small = j
            v = j
            print('PWEEZ IS SEWIOUS',  j, small)
    r = ''
    t = list1[0]
    print(v)
    x = 0
    while list2[x] < v:
        r += t[x]
        x+=1
        print(x)
    print(r, ' a' )

    print(list3)
except IndexError:
    print('no common prefix')

    
            
            
