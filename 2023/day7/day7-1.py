input = open("input.txt", "r")

hands = []
card_order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
hands_new = []
total_winning = 0

five_of_a_kind  = [0, 0, 0, 0, 5]
four_of_a_kind  = [1, 0, 0, 4, 0]
full_house      = [0, 2, 3, 0, 0]
three_of_a_kind = [2, 0, 3, 0, 0]
two_pair        = [1, 4, 0, 0, 0]
one_pair        = [3, 2, 0, 0, 0]
high_card       = [5, 0, 0, 0, 0]

for linenum, line in enumerate(input):
    line = line.rstrip()
    hands.append(line.split())

for handnum, hand in enumerate(hands):
    cards = hand[0]
    matches = []
    for card1 in cards:
        match = 0
        for card2 in cards:
            #print(card1, card2)
            if card1 == card2:
                match +=1
        #print(matches)
        matches.append(match)
    hands[handnum].append(matches)
    #print(hand[2])

    nums = hand[2]
    nums.sort()
    #print(nums)
    one, two, three, four, five = 0, 0, 0, 0, 0
    for num in nums:
        if num == 1:
            one += 1
        elif num == 2:
            two += 1
        elif num == 3:
            three += 1
        elif num == 4:
            four += 1
        elif num == 5:
            five += 1

    count = [one, two, three, four, five]
    power = 0
    #print(count, nums)
    if count == five_of_a_kind:
        power = 7
    elif count == four_of_a_kind:
        power = 6
    elif count == full_house:
        power = 5
    elif count == three_of_a_kind:
        power = 4
    elif count == two_pair:
        power = 3
    elif count == one_pair:
        power = 2
    elif count == high_card:
        power = 1
    hand.append(power)
    #hand.append(1)

def sorting(e):
    return e[3]

hands.sort(key = sorting, reverse = True)

for handnum, hand in enumerate(hands):
    cards = hand[0]
    cards_power = [0, 0, 0, 0, 0]
    for no, card_no in enumerate(card_order):
        for card_pos, card in enumerate(cards):
            if card == card_no:
                cards_power[card_pos] = no
    #print(cards_power)
    hand.append(cards_power)

hands = sorted(hands, key = lambda x: (x[3], x[4]), reverse = True)

#print(hands)
for hand in hands:
    print(hand)

for linenum, hand in enumerate(hands):
   hand.append(int(hand[1]) * (linenum + 1))
   #print(hand)
   total_winning += hand[5]

print(total_winning)
