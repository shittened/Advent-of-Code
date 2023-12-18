input = open("input.txt", "r")

cards = []
total = 0

for line in input:
    line = line.rstrip()
    card = line.split(":")[1].split("|")
    #print(card)
    cards.append(card)
#print(cards)

total = len(cards)

for cardnum, card in enumerate(cards):
    matches = 0
    for winning in card[0].split():
        for owned in card[1].split():
            if winning == owned:
                matches += 1
    #print(matches)
    total += matches

print(total)
