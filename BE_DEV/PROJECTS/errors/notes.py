# ERRORS

# Traceback

# Whenever Python runs into an error, it prints this line first:
# [ Traceback (most recent call last): ]

def multiply_a(a, b):
    return a * b

def multiply_b(a, b):
    return multiply_a(a, b)

def multiply_c(a, b):
    return multiply_b(a, b)

print(multiply_c(3, 5))

# print(multiply_c('incoming', 'error')) -> Returns an error of course, since two strings can not by multiplied by each other, hence TypeError

# Error Types

# TypeError: when you made a mismatch between types of variables and operators (see example above: multiplying strings -> multiply operator can not be used on strings)
# SyntaxError: when you made a typo or indentation mistake.
# ImportError: when you're trying to import a module that does not exist.
# IndexError: when you try to access a spot in a list that does not exist.
# ValueError: when you try to call a function with arguments of the wrong type.

# Try.. Except:

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("You tried to divide by zero. That's not possible in math.")
    return None

print(divide(4, 0))

"""while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")"""

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")