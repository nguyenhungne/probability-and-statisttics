import random

def simualtor_dice5(n):
    count_sum_large_six = 0

    for _ in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        if dice1 + dice2 > 6:
            count_sum_large_six += 1

    probability = count_sum_large_six / n
    return probability

print(simualtor_dice5(100000000))
