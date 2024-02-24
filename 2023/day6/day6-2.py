input = open("input.txt", "r")

time = ''
record = ''
ways_to_beat = 0

for linenum, line in enumerate(input):
    line = line.split()[1:]
    for num in line:
        if linenum == 0:
            time += num
        else:
            record += num
            
for button_hold in range(int(time)):
    print(button_hold, time)
    speed = button_hold
    time_left = int(time) - button_hold
    distance = speed * time_left
    if time_left <= int(time):
        if distance > int(record):
            ways_to_beat += 1

print(ways_to_beat)
