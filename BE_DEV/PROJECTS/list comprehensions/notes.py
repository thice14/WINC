example_names = ['Anna Ansville Adrighem', 'Bob Bobsville Breukel', 'Carla Carlsville Cmeets']

example_last_names = []
for name in example_names:
    example_last_names.append(name.split(' ')[-1]) # or [2]
print(example_last_names)

example_middle_names = []
for name in example_names:
    example_middle_names.append(name.split(' ')[1]) # or [-2]
print(example_middle_names)

example_first_names = []
for name in example_names:
    example_first_names.append(name.split(' ')[0]) # or [-3]
print(example_first_names)

# COMPREHENSION

example_names2 = ['Anna Ansville', 'Bob Bobsville', 'Carla Carlsville']
example_last_names2 = [n.split(' ')[-1] for n in example_names2]
print(example_last_names2)

# HOW TO CREATE LISTS IN PYTHON:

# https://realpython.com/list-comprehension-python/

# I: Using For Loops (& Append)

# 1. Instantiate an empty list.
# 2. Loop over an iterable or range of elements.
# 3. Append each element to the end of the list.

squares = []
for i in range(10):
    squares.append(i * i)
print(squares)

# II: Using map() Objects

# Example: Calculate the price after tax for a list of transactions:

transactions = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08
def get_price_with_tax(transaction):
    return round(transaction * (1 + TAX_RATE),2)
final_prices = map(get_price_with_tax, transactions)
print(list(final_prices))

# III: Using List Comprehensions

squares = [i * i for i in range(10)]
print(squares)


# HOW TO SUPERCHARGE LIST COMPREHENSIONS

# new_list = [expression for member in iterable]
# BETTER and CLEARER expressed:
# new_list = [expression for member in iterable (if conditional)]

sentence = 'the rocket came back from mars'
vowels = [i for i in sentence if i in 'aeiou']
print(vowels)

sentence = 'The rocket, who was named Ted, came back \
... from Mars because he missed his friends.'
def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels
consonants = [i for i in sentence if is_consonant(i)]
print(consonants)

original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 0 else 0 for i in original_prices]
print(prices)

