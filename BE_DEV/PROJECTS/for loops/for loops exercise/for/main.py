from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """
# 1 SHORTEST_NAMES

country_list = get_countries()
# countries_lower = [x.lower() for x in country_list]

def shortest_names(country_list):
    
    shortest_names_list = []
    
    for country in country_list:
        if len(country) == len(min(country_list, key=len)):
            shortest_names_list.append(country)
    return shortest_names_list

# TEST SNIPPET TO GET THE 6 LONGEST NAMES FROM COUNTRY_LIST:
# print(sorted(country_list, key=len)[-6:])

# 2 MOST_VOWELS

# BELOW IS MOSTLY COPIED FROM SLACK

def most_vowels(countries):
    vowels = 'aeiouAEIOU'
    L = []
    for country in countries:
        count = 0
        for char in country:
            if char in vowels:
                count = count + 1
        L.append([country, count])
        L = sorted(L, key = lambda x: x[1], reverse=True)[:3]
    return [item[0] for item in L]

# 3 ALPHABET_SET

import string

def alphabet_set(countries):

    alphabet_list = list(string.ascii_lowercase)

    alphabet_set_list = []

    for c in countries:
        for letter in c:
            for char in alphabet_list:
                if char == letter.lower():
                    alphabet_list.remove(char)
                    if c not in alphabet_set_list:
                        alphabet_set_list.append(c)
                continue
            continue
        continue
    return alphabet_set_list

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """

print(shortest_names(country_list))
print(most_vowels(country_list))
print(alphabet_set(country_list))
