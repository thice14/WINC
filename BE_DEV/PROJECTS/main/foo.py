

# (1) Python takes note of this function
def main():
    # (5) At this point greet() is known and we can run it.
    print(greet('Bob'))

# (2) Then this one
def greet(name):
    return f'Hi, {name}!'

# (3) Now this statement is read
if __name__ == '__main__':
    # (4) main is run
    main()

"""def main():
    print('Do things here.')
    # ...
    print('End of the program.')

if __name__ == '__main__':
    main()
    """