import random

def simualtor_dice3(n):
    the_same_count = 0

    for _ in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        if dice1 == dice2:
            the_same_count += 1

    probability = the_same_count / n
    return probability

print(simualtor_dice3(100000000))
