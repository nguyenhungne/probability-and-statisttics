import math
import matplotlib.pyplot as plt

def pmf_bernoulli(p, x):
	if x == 1:
		return p
	return 1 - p

def plot_pmf_bernoulli(p):
	X = [0,1]
	P_bernoulli = [pmf_bernoulli(p,x) for x in X]

	plt.plot(X, P_bernoulli, 'o')
	plt.title('PMF of P_bernoulli(p=%.2f)' % p)
	plt.xlabel('Value')
	plt.ylabel('Probability')
	plt.show()

plot_pmf_bernoulli(0.5)

"""B/ Binomial distribution"""
def combination(total_items, selected_items):
    return math.factorial(total_items) / (math.factorial(selected_items) * math.factorial(total_items - selected_items))

def pmf_binom(successes, trials, success_prob):
    return combination(trials, successes) * math.pow(success_prob, successes) * math.pow(1 - success_prob, trials - successes)

def plot_pmf_binom(num_trials, success_probability):
    num_successes = list(range(0, num_trials + 1))
    
    probabilities = [pmf_binom(success, num_trials, success_probability) for success in num_successes]

    plt.plot(num_successes, probabilities, '-o')

    axes = plt.gca()
    axes.set_xlim([0, num_trials])
    axes.set_ylim([0, 1.1 * max(probabilities)])

    plt.title('PMF of Binomial Distribution (n=%i, p=%.2f)' % (num_trials, success_probability))
    plt.xlabel('Number of successes (k)')
    plt.ylabel('Probability of k successes')
    
    plt.show()

"""Poisson distribution"""

def pmf_poisson(k, lamda):
	return math.pow(lamda, k) * math.pow(math.e, -1 * lamda) / math.factorial(k)

def plot_pmf_poisson(max_events, average_rate):
    """Plot the Poisson probability mass function."""
    event_counts = list(range(0, max_events + 1))
    probabilities = [pmf_poisson(event_count, average_rate) for event_count in event_counts]

    plt.plot(event_counts, probabilities, '-o')

    plt.title('PMF of Poisson Distribution (λ=%i)' % (average_rate))
    plt.xlabel('Number of events')
    plt.ylabel('Probability')
    plt.show()

"""D/ Geometric distribution"""

def pmf_geo(success_probability, num_failures):
    """Calculate the probability mass function of the geometric distribution."""
    return success_probability * math.pow(1 - success_probability, num_failures)

def plot_pmf_geo(success_probability, max_failures):
	"""Plot the probability mass function of the geometric distribution."""
	failure_counts = list(range(0, max_failures + 1))
	probabilities = [pmf_geo(success_probability, failures) for failures in failure_counts]

	plt.plot(failure_counts, probabilities, '-o')

	plt.title('PMF of Geometric Distribution (p=%.2f)' % success_probability)
	plt.xlabel('Number of failures before success')
	plt.ylabel('Probability')
	plt.show()

"""Ex 1: One factory has 5 machines. The probability of each machine is broken in 1 session is 0.1.
- (a) Use probability distribution functions to calculate the probability that 2 machines are broken in 1 session. (Answer: 0.073)
- (b) Call X = {0, 1, 2, 3, 4, 5} is the event that in 1 session there are 0, 1, 2, 3, 4, and 5 broken machines respectively. Draw a graph representing the relationship between X and the corresponding probability.

"""

print(pmf_binom(2, 5, 0.1))
plot_pmf_binom(5, 0.1)

"""Ex2: A post office receives an average of 3 phone calls per minute.
- (a) Use probability distribution functions to calculate the probability that the center receives 2 calls in 1 minute. (Answer: 0.224)
- (b) Call X = {1, 2, 3, 4, 5} as an event in 1 minute there are 1, 2, 3, 4, 5 respectively calls to the post office. Draw a graph representing the relationship between X and the corresponding probability.
"""

print(pmf_poisson(2, 3))
plot_pmf_poisson(5,3)

"""Ex3: Each person is given 10 bullets and fired until 1 member hits the target. Knowing the probability of each bullet being hit is 40%.
- (a) Use probability distribution functions to calculate the probability that a person hits the target in his third try. (Answer: 0.144)
- (b) Call X = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} as the event where a person hits the target in his 1st, 2nd, 3rd, ..., 10th try. Draw a graph representing the relationship between X and the corresponding probability.
"""

print(pmf_geo(0.4,2))
plot_pmf_geo(0.4,10)
