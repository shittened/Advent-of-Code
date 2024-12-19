input = open('input.txt', 'r')

col1 = []
col2 = []
lenghts = []
total = 0

for line in input:
    line = line.rstrip()
    line = line.split()
    col1.append(int(line[0]))
    col2.append(int(line[1]))

col1 = sorted(col1)
col2 = sorted(col2)

for i in range(len(col1)):
    lenght = 0

    if col1[i] > col2[i]:
        lenght = col1[i] - col2[i]
    else:
        lenght = col2[i] - col1[i]
    
    lenghts.append(lenght)

for lenght in lenghts:
    total += lenght

print(total)
