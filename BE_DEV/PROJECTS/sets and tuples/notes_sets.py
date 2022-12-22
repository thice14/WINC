# 1. SETS

list_a = [1,2,3]
list_b = [3,2,1]
print(list_a == list_b)
print(set(list_a) == set(list_b))

set_a = set([1,2,3])
set_a.add(3)
print(set_a) # '3' is not actually added, since it was already in the set. Values in sets can only appear once.

set_a = set([1,2,3])
set_a.add(4)
print(set_a) #'4' is added, because it was not in the set yet.

set_a = set([1,2,3])
set_b = set([3,4,5])

# Union
# You can read this as 'set_a or set_b', so: 'any element that is in set a or set b'. I.e. collets all unique values from both sets in one set.
print(set_a | set_b)
print(len(set_a | set_b)) # Returns the amount of unique values in the two sets combined. Only possible between sets.
print(set_a.union(set_b))
set_c = set([3,6,9])
print(set_a | set_b | set_c)
print(set_a.union(set_b, [3,6,9]))
# print(set_a | [3,6,9]) -> NOT POSSIBLE! Operator only works between sets, not between a set and other iterables. Use .union() instead!


# Difference
print(set_a - set_b) # Returns set_a minus any corresponding value found in set_b
print(set_b - set_a) # Returns set_b minus any corresponding value found in set_a
print(set_a.difference(set_b)) 

# Intersection
print(set_a.intersection(set_b)) # Returns every overlapping value from both sets, or between a set and another iterable.
print(set_a & set_b) # Works just like method .intersection(), but only works between sets, not with other iterables.

# Checking if a set is a subset of another.
# In other words: if the other set includes all of its own elements.
small = set([2,3])
big = set([1,2,3,4])
intermediate = set([3,4,5])
print(small.issubset(big)) # Returns a boolean: True or False
print(small <= big) # <= or < operator instead of .issubset() method. The < operator is a proper determination to determine subset. By <= operator every set returns true in comparison to itself.
print(small.issubset(intermediate)) # False
print(big < big) # False
print(big <= big) # True

# Checking if a set is a superset of another
# In other words: if the set it is compared to contains all elements of this set

print(big.issuperset(small)) # True
print(small.issuperset(big)) # False
print(big >= big) # True
print(big > big) # False
print(big > small) # True

# Symmetric Difference
a = {1, 2, 3, 4, 5}
b = {10, 2, 3, 4, 50}
c = {1, 50, 100}

print(a - b - c) # Since a-b is executed first, and results in {5}, the following equation {5} - c does not impact {5} anymore.
print(c - b - a)
print(a.symmetric_difference(b)) # Currently .symmetric_difference() method only allows 1 set to be compared with. 
print(a ^ b)
print(a ^ b ^ c) # The ^ operator allows a symmetric difference equation with multiple sets

# Disjoint

print(a.isdisjoint(b)) # Determines whether or not these two sets have any elements in common. True = nothing in common, False = elements in common
d = {6, 7, 8, 9}
print(a.isdisjoint(d))
print(a.isdisjoint(c - {1})) # Comparing set A with set C minus value {1}. Curly braces are crucial!

# Modifying a Set

# Ways to append two sets. Operator |= and Method .update(). Have to code first, followed by print statement. Do not return/work directly in a print statemtent.
a|= b
print(a)

c.update(d)
print(c)

# Modify a set by intersection.
# x1.intersection_update(x2[, x3 ...])
# x1 &= x2 [& x3 ...]

# x1.intersection_update(x2) and x1 &= x2 update x1, retaining only elements found in both x1 and x2:

x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}

x1 &= x2
print(x1) # {'foo', 'baz'}


x1.intersection_update(['baz', 'qux'])
print(x1) # {'baz'}

# Modify a set by difference.
# Method: x1.difference_update(x2[, x3 ...])
# Operator: x1 -= x2 [| x3 ...]

# x1.difference_update(x2) and x1 -= x2 update x1, removing elements found in x2:

x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}

x1 -= x2
print(x1) # {'bar'}

x1.difference_update(['foo', 'bar', 'qux'])
print(x1) # set()

# Modify a set by symmetric difference.
# Method: x1.symmetric_difference_update(x2)
# Operator: x1 ^= x2

# x1.symmetric_difference_update(x2) and x1 ^= x2 update x1, retaining elements found in either x1 or x2, but not both:

x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}

x1 ^= x2
print(x1) # {'bar', 'qux'}

x1.symmetric_difference_update(['qux', 'corge'])
print(x1) # {'bar', 'corge'}

# Other Methods For Modifying Sets

# x.add(<elem>)
x = {'foo', 'bar', 'baz'}
x.add('qux') # {'baz', 'qux', 'foo', 'bar'} -> random order!
print(x)

# x.remove(<elem>)

x = {'foo', 'bar', 'baz'}
x.remove('baz') # {'foo', 'bar'} | IF <elem> is not found in the set, it returns a KeyError!
print(x)

# x.discard(<elem>)
x = {'foo', 'bar', 'baz'}
x.discard('qux') # {'foo', 'bar', 'baz'} | Just returns the original set. In contrast to .remove(), the .discard() method continues to work and does NOT return an error
print(x)
x.discard('baz') # {'foo', 'bar'}
print(x)

# x.pop()
# Removes a random element from a set.
x = {'foo', 'bar', 'baz'}
x.pop()
print(x) # Return two random elements out of the original 3
x.pop()
print(x) # Returns one random element out of the previously deducted two elements
x.pop()
print(x) # Returns an empty set -> set() 

# x.clear()
# Clears a set.

x = {'foo', 'bar', 'baz'}
x.clear()
print(x) # All elements of the set are removed. Returns an empty set: set()

# FROZEN SETS - frozenset([])

# Python provides another built-in type called a frozenset, which is in all respects exactly like a set, except that a frozenset is immutable. 

# You can perform non-modifying operations on a frozenset:
x = frozenset(['foo', 'bar', 'baz'])
print(x) # frozenset({'foo', 'baz', 'bar'})

print(len(x)) # 3

print(x & {'baz', 'qux', 'quux'}) # frozenset({'baz'})

# Methods that attempt to modify a frozenset fail:
"""
>>> x = frozenset(['foo', 'bar', 'baz'])

>>> x.add('qux')
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    x.add('qux')
AttributeError: 'frozenset' object has no attribute 'add'

>>> x.pop()
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    x.pop()
AttributeError: 'frozenset' object has no attribute 'pop'

>>> x.clear()
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    x.clear()
AttributeError: 'frozenset' object has no attribute 'clear'

>>> x
frozenset({'foo', 'bar', 'baz'})"""

# Frozensets and Augmented Assignment

# Although a frozenset is immutable, it can still be the target of an augmented assignment operator.

f = frozenset(['foo', 'bar', 'baz'])
s = {'baz', 'qux', 'quux'}

f &= s
print(f) # frozenset({'baz'})

# The statement f &= s is effectively equivalent to f = f & s. 
# It isn’t modifying the original f. It is reassigning f to a new object, and the object f originally referenced is gone.

# Frozensets are useful in situations where you want to use a set, but you need an immutable object. 
# For example, you can’t define a set whose elements are also sets, because set elements must be immutable:

""">>> x1 = set(['foo'])
>>> x2 = set(['bar'])
>>> x3 = set(['baz'])
>>> x = {x1, x2, x3}
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    x = {x1, x2, x3}
TypeError: unhashable type: 'set'
"""

# If you really feel compelled to define a set of sets (hey, it could happen), 
# you can do it if the elements are frozensets, because they are immutable:

x1 = frozenset(['foo'])
x2 = frozenset(['bar'])
x3 = frozenset(['baz'])
x = {x1, x2, x3}
print(x) # {frozenset({'bar'}), frozenset({'baz'}), frozenset({'foo'})}




