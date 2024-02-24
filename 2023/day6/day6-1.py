input = open("input.txt", "r")

times = []
distances = []
races = []
list_ways_to_beat = []

for linenum, line in enumerate(input):
    line = line.split()[1:]
    for num in line:
        if linenum == 0:
            times.append(num)
        else:
            distances.append(num)

for i in range(len(times)):
    race = []
    race.append(int(times[i]))
    race.append(int(distances[i]))
    races.append(race)

for racenum, race in enumerate(races):
    time = race[0]
    record = race[1]
    ways_to_beat = 0
    for button_hold in range(time):
        speed = button_hold
        time_left = time - button_hold
        distance = speed * time_left
        if time_left <= time:
            if distance > record:
                ways_to_beat += 1
    list_ways_to_beat.append(ways_to_beat)

margin_of_error = 1
for i in list_ways_to_beat:
    margin_of_error *= i

print(margin_of_error)
