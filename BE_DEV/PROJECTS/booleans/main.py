# Naming Boolean variables
# Boolean values can only hold [True] or [False]
# Name the Boolean variable to something that says something which can be true or not. See examples below.

is_raining = True
sun_is_shining = False
team_a_wins = True
team_b_wins = False

# Try to avoid NEGATIVE names like [not_training]. 
# It makes reasoning about your code harder due to double negatives turning into positives.

# Boolean Context

"""if some_kind_of_value:
    print('The expression results in a truth value')"""

bool("") # False
bool("hi mom") # True

string_a = ''
string_b = 'hi mom'

if string_a:
    print('expression results in a truthy value') # Nothing is printed because an empty string is converted to False

if string_b:
    print('expression results in a truthy value') # The print line is executed because a non-empty string is converted to True

if string_a != "":
    print('string_a != ""') # Nothing is printed because string_a = "" , in other words the equation is [False], so no print is executed

if string_b != "":
    print('string_b != ""') # This expression is printed because string_b is not empty, hence equation string_b != "" is [True], thus printed.

    # Remember "!=" means "IS NOT"

print(10 < 9)
print(10 == 9)
print(10 > 9)

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print(bool("Hello"))
print(bool(15))

x = 'Hello'
y = 15

print(bool(x))
print(bool(y))

print(bool(" ")) 

"""Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones."""

# Examples of False Values

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# One last example of False Value: a [class] with a [__len__] function

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
