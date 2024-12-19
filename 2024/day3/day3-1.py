input = open('input.txt', 'r')

results = []
final = 0

for line in input:
    line = line.rstrip()
    line = line.split('mul')
    
    for part in line:
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

for result in results:
    final += result

print(final)
