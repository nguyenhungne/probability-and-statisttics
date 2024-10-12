import random

def simulator_dice1(n):
    both_even_count = 0
    
    for _ in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        
        if dice1 % 2 == 0 and dice2 % 2 == 0:
            both_even_count += 1
    
    probability = both_even_count / n
    return probability

print(simulator_dice1(10000000))