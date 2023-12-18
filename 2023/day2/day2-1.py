input = open("input.txt", "r")

maxred = 12
maxgreen = 13
maxblue = 14
idsok = []
sum = 0

# cubes - lines
for line in input:
    line = line.rstrip().split(":")
    gamenum = line[0].split()
    gameid = gamenum[1]
    cubes = line[1].split(";")
    rgbcubes = []
    ok = []

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
        if rgbcubes[i][0] <= 12 and rgbcubes[i][1] <= 13 and rgbcubes[i][2] <= 14:
            rgbcubes[i] = True
            #print(rgbcubes[i])
        else:
            rgbcubes[i] = False
            
    #print(rgbcubes)

    for i in range(len(rgbcubes)):
        ok.append(True)
    #print(ok)
        
    if rgbcubes == ok:
        #print(gameid)
        idsok.append(gameid)

#print(idsok)

for id in idsok:
    sum += int(id)

print(sum)
