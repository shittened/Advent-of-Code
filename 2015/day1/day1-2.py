input = open('input.txt', 'r')

floor = 0

for line in input:
    line = line.rstrip()
    for charpos, char in enumerate(line):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        if floor == -1:
            print(charpos + 1)
            break
