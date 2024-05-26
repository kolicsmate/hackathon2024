sourcefile = open('matrix_operations\input.txt', 'r')
matrices = []
next(sourcefile)

for line in sourcefile:

    if line.strip() != "" and line.strip() != "oper":
        matrices.append(line.strip().split(" "))
        
operations=[]
onlymatrices = []
for i in range(len(matrices)):
    if len(matrices[i]) == 1:
        onlymatrices.append(['A',])
    







print(matrices)