input = open('input.txt', 'r')

intlines = []
safes = []
unsafes = []
tolerated = []

def test(intline, line_to_add, add_to_unsafes):
    if intline != sorted(intline):
        if intline != list(reversed(sorted(intline))):
            if add_to_unsafes:
                unsafes.append(intline)
            return

    for i in range(len(intline)):
        if i + 1 < len(intline):
            if intline[i] == intline[i + 1]:
                if add_to_unsafes:
                    unsafes.append(intline)
                break
            if intline[i] - intline[i + 1] > 3:
                if add_to_unsafes:
                    unsafes.append(intline)
                break
            if intline[i + 1] - intline[i] > 3:
                if add_to_unsafes:
                    unsafes.append(intline)
                break
    else:
        if line_to_add not in safes:
            safes.append(line_to_add)

for line in input:
    line = line.rstrip()
    line = line.split()
    intline = []

    for num in line:
        intline.append(int(num))

    intlines.append(intline)
    
for intline in intlines:
    test(intline, intline, True)

for line in unsafes:
    for i in range(len(line)):
        newline = []
        for j in range(len(line)):
            if i != j:
                newline.append(line[j])
        test(newline, line, False)

print(len(safes))
