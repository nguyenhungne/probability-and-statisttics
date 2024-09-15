import itertools

A = {1, 2, 3, 4, 5}

num_3_digit = list(itertools.permutations(A, 3))

num_3_digit = [int(''.join(map(str, num))) for num in num_3_digit]

num_length = len(num_3_digit)

num_3_digit, num_length
