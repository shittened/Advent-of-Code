input = open("input.txt", "r")

allnumbers = []
sum = 0

for line in input:
    numbers = []
    for char in line:
        if char.isdigit():
            numbers.append(char)
    number = str(numbers[0]) + str(numbers[len(numbers) - 1])
    allnumbers.append(int(number))

for i in allnumbers:
    sum += i

print(sum)
