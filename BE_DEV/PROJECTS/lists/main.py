bob = 'Bob'
shaun = 'Shaun'
preeti = 'Preeti'
jeff = 'Jeff'

# The list above can be written better, more dynamic and flexible. 

names = ['Bob', 'Shaun', 'Preeti', 'Jeff']

# A list is an object just like any other, like str, int and float. 
# They can hold a mix of objects, even other lists:

example_list = ['Bob', 3.14, 42]
example_list_of_lists = [['Bob', 3.14, 42], ['Preeti', 3.14, 42]]

# Indexing and slicing in lists

example_list = ['zeroth', 'first', 'second', 'third']
# Get the zeroth item.
print(example_list[0])
# Get the second item.
print(example_list[2])
# Get a slice of the list
print(example_list[0::2]) # This is slicing with the value in the middle kept out, meaning until the end of the list. I
print(example_list[0:3:2]) # This is the same thing, but with the index number of the final value in the list mentioned, though it is not necessary. Leaving it blank, as done above, does the same. Plus you do not have to count them ;-) 


# Mutability

example_string = 'Gi!'
# The next line results in an error
# example_string[0] = 'H'

# But this works fine
example_list = ['zeroth', 1, 2, 3]
example_list[0] = 0
print(example_list)
# Output: [0, 1, 2, 3]

# Comparison and Order

example_list_a = [1, 2, 3]
example_list_b = [3, 2, 1]
print(example_list_a == example_list_b) # Same value, but different order, so for Python they are NOT! the same, hence [False]

# Casting

example_list = ['this', 'is', 'fun']
print(str(example_list))
print(list(str(example_list)))
str(list(str(example_list)))
list(str(list(str(example_list))))
str(list(str(list(str(example_list))))) # etc.

# Common Operations with LISTS:

# Computing length of a list with [len]
# Finding the minimum or maximum in a list with [min] or [max]
# Concatenating (+) two or more lists with operator [+]
# Checking if something is in a list with [in]

example_list = [42.0, 3.50, 3.14, 42.0]
len(example_list)
# 4
min(example_list)
# 3.14
max(example_list)
# 42.0
example_list + ['another one']
# [42.0, 3.5, 3.14, 42.0, 'another one']
42.0 in example_list
# True
