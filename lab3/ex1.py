from fractions import Fraction

def P(event, space):
    return Fraction(len(event & space), len(space))

S = {'MMM', 'MMF', 'MFM', 'MFF', 'FMM', 'FMF', 'FFM', 'FFF'}

B = {s for s in S if 'F' in s}

A = {'FFF'}

P_B = P(B, S)
P_A_B = P(A & B, S)

P_A_given_B = P_A_B / P_B

print(f"Conditional probability P(A|B) is: {P_A_given_B}")
