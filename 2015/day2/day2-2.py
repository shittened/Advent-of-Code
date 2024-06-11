input = open('input.txt', 'r')

ribbons = []
total = 0

for line in input:
    line = line.rstrip()
    line = line.split('x')
    l = int(line[0])
    w = int(line[1])
    h = int(line[2])
    p1 = 2 * l + 2 * w
    p2 = 2 * w + 2 * h
    p3 = 2 * h + 2 * l
    p = min([p1, p2, p3])
    v = l * w * h
    ribbon = p + v
    ribbons.append(ribbon)

for ribbon in ribbons:
    total += ribbon

print(total)
