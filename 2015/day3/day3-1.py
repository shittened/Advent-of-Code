input = open('input.txt', 'r')

position = [0, 0]
houses = [(0, 0)]

for line in input:
    line = line.rstrip()
    for char in line:
        direction = char
        match direction:
            case '^':
                position[1] += 1
            case 'v':
                position[1] -= 1
            case '>':
                position[0] += 1
            case '<':
                position[0] -= 1
        house = (position[0], position[1])
        houses.append(house)

houses = list(set(houses))
print(len(houses))
