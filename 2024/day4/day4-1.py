input = open('input.txt', 'r')
strings = ['XMAS', 'SAMX']
strings_total = 0
lines = []
checked = []

for line in input:
    line = line.rstrip()
    strings_in_line = 0

    for string in strings:
        strings_in_line += line.count(string)

    strings_total += strings_in_line
    lines.append(line)

for i, line in enumerate(lines):
    for j, char in enumerate(line):

        if lines[i][j] == 'X':
            if i + 3 < len(lines):
                if lines[i + 1][j] == 'M':
                    to_check = [[i, j], [i + 1, j], [i + 2, j], [i + 3, j]]
                    if to_check not in checked:
                        if lines[i + 2][j] == 'A':
                            if lines[i + 3][j] == 'S':
                                strings_total += 1
                                checked.append(to_check)

                if j - 3 >= 0:
                    to_check = [[i, j], [i + 1, j - 1], [i + 2, j - 2], [i + 3, j - 3]]
                    if to_check not in checked:
                        if lines[i + 1][j - 1] == 'M':
                            if lines[i + 2][j - 2] == 'A':
                                if lines[i + 3][j - 3] == 'S':
                                    strings_total += 1
                                    checked.append(to_check)

                if j + 3 < len(line):
                    to_check = [[i, j], [i + 1, j + 1], [i + 2, j + 2], [i + 3, j + 3]]
                    if to_check not in checked:
                        if lines[i + 1][j + 1] == 'M':
                            if lines[i + 2][j + 2] == 'A':
                                if lines[i + 3][j + 3] == 'S':
                                    strings_total += 1
                                    checked.append(to_check)

            if i - 3 >= 0:
                if lines[i - 1][j] == 'M':
                    to_check = [[i, j], [i - 1, j], [i - 2, j], [i - 3, j]]
                    if to_check not in checked:
                        if lines[i - 2][j] == 'A':
                            if lines[i - 3][j] == 'S':
                                strings_total += 1
                                checked.append(to_check)

                if j - 3 >= 0:
                    to_check = [[i, j], [i - 1, j - 1], [i - 2, j - 2], [i - 3, j - 3]]
                    if to_check not in checked:
                        if lines[i - 1][j - 1] == 'M':
                            if lines[i - 2][j - 2] == 'A':
                                if lines[i - 3][j - 3] == 'S':
                                    strings_total += 1
                                    checked.append(to_check)

                if j + 3 < len(line):
                    to_check = [[i, j], [i - 1, j + 1], [i - 2, j + 2], [i - 3, j + 3]]
                    if to_check not in checked:
                        if lines[i - 1][j + 1] == 'M':
                            if lines[i - 2][j + 2] == 'A':
                                if lines[i - 3][j + 3] == 'S':
                                    strings_total += 1
                                    checked.append(to_check)

        elif lines[i][j] == 'S':
            if i + 3 < len(lines):
                if lines[i + 1][j] == 'A':
                    to_check = [[i, j], [i + 1, j], [i + 2, j], [i + 3, j]]
                    if to_check not in checked:
                        if lines[i + 2][j] == 'M':
                            if lines[i + 3][j] == 'X':
                                strings_total += 1
                                checked.append(to_check)

                if j - 3 >= 0:
                    to_check = [[i, j], [i + 1, j - 1], [i + 2, j - 2], [i + 3, j - 3]]
                    if to_check not in checked:
                        if lines[i + 1][j - 1] == 'A':
                            if lines[i + 2][j - 2] == 'M':
                                if lines[i + 3][j - 3] == 'X':
                                    strings_total += 1
                                    checked.append(to_check)

                if j + 3 < len(line):
                    to_check = [[i, j], [i + 1, j + 1], [i + 2, j + 2], [i + 3, j + 3]]
                    if to_check not in checked:
                        if lines[i + 1][j + 1] == 'A':
                            if lines[i + 2][j + 2] == 'M':
                                if lines[i + 3][j + 3] == 'X':
                                    strings_total += 1
                                    checked.append(to_check)
            if i - 3 >= 0:
                if lines[i - 1][j] == 'A':
                    to_check = [[i, j], [i - 1, j], [i - 2, j], [i - 3, j]]
                    if to_check not in checked:
                        if lines[i - 2][j] == 'M':
                            if lines[i - 3][j] == 'X':
                                strings_total += 1
                                checked.append(to_check)

                if j - 3 >= 0:
                    to_check = [[i, j], [i - 1, j - 1], [i - 2, j - 2], [i - 3, j - 3]]
                    if to_check not in checked:
                        if lines[i - 1][j - 1] == 'A':
                            if lines[i - 2][j - 2] == 'M':
                                if lines[i - 3][j - 3] == 'X':
                                    strings_total += 1
                                    checked.append(to_check)

                if j + 3 < len(line):
                    to_check = [[i, j], [i - 1, j + 1], [i - 2, j + 2], [i - 3, j + 3]]
                    if to_check not in checked:
                        if lines[i - 1][j + 1] == 'A':
                            if lines[i - 2][j + 2] == 'M':
                                if lines[i - 3][j + 3] == 'X':
                                    strings_total += 1
                                    checked.append(to_check)

print(strings_total)
