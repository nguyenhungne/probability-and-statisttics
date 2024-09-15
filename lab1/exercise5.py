import itertools

suits = ['Spades', 'Clubs', 'Diamond', 'Hearts']
denominations = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

deck = [f"{denom}{suit}" for denom in denominations for suit in suits]

poker_5 = list(itertools.combinations(deck, 5))
len_poker_5 = len(poker_5)
print(len_poker_5)
print(poker_5)

three_of_a_kind = []

for denom in denominations:
    three_cards = list(itertools.combinations([f"{denom}{suit}" for suit in suits], 3))
    
    remaining_deck = [card for card in deck if denom not in card]
    two_cards = list(itertools.combinations(remaining_deck, 2))
    
    for three in three_cards:
        for two in two_cards:
            three_of_a_kind.append(three + two)

len_three_of_a_kind = len(three_of_a_kind)

print(len_poker_5)
print(len_three_of_a_kind)