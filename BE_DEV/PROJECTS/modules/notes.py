# MODULES

# A lot of programming challenges are common to many programs, for example:
# - Fetching something from a web server;
# - Searching for a piece of text in a string;
# - Reading a file from the local file system.

import time # Modules can be imported with the [import] statement

print(time.asctime())

# REAL PYTHON: MODULES
# https://realpython.com/python-modules-packages/

# There are several advantages to modularizing code in a large application:
# - Simplicity
# - Maintainability
# - Reusability
# - Scoping 

# There are actually three different ways to define a module in Python:

# 1: A module can be written in Python itself.
# 2: A module can be written in C and loaded dynamically at run-time, like the re (regular expression) module.
# 3: A built-in module is intrinsically contained in the interpreter, like the itertools module.

# !!! A module’s contents are accessed the same way in all three cases: with the import statement. !!!

# A module is a file that contains legitimate Python code and then give the file a name with a .py extension. That’s it! No special syntax or voodoo is necessary.

import mod
print(mod.s)
print(mod.a)
print(mod.foo(['quux', 'corge', 'grault']))
x = mod.Foo()
print(x)

import sys

sys.path.append(r'/Users/thijsbreukel/Documents/WINC/BE DEV')
# print(sys.path)

# print(mod.__file__)

# As seen above, for objects from [mod] to be accessed in the local context,
# names of objects defined in the module must be prefixed by mod. -> mod.s & mod.Foo()

# Another option is through a for loop, from <module_name> import <name(s)>:

from mod import s, foo
print(s)
print(foo('quux'))

from mod import Foo
x = Foo()
print(x)

from mod import * # This will import all objects from module [mod] to this local context

"""
!!!
This [from mod import *] isn't necessarily recommended in large-scale production code. 
It's a bit dangerous because you are entering names into the local symbol table en masse. 
Unless you know them all well and can be confident there won't be a conflict, 
you have a decent chance of overwriting an existing name inadvertently. 
However, this syntax is quite handy when you are just mucking around with the interactive interpreter, 
for testing or discovery purposes, because it quickly gives you access to everything a module has to offer without a lot of typing.
!!!
"""

# It is possible to import individual objects but enter them into the local symbol table with alternate names:

# from <module_name> import <name> as <alt_name>

s = 'foo'
a = ['foo', 'bar', 'baz']

from mod import s as string, a as alist

print(s)
print(string)
print(a)
print(alist)

# You can also import an entire module under an alternate name:

# import <module_name> as <alt_name>

import mod as my_module
print(my_module.a)
print(my_module.foo('qux'))

# Module contents can be imported from within a function definition. 
# In that case, the import does not occur until the function is called:

def bar():
     from mod import foo
     foo('corge')
    
print(bar())

# !!! However, Python 3 does not allow the indiscriminate import * syntax from within a function !!! 
# -> SyntaxError: import * only allowed at module level

# Lastly, a try statement with an except ImportError clause can be used to guard against unsuccessful import attempts:
try:
    # Non-existent module
    import baz
except ImportError:
    print('Module not found')

try:
     # Existing module, but non-existent object
    from mod import baz
except ImportError:
    print('Object not found in module')

# The dir() Function

print(dir()) # The built-in function dir() returns a list of defined names in a namespace. 
# Without arguments, it produces an alphabetically sorted list of names in the current local symbol table

print(dir(mod)) # When given an argument that is the name of a module, dir() lists the names defined in the module

# Executing a Module as a Script

# Any .py file that contains a module is essentially also a Python script, and there isn’t any reason it can’t be executed like one.

from fact import fact
print(fact(6))
