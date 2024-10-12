import random

def simualtor_dice2(n):
    one_even_one_odd_count = 0

    for _ in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        if (dice1 % 2 == 0 and dice2 % 2 != 0) or (dice1 % 2 != 0 and dice2 % 2 == 0):
            one_even_one_odd_count += 1

    probability = one_even_one_odd_count / n
    return probability

print(simualtor_dice2(1000000000))