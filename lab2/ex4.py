import random

def simualtor_dice4(n):
    count_one_six_one_one = 0

    for _ in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        if (dice1 == 1 and dice2 == 6) or (dice1 == 6 and dice2 == 1):
            count_one_six_one_one += 1

    probability = count_one_six_one_one / n
    return probability

print(simualtor_dice4(100000000))
