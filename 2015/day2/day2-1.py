input = open('input.txt', 'r')

areas = []
total = 0

for line in input:
    line = line.rstrip()
    line = line.split('x')
    l = int(line[0])
    w = int(line[1])
    h = int(line[2])
    s1 = l * w
    s2 = w * h
    s3 = h * l
    area = 2 * s1 + 2 * s2 + 2 * s3
    plus = min([s1, s2, s3])
    areaplus = area + plus
    #print(l, w, h, s1, s2, s3, plus, area, areaplus)
    areas.append(areaplus)

for area in areas:
    total += area

print(total)
