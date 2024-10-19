import numpy as np
import collections

# (a) Save the results of flipping 2 coins 10,000 times into the variable x
# 0 = no heads, 1 = one head, 2 = two heads
x = np.random.binomial(2, 0.5, 10000)

# (b) Find the values of random variable X
# In this case, X represents the number of heads in each trial, so the values in x are already the values of X.
X = x

# (c) Calculate the probability distribution function of X
value_counts = collections.Counter(x)
total_trials = len(x)
P = {k: v / total_trials for k, v in value_counts.items()}

# (d) Calculate the characteristic parameters of random variable X: expectation, variance, standard deviation
mean_x = np.mean(x)  # Kỳ vọng (trung bình)
variance_x = np.var(x)  # Phương sai
std_dev_x = np.std(x)  # Độ lệch chuẩn

# (e) Calculate the probability to have at least one head
# X >= 1 corresponds to having at least one head
prob_at_least_one_head = sum(P[k] for k in range(1, 3))

# Output the results
print(f"Values of random variable X (sample): {X[:10]}")
print(f"Probability distribution (P): {P}")
print(f"Expectation (Mean): {mean_x}")
print(f"Variance: {variance_x}")
print(f"Standard Deviation: {std_dev_x}")
print(f"Probability of having at least one head: {prob_at_least_one_head}")
