input = open("input.txt", "r")

allnumbers = []
sum = 0

digits = ('zero', 'one', 'two', 'three', 'four',
          'five', 'six', 'seven', 'eight', 'nine')

for line in input:
    numbers = []

    for charpos, char in enumerate(line):
        if char.isdigit():
            numbers.append(char)
        for digit, digitname in enumerate(digits):
            if line[charpos:].startswith(digitname):
                numbers.append(digit)

    allnumbers.append(str(numbers[0]) + str(numbers[len(numbers) - 1]))

for number in allnumbers:
    sum += int(number)

print(sum)
