input = open('input.txt', 'r')

col1 = []
col2 = []
similarity_scores = []
similarity_score = 0

for line in input:
    line = line.rstrip()
    line = line.split()
    col1.append(int(line[0]))
    col2.append(int(line[1]))

for num1 in col1:
    similar = 0
    for num2 in col2:
        if num1 == num2:
            similar += 1
    similar *= num1
    similarity_scores.append(similar)

for score in similarity_scores:
    similarity_score += score

print(similarity_score)
