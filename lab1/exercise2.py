import itertools

def cross(A, B):
    '''The set of ways of concatenating one item from
    collection A with one from B.'''
    return {a + b for a in A for b in B}

urn = cross('W', '12345678') | cross('B', '123456') | cross('R', '123456789')

# (a)
print('a)')
U3 = list(itertools.combinations(urn, 3))
length_U3 = len(U3)
print("this is U3: ", U3)
print("this is the length of U3: ", length_U3)

# (b)
# Enumerate all possible cases of three balls of different colors
print('b)')
U3_diff_colors = list(itertools.permutations(urn, 3))
length_U3_diff_colors = len(U3_diff_colors)
print("this is U3_diff_colors: ", U3_diff_colors)
print("this is the length of U3_diff_colors: ", length_U3_diff_colors)

# (c)
# Enumerate all possible cases of the first ball being white and the second ball red.
print('c)')
first_white_second_red = [combo for combo in U3 if combo[0][0] == 'W' and combo[1][0] == 'R']
length_first_white_second_red = len(first_white_second_red)
print("this is first_white_second_red: ", first_white_second_red)
print("this is the length of first_white_second_red: ", length_first_white_second_red)
