cards = open('input.txt').readlines()

count = 0
multiplier = [1 for _ in cards]

for i, card in enumerate(cards):
    card = card.split(":")[1].split("|")

    winning = set([int(x) for x in card[0].strip().split()])
    have = set(int(x) for x in card[1].strip().split())

    wins = set(x for x in have if x in winning)

    cmultiplier = multiplier[i]

    for j in range(i + 1, min(i + len(wins) + 1, len(cards))):
        multiplier[j] += cmultiplier

    count += cmultiplier

print(count)
