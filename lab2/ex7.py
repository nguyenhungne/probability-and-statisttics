import random
from itertools import product

def simulator_poker2(n):
    Ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
    Suits = {'♡', '♢', '♣', '♠'}
    Cards = list(product(Ranks, Suits))
    
    different_suits_count = 0

    for _ in range(n):
        random.shuffle(Cards)
        hand = random.sample(Cards, 4)
        
        suits_in_hand = {card[1] for card in hand}
        
        if len(suits_in_hand) == 4:
            different_suits_count += 1

    probability = different_suits_count / n
    return probability

n = 10000
print("Experimental probability:", simulator_poker2(n))
