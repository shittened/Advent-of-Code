import time

input = open("input.txt", "r")

directions = []
nodes = []
path = []

for linenum, line in enumerate(input):
    line = line.rstrip()
    if linenum == 0:
        for char in line:
            directions.append(char)

    elif linenum > 1:
        line = line.split()
        current_node = line[0]
        next_nodes = []
        next_nodes.append(line[2].split("(")[1].split(",")[0])
        next_nodes.append(line[3].split(")")[0])
        nodes.append([current_node, next_nodes])

for directionpos, direction in enumerate(directions):
    if direction == "L":
        directions[directionpos] = 0
    else:
        directions[directionpos] = 1

nodes = sorted(nodes, key = lambda x: x[0])
path.append(nodes[0])
directions += directions
directions += directions
directions += directions
directions += directions

print(directions[:5])
for location in path:
    for direction in directions:
        for node in nodes:
            if node[0] == location[1][direction]:
                if path[len(path) - 1][0] != "ZZZ":
                    if path[len(path) - 1] != node:
                        print(node, location, direction)
                        path.append(node)

#print(len(directions))
#for node in nodes:
#    print(node)
#print(path)
#print(len(path), len(nodes))
#for location in path:
#    print(location)
#    if location[0] == "ZZZ":
#        print(location)
print(len(path))
