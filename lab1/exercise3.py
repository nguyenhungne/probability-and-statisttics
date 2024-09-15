import itertools

math_books = ['Math1', 'Math2', 'Math3', 'Math4']
physics_books = ['Phys1', 'Phys2', 'Phys3']
chemistry_books = ['Chem1', 'Chem2']
language_books = ['Lang1']

subjects = [math_books, physics_books, chemistry_books, language_books]

subject_arrangements = list(itertools.permutations(subjects))

all_arrangements = []

for subject_arrangement in subject_arrangements:
    arranged_books = []
    for books in subject_arrangement:
        arranged_books.append(list(itertools.permutations(books)))
    
    for books_in_subject in itertools.product(*arranged_books):
        full_arrangement = sum(books_in_subject, ())
        all_arrangements.append(full_arrangement)

num_arrangements = len(all_arrangements)

print(num_arrangements)
print(all_arrangements)
