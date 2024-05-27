sourcefile = open('./input.txt', 'r', encoding="utf-8")
lines = []

for line in sourcefile:
    #print(line)
    string = ""
    for char in line.strip():
        if char.isalnum():
            string += char.lower()
      
    lines.append(string)

#print(lines)
  

k =1
for line in lines:
  alphnum = ''

  i = 0
  n = len(line)
  while line[i] == line[n-i-1] and i < n/2:
      if line[i] not in alphnum:
        alphnum += line[i]
      i += 1

  if i < n/2:
    print('NO, -1')
  else:
    print("YES,", len(alphnum))
  k+=1
