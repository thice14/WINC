def double(x):
    doubled_x = x * 2
    return doubled_x

four_doubled = double(4)
print(four_doubled)

print(double(5))
print(double(21))
print(double(1.2))
print(double('Hey! '))

def initials(name):
    first = name[0].upper()
    last = name[name.find(' ')+1].upper()
    return f'{first}. {last}.'

print(initials('Ex Ample'))
print(initials('Bob Cat'))
print(initials('Function Nice'))

def multiply(a, b):
    return a * b

print(multiply(2, 2))
print(multiply(9, 2.3))
print(multiply(29, 'Hey! '))

def func_with_multiple_args(arg_0, arg_1):
    print('I received the arguments:', arg_0, arg_1)
