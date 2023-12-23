input = open("input.txt", "r")

times = []
distances = []
records = []
margin_of_err = 1

for linenum, line in enumerate(input):
    line = line.rstrip()
    line = line.split()
    line.remove(line[0])
    for num in line:
        if linenum == 0:
            times.append(int(num))
        else:
            distances.append(int(num))

for time in times:
    good_times = 0
    for distance in distances:
        for hold in range(time):
            hold += 1
            speed = hold
            current_time = time - hold
            dist = hold * current_time
            if dist > distance:
                good_times += 1
    if good_times > 0:
        records.append(good_times)
        #print(good_times)

for record in records:
    margin_of_err *= record
    print(margin_of_err)

print(margin_of_err)
