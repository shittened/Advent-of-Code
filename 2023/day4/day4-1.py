input = open("input.txt", "r")

cards = []
points = 0

for line in input:
    line = line.rstrip()
    card = line.split(":")[1].split("|")
    #print(card)
    cards.append(card)
#print(cards)

for cardnum, card in enumerate(cards):
    combo = 0
    for winning in card[0].split():
        for owned in card[1].split():
            if winning == owned:
                if combo == 0:
                    combo = 1
                else:
                    combo *= 2
    #print(combo)
    points += combo

print(points)
