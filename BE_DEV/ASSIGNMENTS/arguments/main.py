# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def main():
    print(greet('Bob'))
    print(greet('Bob', "What's up, <name>!"))
    print(force(0.1))
    print(force(0.1, 'moon'))
    print(round(pull(1500, 800, 3),10))

# PART 1: GREET TEMPLATE

def greet(name, greeting='Hello, <name>!'):
    updated_greeting = greeting.replace("<name>", name)
    return updated_greeting


# PART 2: FORCE

def force(mass, body='earth'):

    bodies = {
        "sun": 274,
        "jupiter": 24.92,
        "neptune": 11.15,
        "saturn": 10.44,
        "earth": 9.798,
        "uranus": 8.87,
        "venus": 8.87,
        "mars": 3.71,
        "mercury": 3.7,
        "moon": 1.62,
        "pluto": 0.58
    }

    gravity = bodies[body]
    
    force = mass * round(gravity,1)

    return force


# PART 3: GRAVITY

def pull(mass1, mass2, distance):

    grav_constant = 6.674 * 10.00 ** -11

    force = grav_constant * mass1 * mass2 / distance ** 2

    return force


if __name__ == '__main__':
    main()
