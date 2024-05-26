szamok = [['A', 1],['B', 2],['C',3],['D',4],['E',3],['F',4],['I',3],['J',4]]

def ossz(x,y):
    z = x + y
    return z

def szor(x,y):
    z = x*y
    return z
    
operations = [['A', '+', 'B'], ['B', '+', 'B', '+', 'A'], ['C', '+', 'D', '+', 'D', '+', 'C'], ['E', '*', 'F', '+', 'I', '*', 'J']]

for dz in operations:
    for dzs in range(len(dz)):
        for c in szamok:
            if c[0] == dz[dzs]:
                dz[dzs]= c[1]

for i in operations:
    matrixbetuk = []
    muveletek = []
    szorzaskesz = []
    for j in range(len(i)):
        if i[j]=="*":
            szorzaskesz.pop()
            szorzaskesz.append(szor(i[j-1],i[j+1]))
        elif i[j] != "+" and len(szorzaskesz) > 0 and type(szorzaskesz[len(szorzaskesz)-1]) == int:
            continue
        else:
            szorzaskesz.append(i[j])
    print(szorzaskesz)
    
    
    osszkesz = []
    while len(szorzaskesz) != 1:
        for o in range(len(szorzaskesz)):
            if szorzaskesz[o] == '+':
                if len(osszkesz) > 0:
                    osszkesz.append(ossz(osszkesz[0], szorzaskesz[o+1]))
                    del(osszkesz[0])
                else:
                    osszkesz.pop()
                    osszkesz.append(ossz(szorzaskesz[0], szorzaskesz[o+1]))
            elif len(osszkesz) > 0 and type(osszkesz[len(osszkesz)-1]) == int:
                continue
            else:
                osszkesz.append(szorzaskesz[o])
        szorzaskesz = osszkesz
        print(osszkesz)  