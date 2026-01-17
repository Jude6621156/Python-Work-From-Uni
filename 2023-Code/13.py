k = int(input('int '))
s = input('string')

list1 = [i for i in s]
list2 = []


for a, b in enumerate(list1):
    counter = a
    while counter < len(list1):
        x = a
        while x < counter:
            list2.append(list1[x])
            x+=1
        t = 0
        for c in list2:
    
            for d in list2:
                if d == c:
                    list2.remove(d)
        t+=1
            
  
