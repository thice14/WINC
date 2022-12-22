# FUNCTION ARGUMENTS

# Default Parameters

# Example: a function to get the weather report
"""
def weather_report(day):
    print(f'Here is the weather for {day}')
    # get the weather report from somewhere
    # ...
    return info

weather_report('today')
"""

# Example: It might be the case that we usually want the weather for today. 
# In this case we can define a default for the date parameter. 
# The day-parameter is now optional. It's not required when calling the function.

"""
def weather_report(day='today'):
    print(f'Here is the weather for {day}')
    # get the weather report from somewhere
    # ...
    return info

weather_report()
"""

# Example: If we then want tomorrows weather we can override the default by supplying the optional argument.

"""
weather_report('tomorrow') --> 'tomorrow' will overwrite the default argument (day='today')
"""

# Keyword Arguments

# Improve readability of your code in cases where you do a function call 
# from which it is not immediately clear what each argument means 
# by specifying the parameters as keyword arguments.


# Without keyword arguments.
"""
send_email('bob@example.com',
           'preeti@example.com',
           'eric@example.com',
           'Thanks for the cake!')
"""

# With keyword arguments. Much clearer.
"""
send_email(sender='bob@example.com',
           to='preeti@example.com',
           cc='eric@example.com',
           msg='Thanks for the birthday cake!')
"""

def f(qty, item, price):
    print(f'{qty} {item} cost ${price:.2f}')

# Without keyword arguments
f(6, 'bananas', 1.74) # 6 bananas cost $1.74

# With keyword arguments
f(qty=6, item='bananas', price=1.74) # 6 bananas cost $1.74

# Or mixed can works as well, as long you keep going with keyword arguments once you started!
f(6, 'bananas', price=1.74) # 6 bananas cost $1.74

# This does NOT work!
"""
f(6, item='bananas', 1.74) # SyntaxError: positional argument follows keyword argument
"""
