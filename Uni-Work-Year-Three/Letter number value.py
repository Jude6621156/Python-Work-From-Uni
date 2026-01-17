dict = {}
for i in range(65, 91):
    dict.update({chr(i): i})


def l(a):
    b = a.upper()
    total = 0
    for c in b:
        d = ord(c) - 64
        total+=d

    print(total)

PWEEZ = input('pweez')
l(PWEEZ)
    
    
    
