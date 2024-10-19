import itertools
import random
from fractions import Fraction

# (a) Create a set Cards to store cards in the form '10♠', '10♡', etc.
suits = ['♠', '♣', '♦', '♡']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
Cards = {f"{rank}{suit}" for rank in ranks for suit in suits}

# (b) Randomly collect 3 cards, save the elements in variable B
B = set(random.sample(Cards, 3))

# (c) Event A1: 3 cards include 1 or 2 Kings (K)
A1 = set()
for combination in itertools.combinations(Cards, 3):
    count_k = sum(1 for card in combination if 'K' in card)
    if count_k == 1 or count_k == 2:
        A1.add(combination)

# (d) Event A2: 3 cards include at least 1 King (K)
A2 = set()
for combination in itertools.combinations(Cards, 3):
    if any('K' in card for card in combination):
        A2.add(combination)

# (e) Calculate the probability of two events A1 and A2
def P(event, space):
    return Fraction(len(event), len(space))

# Total possible combinations of 3 cards
total_combinations = set(itertools.combinations(Cards, 3))

# Calculate probabilities
P_A1 = P(A1, total_combinations)
P_A2 = P(A2, total_combinations)

# Print results
print(f"Randomly selected cards B: {B}")
print(f"P(A1) = {P_A1}, P(A2) = {P_A2}")
