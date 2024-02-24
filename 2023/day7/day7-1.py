input = open("input.txt", "r")
    
cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'K']
five_of_a_kind = [5]
four_of_a_kind = [4, 1]
full_house = [3, 2]
three_of_a_kind = [3, 1, 1]
two_pair = [2, 2, 1]
one_pair = [2, 1, 1, 1]
high_card = [1, 1, 1, 1, 1]
ranks = [high_card, one_pair, two_pair, three_of_a_kind, full_house, four_of_a_kind, five_of_a_kind]
hands = []
winnings = []

def sort_hands(hand):
    return hand[4], hand[0][1]

for line in input:
    line = line.split()
    hand = []
    cards_in_hand = []

    for card in line[0]:
        cards_in_hand.append(card)
    hand.append(cards_in_hand)

    card_powers = []
    card_types = []
    for card in hand[0]:
        if card not in card_types:
            card_types.append(card)
        for i in range(len(cards)):
            if card == cards[i]:
                card_powers.append(i + 1)
    hand.append(card_powers)

    cards_counts = []
    for card in card_types:
        count = hand[0].count(card)
        cards_counts.append([card, count])
    hand.append(cards_counts)

    counts = []
    for count in hand[2]:
        counts.append(count[1])
    counts = sorted(counts, reverse = True)
    hand.append(counts)

    for ranknum, rank in enumerate(ranks):
        if hand[3] == rank:
            hand.append(ranknum + 1)

    hand.append(int(line[1]))
    hands.append(hand)

hands = sorted(hands, key = sort_hands, reverse = False)
for rank, hand in enumerate(hands):
    #print(hand)
    winning = (rank + 1) * hand[5]
    #print(winning)
    winnings.append(winning)

total = 0
for winning in winnings:
    total += winning

print(total)
