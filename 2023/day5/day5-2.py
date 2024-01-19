input = open("input.txt", "r")

seeds = []
numbers = []
final_locations = []

seed_to_soil_start = 0
soil_to_fertilizer_start = 0
fertilizer_to_water_start = 0
water_to_light_start = 0
light_to_temperature_start = 0
temperature_to_humidity_start = 0
humidity_to_location_start = 0

seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

seeds_soils = []
seeds_soils_fertilizers = []
seeds_soils_fertilizers_waters = []
seeds_soils_fertilizers_waters_lights = []
seeds_soils_fertilizers_waters_lights_temperatures = []
seeds_soils_fertilizers_waters_lights_temperatures_humidities = []
seeds_soils_fertilizers_waters_lights_temperatures_humidities_locations = []

for linenum, line in enumerate(input):
    if line.startswith("seeds"):
        line = line.split(":")[1].split()
        pair = []
        for i, seed in enumerate(line):
            if i % 2 == 0:
                pair.append(int(seed))
            else:
                pair.append(int(seed))
                seeds.append(pair)
                pair = []

    elif line.startswith("seed"):
        seed_to_soil_start = linenum

    elif line.startswith("soil"):
        soil_to_fertilizer_start = linenum

    elif line.startswith("fertilizer"):
        fertilizer_to_water_start = linenum

    elif line.startswith("water"):
        water_to_light_start = linenum

    elif line.startswith("light"):
        light_to_temperature_start = linenum

    elif line.startswith("temperature"):
        temperature_to_humidity_start = linenum

    elif line.startswith("humidity"):
        humidity_to_location_start = linenum

    elif line[0].isdigit():
        nums = []
        for num in line.rstrip().split():
            nums.append(int(num))
        numbers.append([nums, linenum])

for number in numbers:
    if number[1] > seed_to_soil_start:
        if number[1] < soil_to_fertilizer_start:
            #print(number)
            seed_to_soil.append(number[0])

    if number[1] > soil_to_fertilizer_start:
        if number[1] < fertilizer_to_water_start:
            #print(number)
            soil_to_fertilizer.append(number[0])

    if number[1] > fertilizer_to_water_start:
        if number[1] < water_to_light_start:
            fertilizer_to_water.append(number[0])

    if number[1] > water_to_light_start:
        if number[1] < light_to_temperature_start:
            water_to_light.append(number[0])

    if number[1] > light_to_temperature_start:
        if number[1] < temperature_to_humidity_start:
            light_to_temperature.append(number[0])

    if number[1] > temperature_to_humidity_start:
        if number[1] < humidity_to_location_start:
            temperature_to_humidity.append(number[0])

    if number[1] > humidity_to_location_start:
        humidity_to_location.append(number[0])

for seednum, seed in enumerate(seeds):
    for seed_soil in seed_to_soil:
        if seed[0] >= seed_soil[1]:
            if seed[0] + seed[1] <= seed_soil[1] + seed_soil[2]:
                seeds_soils.append([seed, seed_soil])
                seeds.remove(seeds[seednum])

for seed in seeds:
    seeds_soils.append([seed, [seed[0], seed[0], seed[1]]])

def mapping(input, map, output):
    for i, j in enumerate(input):
        for k in map:
            if j[1][0] >= k[1]:
                if j[1][0] + j[1][2] <= k[1] + k[2]:
                    output.append([j, k])
                    input.remove(input[i])
    for l in input:
        output.append([l, [l[1][0], l[1][0], l[1][2]]])

mapping(seeds_soils, soil_to_fertilizer, seeds_soils_fertilizers)
mapping(seeds_soils_fertilizers, fertilizer_to_water, seeds_soils_fertilizers_waters)
mapping(seeds_soils_fertilizers_waters, water_to_light, seeds_soils_fertilizers_waters_lights)
mapping(seeds_soils_fertilizers_waters_lights, light_to_temperature, seeds_soils_fertilizers_waters_lights_temperatures)
mapping(seeds_soils_fertilizers_waters_lights_temperatures, temperature_to_humidity, seeds_soils_fertilizers_waters_lights_temperatures_humidities)
mapping(seeds_soils_fertilizers_waters_lights_temperatures_humidities, humidity_to_location, seeds_soils_fertilizers_waters_lights_temperatures_humidities_locations)

for i in seeds_soils_fertilizers_waters_lights_temperatures_humidities_locations:
    final_locations.append(i[1][0])

print(min(final_locations))
