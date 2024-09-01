input = open('input.txt', 'r')

position1 = [0, 0]
position2 = [0, 0]
houses = [(0, 0)]

for line in input:
    line = line.rstrip()
    for i in range(len(line)):
        direction = line[i]
        match direction:
            case '^':
                if i % 2 == 0:
                    position1[1] += 1
                else:
                    position2[1] += 1
            case 'v':
                if i % 2 == 0:
                    position1[1] -= 1
                else:
                    position2[1] -= 1
            case '>':
                if i % 2 == 0:
                    position1[0] += 1
                else:
                    position2[0] += 1
            case '<':
                if i % 2 == 0:
                    position1[0] -= 1
                else:
                    position2[0] -= 1

        house1 = (position1[0], position1[1])
        house2 = (position2[0], position2[1])
        houses.append(house1)
        houses.append(house2)

houses = list(set(houses))
print(len(houses))
