from collections import Counter

input = open('input.txt', 'r')
nice_strings = 0

def containsStrings(text):
    strings = ['ab', 'cd', 'pq', 'xy']

    for string in strings:
        if string in text:
            return True

    return False

def threeVowels(text):
    vowels = 'aeiou'
    count = 0

    for vowel in vowels:
        for letter in text:
            if count >= 3:
                break
            if letter == vowel:
                count += 1

    if count >= 3:
        return True
    else:
        return False

def repeatingLetter(text):
    letters = Counter(text)
    for i in letters.values():
        if i > 1:
            return True
    return False

for line in input:
    line = line.rstrip()

    if containsStrings(line):
        continue

    if not threeVowels(line):
        continue

    if not repeatingLetter(line):
        continue

    print(line)
    nice_strings += 1
    print('nice strings: ' + str(nice_strings)) #TOO LOW
