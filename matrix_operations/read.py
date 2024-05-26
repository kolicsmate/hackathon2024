sourcefile = open('matrix_operations\input.txt', 'r')
matrices = []
next(sourcefile)

for line in sourcefile:

    if line.strip() != "" and line.strip() != "oper":
        
        matrices.append(line.strip().split(" "))
        
print(matrices)

matricesonly = []
alphindexes = []
i = 0
while matrices[i][0] != 'operations':
    try:
        int(matrices[i][0])
        matricesonly.append(matrices[i])
    except:
        matricesonly.append(matrices[i][0])
        alphindexes.append(i)
    i+= 1
        
print(matricesonly, alphindexes)
veglegesmatrixok = []
'''for i in range((len(matricesonly))):'''
    
    
        