input = open('input.txt', 'r')

safes = []

for line in input:
    line = line.rstrip()
    line = line.split()
    intline = []

    for num in line:
        intline.append(int(num))
    
    if intline != sorted(intline):
        if intline != list(reversed(sorted(intline))):
            continue

    for i in range(len(intline)):
        if i + 1 < len(intline):
            if intline[i] == intline[i + 1]:
                break
            if intline[i] - intline[i + 1] > 3:
                break
            if intline[i + 1] - intline[i] > 3:
                break
    else:
        if intline not in safes:
            safes.append(intline)

print(len(safes))
