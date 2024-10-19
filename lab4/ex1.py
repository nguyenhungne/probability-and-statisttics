import numpy as np
import collections

# (a) Determine the values of the random variable X and store it in variable X
x = np.random.choice([0, 1, 2, 3, 4, 5], 3650, p=[0.1, 0.2, 0.3, 0.2, 0.15, 0.05])

# (b) Calculate the probability distribution function of X and store it in variable P
value_counts = collections.Counter(x)  # Count occurrences of each value in x
probability_distribution = {}  # Calculate probability for each value
total_days = len(x)
for value, count in value_counts.items():
    probability_distribution[value] = count / total_days

# (c) Calculate the characteristic parameters of X: expectation, variance, standard deviation
mean_x = np.mean(x)
variance_x = np.var(x)
standard_deviation_x = np.std(x)

# (d) Calculate the probability of having 3 or more emergency cases
prob_3_or_more = np.sum([probability_distribution.get(i, 0) for i in [3, 4, 5]])

# Output the results
print(f"Values of the random variable X: {x[:10]} (first 10 values for preview)")
print(f"Probability distribution (P): {probability_distribution}")
print(f"Expectation (Mean): {mean_x}")
print(f"Variance: {variance_x}")
print(f"Standard Deviation: {standard_deviation_x}")
print(f"Probability of having 3 or more emergency cases: {prob_3_or_more}")
