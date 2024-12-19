input = open('input.txt', 'r')
nice_strings = 0
vowels = ['a', 'e', 'i', 'o', 'u']
strings = ['ab', 'cd', 'pq', 'xy']
nice_strings = 0

def ContainsStrings(line, strings):
    for string in strings:
        if string in line:
            return True
    return False

def ContainsVowels(line, vowels):
    no_vowels = 0
    for char in line:
        for vowel in vowels:
            if char == vowel:
                no_vowels += 1
    if no_vowels >= 3:
        return True
    else:
        return False

def ContainsLettersTwiceInRow(line):
    prev_char = ''
    for char in line:
        if not char == prev_char:
            prev_char = char
        else:
            return True
    return False

for line in input:
    line = line.rstrip()
    #print(line, ContainsVowels(line, vowels))
    #print(line, ContainsStrings(line, strings))
    #print(line, ContainsLettersTwiceInRow(line))

    if ContainsStrings(line, strings):
        continue
    if not ContainsVowels(line, vowels):
        continue
    if not ContainsLettersTwiceInRow(line):
        continue

    nice_strings += 1
print(nice_strings)
