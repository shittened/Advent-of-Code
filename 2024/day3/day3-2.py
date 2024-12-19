input = open('input.txt', 'r')

lines = []
results = []
final = 0

def mul(bigpart, results):
    bigpart = bigpart.split('mul')

    for part in bigpart:
        if part[0] != '(':
            continue
        part = part[1:]
        part = part.split(')')[0]
        part = part.split(',')
        if len(part) != 2:
            continue
        if not part[0].isnumeric():
            continue
        if not part[1].isnumeric():
            continue
        
        result = int(part[0]) * int(part[1])
        results.append(result)

for line in input:
    line = line.rstrip()
    line = line.split('do')
    lines.append(line)

for i, line in enumerate(lines):
    for j, bigpart in enumerate(line):
        if bigpart.startswith('()'):
            mul(bigpart, results)
        if i == 0:
            if j == 0:
                if not bigpart.startswith('n\'t()'):
                    mul(bigpart, results)

for result in results:
    final += result

print(final)
