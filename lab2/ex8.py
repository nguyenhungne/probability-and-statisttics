import math

def combinations(n, k):
    return math.comb(n, k)

def probability_two_white_two_blue_two_red():
    total_combinations = combinations(23, 6)
    
    favorable_combinations = combinations(8, 2) * combinations(6, 2) * combinations(9, 2)
    
    probability = favorable_combinations / total_combinations
    return probability

prob = probability_two_white_two_blue_two_red()
print(f"The probability of getting exactly 2 white, 2 blue, and 2 red balls is: {prob}")
