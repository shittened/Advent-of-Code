input = open("input.txt", "r")

seeds = []
numbers = []

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

seed2 = []
seed_soil2 = []
seed_soil_fertilizer2 = []
seed_soil_fertilizer_water2 = []
seed_soil_fertilizer_water_light2 = []
seed_soil_fertilizer_water_light_temperature2 = []
seed_soil_fertilizer_water_light_temperature_humidity2 = []

seeds_soils = []
seeds_soils_fertilizers = []
seeds_soils_fertilizers_waters = []
seeds_soils_fertilizers_waters_lights = []
seeds_soils_fertilizers_waters_lights_temperatures = []
seeds_soils_fertilizers_waters_lights_temperatures_humidities = []
seeds_soils_fertilizers_waters_lights_temperatures_humidities_locations = []

final_locations = []

for linenum, line in enumerate(input):
    if line.startswith("seeds"):
        line = line.split(":")[1].split()
        for seed in line:
            seeds.append(int(seed))

    elif line.startswith("seed-"):
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

#print(seeds)
#print(seed_to_soil_start)
#print(soil_to_fertilizer_start)
#print(numbers)
#print(seed_to_soil)
#print(soil_to_fertilizer)
#print(fertilizer_to_water)
#print(water_to_light_start)
#print(light_to_temperature_start)
#print(water_to_light)
#print(light_to_temperature)
#print(temperature_to_humidity)
#print(humidity_to_location_start)
#print(humidity_to_location)

for seed in seeds:
    for numbers in seed_to_soil:
        if seed >= numbers[1]:
            if seed <= numbers[1] + numbers[2]:
                #print(seed, numbers)
                difference = seed - numbers[1]
                soil = numbers[0] + difference
                seeds_soils.append([seed, soil])
                seed2.append(seed)

    if seed not in seed2:
        seeds_soils.append([seed, seed])

#print(len(seeds))
#print(seeds_soils)
#print(len(seeds_soils))

def mapping(source, map, output, output2):
    for i in source:
        for j in map:
            if i[len(i) - 1] >= j[1]:
                if i[len(i) - 1] <= j[1] + j[2]:
                    diff = i[len(i) - 1] - j[1]
                    new_elem = j[0] + diff
                    new_list = []
                    for k in range(len(i)):
                        new_list.append(i[k])
                    new_list.append(new_elem)
                    output.append(new_list)
                    output2.append(i)
        if i not in output2:
            new_list2 = []
            for l in range(len(i)):
                new_list2.append(i[l])
            new_list2.append(i[len(i) - 1])
            output.append(new_list2)

mapping(seeds_soils, soil_to_fertilizer, seeds_soils_fertilizers, seed_soil2)
mapping(seeds_soils_fertilizers, fertilizer_to_water, seeds_soils_fertilizers_waters, seed_soil_fertilizer2)
mapping(seeds_soils_fertilizers_waters, water_to_light, seeds_soils_fertilizers_waters_lights, seed_soil_fertilizer_water2)
mapping(seeds_soils_fertilizers_waters_lights, light_to_temperature, seeds_soils_fertilizers_waters_lights_temperatures, seed_soil_fertilizer_water_light2)
mapping(seeds_soils_fertilizers_waters_lights_temperatures, temperature_to_humidity, seeds_soils_fertilizers_waters_lights_temperatures_humidities, seed_soil_fertilizer_water_light_temperature2)
mapping(seeds_soils_fertilizers_waters_lights_temperatures_humidities, humidity_to_location, seeds_soils_fertilizers_waters_lights_temperatures_humidities_locations, seed_soil_fertilizer_water_light_temperature_humidity2)

#print(seeds_soils_fertilizers)
#print(len(seeds_soils_fertilizers))
#print(seeds_soils_fertilizers_waters)
#print(len(seeds_soils_fertilizers_waters))
#print(seeds_soils_fertilizers_waters_lights)
#print(seeds_soils_fertilizers_waters_lights_temperatures)
#print(len(seeds_soils_fertilizers_waters_lights_temperatures))
#print(len(seeds))
#print(len(seed_soil_fertilizer2))
#print(len(seed_soil2))
#print(len(seeds_soils_fertilizers_waters_lights_temperatures_humidities))
#print(len(seeds_soils_fertilizers_waters_lights_temperatures_humidities[0]))
#print(len(seeds_soils_fertilizers_waters_lights_temperatures_humidities_locations))
#print(len(seeds_soils_fertilizers_waters_lights_temperatures_humidities_locations[0]))

for things in seeds_soils_fertilizers_waters_lights_temperatures_humidities_locations:
    final_locations.append(things[len(things) - 1])

#print(final_locations)
print(min(final_locations))
