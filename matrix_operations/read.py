sourcefile = open('matrix_operations\input.txt', 'r')
matrices = []
next(sourcefile)

for line in sourcefile:

    if line.strip() != "" and line.strip() != "oper":
        
        matrices.append(line.strip().split(" "))
        
print(matrices)

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

print(matricesonly, alphindexes)
veglegesmatrixok = []
for i in range(len(alphindexes)-1):
    veglegesmatrixok.append(matricesonly[alphindexes[i]:alphindexes[i+1]])
    
print(veglegesmatrixok)
print(operonly)

