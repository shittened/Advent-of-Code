input = open('input.txt', 'r')
lines = []
goodparts = []
muls = []
total = 0

for line in input:
    line = line.rstrip()
    lines.append(line)

for i, line in enumerate(lines):
    line = line.split('do')
    for j, part in enumerate(line):
        if not part.startswith('()'):
            continue
        goodparts.append(part)
        if i == 0 and j == 0:
            goodparts.append(part)

for part in goodparts:
    part = part.split('mul')
    for smallpart in part:
        if not smallpart.startswith('('):
            continue
        smallpart = smallpart.split('(')[1]
        smallpart = smallpart.split(')')[0]
        smallpart = smallpart.split(',')
        if len(smallpart) != 2:
            continue
        if not smallpart[0].isnumeric():
            continue
        if not smallpart[1].isnumeric():
            continue
        mul = int(smallpart[0]) * int(smallpart[1])
        muls.append(mul)

for mul in muls:
    total += mul

print(total)
