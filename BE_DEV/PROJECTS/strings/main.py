example_one = 'I am a string'
example_two = "I am a string too"
example_three = """I too am a string.
I am, in fact, a multiline string"""

example_four = 'I\'m a string' # The backslash (\) is used as an Escape
example_five = "I'm a string too"
example_six = 'He said: "I\'m a string too"' 

print(example_one)
print(example_two)
print(example_three)
print(example_four)
print(example_five)
print(example_six)

example_seven = "It is between him \\ her" #To print "\" you need "\\" to circumvent the initial Escape backslashes are used for. The double backslash is the Escape to use a single backslash
print(example_seven)

# Example of the use of \n
example_eight = """A multiline string can be put\non multiple lines as follows"""
print(example_eight)

# Example of the use of \n and \t
example_nine = """A multiline string can be put\n\ton multiple lines like this too and be tabbed"""
print(example_nine)
