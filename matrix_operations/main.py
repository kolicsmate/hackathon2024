sourcefile = open('matrix_operations\input.txt', 'r')
srcwithoutbs = []
next(sourcefile)
for line in sourcefile:
    if line != '\n':
        line = line.strip().split(" ")
        '''if len(line)==1:
        srcwithoutbs.append(line[0])
            else:
                srcwithoutbs.append(line)'''
        srcwithoutbs.append(line)
  
print(srcwithoutbs)
abc = []
newmatrices = []
def matrixAddition(X, Y):
  Z = ''
  for i in range(len(X)):
    Z += str(int(X[i]) + int(Y[i]))
    
  return Z
  
def matrixMultiplication(X,Y,a,b):
  None
  
datainone = ""
x = 0
for i in srcwithoutbs:
  x += 1
  for j in i:
    datainone += j
    if j == 'operations':
      operindex = x
    
print(datainone)

alphindex = []

for a in range(operindex):
  try:
    int(datainone[a])
  except:
    alphindex.append(a)
    continue
  
print(datainone)
print(datainone[alphindex[0]+1:alphindex[1]])
print(alphindex)
print(matrixAddition('1234','1234'))

operations = []
#Matrix adatok betu hanyszor hanyas
while operindex < len(srcwithoutbs):
  operations.append(srcwithoutbs[operindex])
  operindex+= 1
  
print(operations)

def operorder(operation):
  plusindex = []
  multindex = []
  
  for e in range(operation):
    if operation[e] == '+':
      plusindex.append(e)
    if operation[e] == '*':
      multindex.append(e)
      
  for i in multindex:
    matrixMultiplication(operation[i-1], operation[i+1])
    
  for i in plusindex:
    o = matrixAddition(operation[i-1], operation[i+1])
    operation[operation[i+1]:operation[i-1]] = o
  
for operation in operations:
  print(operorder(operation))

