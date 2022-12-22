# WHILE LOOPS

# Example of an Infite Loop:

# while True:
#   print('Woop woop, an infinite loop.')

# !!! Hit control + c on your keyboard to unstuck from this :-) !!!

i = 10
while i > 0:
    print(i)
    i -= 1

a = ['foo', 'bar', 'baz']
while a:
    print(a.pop())

b = ['foo', 'bar', 'baz', 'qux']
s = 'corge'

j = 0
while j < len(b):
    if b[j] == s:
         # Processing for item found
         break
    j += 1
else:
     # Processing for item not found
     print(s, 'not found in list.')
