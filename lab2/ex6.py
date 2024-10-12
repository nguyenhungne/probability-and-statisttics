import random
from itertools import product

def simulator_poker1(n):
    Ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
    Suits = {'♡', '♢', '♣', '♠'}
    Cards = list(product(Ranks, Suits))
    
    all_hearts_count = 0

    for _ in range(n):
        random.shuffle(Cards)
        hand = random.sample(Cards, 5)
        
        if all(card[1] == '♡' for card in hand):
            all_hearts_count += 1

    probability = all_hearts_count / n
    return probability

n = 10000
print("Experimental probability:", simulator_poker1(n))
