szamok = [['A', [2, 3],[6,6]],['B', [4,5,3],[1,1,3]],['C',3],['D',4],['E',3],['F',4],['I',3],['J',4]]

def ossz(x,y):
    z = []
    for v in range(len(x)):
        pit =[]
        for u in range(len(x[v])):
            pit.append(int(x[v][u]) + int(y[v][u]))
        z.append(pit)
    return z

def szor(x,y):
    z = []
    for abs in range(len(x)):
        zs = []
        for lh in range(len(y[0])):
            zs.append(0)
        z.append(zs)

    for trg in range(len(x)):
        for trb in range(len(y[0])):
            for trh in range(len(x[0])):
                z[trg][trb] += int(x[trg][trh]) * int(y[trh][trb])
    print(z)
    return z
            
    
operations = [['A', '*', 'B', '+', 'A', '*', 'B']]
op = []
for lv in operations:
    ld = []
    for ndd in lv:
        ld.append(ndd)
    op.append(ld)

for dz in operations:
    for dzs in range(len(dz)):
        for c in szamok:
            if c[0] == dz[dzs]:
                dz[dzs]= c[1:]
                
kor = 0
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
            if i[j-1] != "*":
                szorzaskesz.append(i[j])
    print(szorzaskesz)
    
    
    osszkesz = []
    while len(szorzaskesz) != 1:
        for o in range(len(szorzaskesz)-1):
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
                if szorzaskesz[o-1] != "+":
                    osszkesz.append(szorzaskesz[o])
        szorzaskesz = osszkesz
        print(osszkesz)
        h = osszkesz[0]
        for cs in op[kor]:
            print(cs, end=" ")
        print()
        for m in h:
            for n in m:
                print(n, end=" ")
            print()
        kor += 1