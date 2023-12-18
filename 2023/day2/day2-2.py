input = open("input.txt", "r")

powers = []
sum = 0

# cubes - lines
for line in input:
    line = line.rstrip().split(":")
    gamenum = line[0].split()
    gameid = gamenum[1]
    cubes = line[1].split(";")
    rgbcubes = []
    #print(cubes)
    maxred = 0
    maxgreen = 0
    maxblue = 0


    #sets
    for set in cubes:
        set = set.split(",")
        #print(set)
        red = 0
        green = 0
        blue = 0
        
        #cube
        for cube in set:
            cube = cube.split()
            #print(cube)
            color = cube[1]
            amount = cube[0]

            if color == "red":
                red = int(amount)
                #print(red, "red")
            elif color == "green":
                green = int(amount)
                #print(green, "green")
            elif color == "blue":
                blue = int(amount)
                #print(blue, "blue")

        rgb = [red, green, blue]
        #print(rgb)
        rgbcubes.append(rgb)
    #print(rgbcubes)

    for i in range(len(rgbcubes)):
        #print(rgbcubes[i][0])
        #print(rgbcubes[i])
        red = rgbcubes[i][0]
        green = rgbcubes[i][1]
        blue = rgbcubes[i][2]
        if red > maxred:
            maxred = red
        if green > maxgreen:
            maxgreen = green
        if blue > maxblue:
            maxblue = blue
    
    #print(maxred, maxgreen, maxblue)
    power = maxred * maxgreen * maxblue
    #print(power)
    powers.append(power)
    #print(powers)

for power in powers:
        sum += int(power)

print(sum)
