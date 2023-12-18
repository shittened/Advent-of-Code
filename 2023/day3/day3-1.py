input = open("input.txt", "r")

dots = []
digits = []
used_digits = []
symbols = []
numbers = []
number = None
engineparts = []
sum = 0

for linenum, line in enumerate(input):
    line  = line.rstrip()
    for charpos, char in enumerate(line):
        if char == ".":
            dots.append([char, charpos, linenum])
        elif char.isdigit():
            digits.append([char, charpos, linenum])
        else:
            symbols.append([char, charpos, linenum])
    #print(linenum)

#print(dots)
#print(digits)
#print(symbols)

for i, digit in enumerate(digits):
    if i + 1 < len(digits):
        if digit[1] == digits[i + 1][1] - 1: 
            #print(digit, digits[i + 1])
            #if digit not in used_digits:
            #    used_digits.append(digit)
            if number == None:
                number = []
                number.append(str(digit[0]))
                number.append([str(digit[1])])
                number.append(str(digit[2]))
            else:
                number[0] = str(number[0]) + str(digit[0])
                number[1].append(str(digit[1]))
                number[2] = str(digit[2])
        else:
            if number != None:
                number[0] = str(number[0]) + str(digit[0])
                number[1].append(str(digit[1]))
                number[2] = str(digit[2])

            numbers.append(number)
            number = None

#for num in numbers:
#    if num == None:
#        print(num)
    #print(number[2])
#for symbol in symbols:
#    print(symbol[2])

for num in numbers:
    if num != None:
        for symbol in symbols:
            if int(num[2]) == int(symbol[2]):
                #print(num, symbol)
                if int(num[1][0]) == int(symbol[1]) + 1:
                    #print(num, symbol)
                    if not num in engineparts:
                        engineparts.append(num)
                elif int(num[1][len(num[1]) - 1]) == int(symbol[1]) - 1:
                    #print(num, symbol)
                    if not num in engineparts:
                        engineparts.append(num)

            elif int(num[2]) == int(symbol[2]) + 1:
                #print(num, symbol)
                if str(symbol[1]) in num[1]:
                    #print(num, symbol)
                    if not num in engineparts:
                        engineparts.append(num)
                elif str(symbol[1] + 1) in num[1]:
                    #print(num, symbol)
                    if not num in engineparts:
                        engineparts.append(num)
                elif str(symbol[1] - 1) in num[1]:
                    #print(num, symbol)
                    if not num in engineparts:
                        engineparts.append(num)

            elif int(num[2]) == int(symbol[2]) - 1:
                #print(num, symbol)
                if str(symbol[1]) in num[1]:
                    #print(num, symbol)
                    if not num in engineparts:
                        engineparts.append(num)
                elif str(symbol[1] + 1) in num[1]:
                    #print(num, symbol)
                    if not num in engineparts:
                        engineparts.append(num)
                elif str(symbol[1] - 1) in num[1]:
                    #print(num, symbol)
                    if not num in engineparts:
                        engineparts.append(num)

for part in engineparts:
    sum += int(part[0])

print(sum)
#print(engineparts)
#print(type(numbers[0][2]))
#print(digits[0])
#print(type(symbols[0][2]))
