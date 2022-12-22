# FOR LOOPS

names = ['Bob', 'Shaun', 'Preeti', 'Jeff']
for name in names:
    print(f'Hello, {name}!')

# Instead of:

names = ['Bob', 'Shaun', 'Preeti', 'Jeff']
print(f'Hello, {names[0]}!')
print(f'Hello, {names[1]}!')
print(f'Hello, {names[2]}!')
print(f'Hello, {names[3]}!')

# Iterables
question = 'How many roads must one walk down?'
for c in question:
    print(c)

# Range
for i in range(10):
    print(i)

print(list(range(10)))

for i in range(900,1000,5):
    print(i)

for i in range(900,800,-5):
    print(i)

# Break and Continue

print('We have a long road ahead.')
for i in range(100):
    print(i)
    if i == 10:
        break
    print('Almost there...')
print("That wasn't so bad after all.")

print('We have a long road ahead.')
for i in range(10):
    if i % 2 == 0:
        print(i)
        continue
    print('Almost there...')
print("That wasn't half bad.")


#Term	    Meaning
#Iteration	The process of looping through the objects or items in a collection
#Iterable	An object (or the adjective used to describe an object) that can be iterated over
#Iterator	The object that produces successive items or values from its associated iterable
#iter()	    The built-in function used to obtain an iterator from an iterable
