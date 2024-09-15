from itertools import combinations

men = ['Man1', 'Man2', 'Man3', 'Man4', 'Man5', 'Man6']
women = ['Woman1', 'Woman2', 'Woman3', 'Woman4', 'Woman5', 'Woman6', 'Woman7', 'Woman8', 'Woman9']

men_combinations = list(combinations(men, 3))
women_combinations = list(combinations(women, 2))

committees = [man_comb + woman_comb for man_comb in men_combinations for woman_comb in women_combinations]

total_committees = len(committees)

print(total_committees)
print(committees)