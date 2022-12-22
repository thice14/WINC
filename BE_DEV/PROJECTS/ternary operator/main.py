
# In Python, you can use conditions in any expression. For example:
nice_weather = False
going_outside = True if nice_weather else False
print(going_outside)

# Not limited to booleans.
nice_weather_odds = .7
party_location = 'inside' if nice_weather_odds < .6 else 'in the yard'
print(party_location)

#  !!! DANGER !!!
# DO NOT OVERUSE IT 
# Constructs like these are very powerful, but with great power comes great responsibility.
# Even though this statement is valid Python code, it clearly went overboard with ternary operators:

party_location = 'inside' if 1 + 2 == 5 or 3 ** 3 == 9\
                  else 'yard' if bool(2//5) is True else\
                  False if True else 'restaurant'

