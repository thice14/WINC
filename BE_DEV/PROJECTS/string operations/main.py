print('Hello, ' + 'world')
print('Jump! ' * 5)

# Examples of the use of the membership operate [in]. Boolean (True/False) finding
print('Samuel' in 'We went out for dinner with Anne, Samuel and Bob') 
print('Shane' in 'We went out for dinner with Anne, Samuel and Bob')

print(str(5) in 'We were lucky that they had a table for 5') # This does work

# print(5 in 'We were lucky that they had a table for 5') -> This does NOT work

# Examples of the use of the [==] operator. Boolean results. Capital sensitive!
print('Me' == 'Me')
print('You' == 'Me')
print('Me' == 'me')

# Examples of indexing into the string. Both clockwise and counter-clockwise work!
letter_grades = 'ABCDF'
print(letter_grades[0])
print(letter_grades[3])
print(letter_grades[-1])
print(letter_grades[-2])
print(letter_grades[-2] == letter_grades[3])

# Examples of slicing.

waltz = 'onetwothree'
print(waltz[0:3])
print(waltz[:3]) # You do not need to specify the 0 if we start at the beginning
print(waltz[3:6])
print(waltz[6:11])
print(waltz[6:]) # Same goes for the end, you can leave it empty
print(waltz[0:11:2]) # You can specify a step size if we don't want a continuous slice. 
print(waltz[0:11:3])
print(waltz[0:11:4])
print(waltz[0:11:6])

""" In waltz[start:stop:step], the first number is the starting point, the second the stop.
The last number indicates the step. First item printed is that at the start, 
followed by the next item that is the indicated amount of steps away,
continously until the end of the string is reached."""

sentence = 'The length of this string is:'
print(sentence, len(sentence))
print('Wait.. you just made it longer!')

answer = 42
qa = f'The answer is.. {answer}'
print(qa)

answer = 42
qa = 'The answer is ..{}'
print(qa.format(answer))
