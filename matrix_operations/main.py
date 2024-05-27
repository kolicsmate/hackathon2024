sourcefile = open('./input.txt', 'r')
matrices = []
next(sourcefile)

for line in sourcefile:

    if line.strip() != "" and line.strip() != "oper":
        
        matrices.append(line.strip().split(" "))
        
#print(matrices)

matricesonly = []
operonly = []
alphindexes = []
i = 0
operation = False
while i < len(matrices):
    if matrices[i][0] == 'operations':
        operation = True
        i+=1
        continue
    if operation:
        operonly.append(matrices[i])
    else:
        try:
            int(matrices[i][0])
            matricesonly.append(matrices[i])
            for g in matrices[i]:
                if g == '':
                    matrices[i].remove('')
        except:
            matricesonly.append(matrices[i][0])
            alphindexes.append(i)
    i+= 1
alphindexes.append(len(matricesonly))
#print(matricesonly, alphindexes)
veglegesmatrixok = []
for i in range(len(alphindexes)-1):
    veglegesmatrixok.append(matricesonly[alphindexes[i]:alphindexes[i+1]])
    
#print(veglegesmatrixok)
#print(operonly)

#operation



szamok = veglegesmatrixok

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
    #print(z)
    return z
            
    
operations = operonly
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
    #print(szorzaskesz)
    
    
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
        #print(osszkesz)
        h = osszkesz[0]
        for cs in op[kor]:
            print(cs, end=" ")
        print()
        for m in h:
            for n in m:
                print(n, end=" ")
            print()
        if kor != len(operation)-1:
            print()
        kor += 1