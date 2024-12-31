input = open('input.txt', 'r')

rules = []
updates =[]

for line in input:
    line = line.rstrip()
    if len(line) == 0:
        continue
    if '|' in line:
        rule = [int(line[:2]), int(line[3:])]
        rules.append(rule)
    else:
        update = []
        line = line.split(',')
        for num in line:
            update.append(int(num))
        updates.append(update)

for update in updates:
    for rule in rules:
        if rule[0] not in update:
            continue
        if rule[1] not in update:
            continue
        for i, num1 in enumerate(update):
            for j, num2 in enumerate(update):
                pass
