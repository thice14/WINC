# TUPLES

# Tuples are much like lists, but immutable. Unlike lists, they are defined using parentheses (( )). 
# They are used when you know for sure that the tuple never needs to be modified. Here's an example:

# Creating a tuple
alice = ('Alice', 5)

# Tuples can contain any number of elements
bob = ('Bob', 3, 9)

# A list of tuples
persons = [alice, bob]
print(persons)

# Just like lists, in tuples you can execute indexing and slicing:

t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
print(t) # ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
print(t[0]) # 'foo'
print(t[-1]) # 'corge'
print(t[1::2]) # ('bar', 'qux', 'corge')
print(t[::-1]) # ('corge', 'quux', 'qux', 'baz', 'bar', 'foo')

# Note: Even though tuples are defined using parentheses, 
# you still index and slice tuples using square brackets, just as for strings and lists.

# Just like lists, tuples are:
# ordered, 
# contain arbitrary objects, 
# can be indexed and sliced, 
# can be nested.
# !But! they can’t be modified:

"""
>>> t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
>>> t[2] = 'Bark!'
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    t[2] = 'Bark!'
TypeError: 'tuple' object does not support item assignment
"""

"""
Why use a tuple instead of a list?

1:
Program execution is faster when manipulating a tuple than it is for the equivalent list. 
(This is probably not going to be noticeable when the list or tuple is small.)

2:
Sometimes you don't want data to be modified. If the values in the collection are meant to remain constant for the life of the program, 
using a tuple instead of a list guards against accidental modification.

3:
There is another Python data type that you will encounter shortly called a dictionary, 
which requires as one of its components a value that is of an immutable type. 
A tuple can be used for this purpose, whereas a list can't be.

"""

t = ()
print(type(t)) # <class 'tuple'>

t = (1, 2)
print(type(t))# <class 'tuple'>

t = (1, 2, 3, 4, 5)
print(type(t)) # <class 'tuple'>

t = (2)
print(type(t)) # Since parentheses are also used to define operator precedence in expressions, Python evaluates the expression (2) as simply the integer 2 and creates an int object.

t = (2,)
print(type(t)) # To tell Python that you really want to define a singleton tuple, include a trailing comma (,) just before the closing parenthesis
print(t[0]) # 2
print(t[-1]) # 2
print(t)

# Tuple Assignment, Packing, and Unpacking

# Packing
t = ('foo', 'bar', 'baz', 'qux')
t[0] # 'foo'
t[-1] # 'qux'

# Unpacking
(s1, s2, s3, s4) = t

s1 # s1 is now connected to t[0] -> 'foo'
s2 # 'bar'
s3 # 'baz'
s4 # 'qux'

# When unpacking, the number of variables on the left must match the number of values in the tuple:

"""
>>> (s1, s2, s3) = t
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    (s1, s2, s3) = t
ValueError: too many values to unpack (expected 3)

>>> (s1, s2, s3, s4, s5) = t
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    (s1, s2, s3, s4, s5) = t
ValueError: not enough values to unpack (expected 5, got 4)
"""

# Packing and unpacking can be combined into one statement to make a compound assignment:

(s1, s2, s3, s4) = ('foo', 'bar', 'baz', 'qux')
s1 # 'foo'
s2 # 'bar'
s3 # 'baz'
s4 # 'qux'

# Again, the number of elements in the tuple on the left of the assignment must equal the number on the right:

"""
>>> (s1, s2, s3, s4, s5) = ('foo', 'bar', 'baz', 'qux')
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    (s1, s2, s3, s4, s5) = ('foo', 'bar', 'baz', 'qux')
ValueError: not enough values to unpack (expected 5, got 4)
"""

# In assignments like this and a small handful of other situations, 
# Python allows the parentheses that are usually used for denoting a tuple to be left out:

t = 1, 2, 3
(t) # (1, 2, 3)

x1, x2, x3 = t
x1, x2, x3 # (1, 2, 3)

x1, x2, x3 = 4, 5, 6
x1, x2, x3 # (4, 5, 6)

t = 2,
t # (2,)

# Frequently when programming, you have two variables whose values you need to swap. 
# In most programming languages, it is necessary to store one of the values in a temporary variable while the swap occurs like this:

a = 'foo'
b = 'bar'
a, b # ('foo', 'bar')

# We need to define a temp variable to accomplish the swap.
temp = a
a = b
b = temp
a, b # ('bar', 'foo')

# In Python, the swap can be done with a single tuple assignment:

a = 'foo'
b = 'bar'
a, b ('foo', 'bar')

# Magic time!
a, b = b, a
a, b # ('bar', 'foo')

