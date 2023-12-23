input = open("input.txt", "r")

digits = []
symbols = []
numbers = []
engineparts = []
sum = 0
used_digits = []
gear_ratios = []

for linenum, line in enumerate(input):
    digits_in_line = []
    line  = line.rstrip()
    for charpos, char in enumerate(line):
        if char != ".":
            if char.isdigit():
                digits_in_line.append([char, charpos, linenum])
            else:
                symbols.append([char, charpos, linenum])
    digits.append(digits_in_line)

for digits_in_line in digits:
    for digit1 in digits_in_line:
        for digit2 in digits_in_line:
            for digit3 in digits_in_line:
                if digit1[1] == digit2[1] + 1:
                    if digit2[1] == digit3[1] + 1:
                        newnum = [digit3[0] + digit2[0] + digit1[0], [digit3[1], digit2[1], digit1[1]], digit1[2]]
                        if digit3 not in used_digits:
                            if digit2 not in used_digits:
                                if digit1 not in used_digits:
                                    numbers.append(newnum)
                                    used_digits.append(digit3)
                                    used_digits.append(digit2)
                                    used_digits.append(digit1)
                                    #print(newnum)

for digits_in_line in digits:
    for digit1 in digits_in_line:
        for digit2 in digits_in_line:
            if digit1[1] == digit2[1] + 1:
                newnum = [digit2[0] + digit1[0], [digit2[1], digit1[1]], digit1[2]]
                if digit2 not in used_digits:
                    if digit1 not in used_digits:
                        numbers.append(newnum)
                        used_digits.append(digit2)
                        used_digits.append(digit1)
                        #print(newnum)

for digits_in_line in digits:
    for digit1 in digits_in_line:
        newnum = [digit1[0], [digit1[1]], digit1[2]]
        if digit1 not in used_digits:
            numbers.append(newnum)
            used_digits.append(digit1)
            #print(newnum)

for symbol in symbols:
    next_to = 0
    adjacent_numbers = []
    for number in numbers:
        if number[2] == symbol[2]:
            if number[1][0] == symbol[1] + 1:
                next_to += 1
                adjacent_numbers.append(number)
            elif number[1][len(number[1]) - 1] == symbol[1] - 1:
                next_to += 1
                adjacent_numbers.append(number)
        elif number[2] == symbol[2] + 1:
            if number[1][0] - 1 <= symbol[1]:
                if number[1][len(number[1]) - 1] + 1 >= symbol[1]:
                    next_to += 1
                    adjacent_numbers.append(number)
        elif number[2] == symbol[2] - 1:
            if number[1][0] - 1 <= symbol[1]:
                if number[1][len(number[1]) - 1] + 1 >= symbol[1]:
                    next_to += 1
                    adjacent_numbers.append(number)
    if symbol[0] == "*":
        if next_to == 2:
            #print(next_to, adjacent_numbers, symbol)
            gear_ratio = int(adjacent_numbers[0][0]) * int(adjacent_numbers[1][0])
            gear_ratios.append(gear_ratio)

for gear_ratio in gear_ratios:
    sum += gear_ratio

print(sum)
#print(gear_ratios)
#print(len(gear_ratios))
