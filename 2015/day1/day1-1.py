input = open('input.txt', 'r')

floor = 0

for line in input:
    line = line.rstrip()
    for char in line:
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1

print(floor)
