#2A
"""golden_globe_winners = ['Jaws', 'Star Wars: Episode IV - A New Hope', 
                        'E.T. the Extra-Terrestrial', 'Memoirs of a Geisha']

golden_globe_winners_low = [x.lower() for x in golden_globe_winners]
golden_globe_winners_up = [x.upper() for x in golden_globe_winners]

def won_golden_globe(x):
    if (x) in golden_globe_winners:
        return True
    elif (x) in golden_globe_winners_low:
        return True
    elif (x) in golden_globe_winners_up:
        return True
    else:
        return False"""

# 3A
"""toto_albums = ["Fahrenheit", "The Seventh One", "Toto 10", "Falling in Between",
                "Toto 14", "Old is New"]

def remove_toto_albums(mixed_list):
    mixed_list = []

    if "Fahrenheit" in str(mixed_list):
        return str(mixed_list.remove("Fahrenheit"))
    elif "The Seventh One" in str(mixed_list):
        return str(mixed_list.remove("The Seventh One"))
    elif "Toto 10" in str(mixed_list):
        return str(mixed_list.remove("Toto 10"))
    elif "Falling in Between" in str(mixed_list):
        return str(mixed_list.remove("Falling in Between"))
    elif "Toto 14" in str(mixed_list):
        return str(mixed_list.remove("Toto 14"))
    elif "Old is New" in str(mixed_list):
        return str(mixed_list.remove("Old is New"))
    else:
        return str(mixed_list)
"""


# 3B


"""def remove_toto_albums(input_list):
    toto_albums = ["Fahrenheit", "The Seventh One", "Toto 10", "Falling in Between", "Toto 14", "Old is New"]

    empty_list = []

    for input in input_list:
        if input in toto_albums:
            input_list.remove(input)
            if input_list == empty_list: 
                return empty_list
    
    
                
    print(input_list)
    return input_list"""

# 3C

"""senior_compositions = ("Star Wars (Main Title)", "Theme from Close Encounters of the Third Kind", "The Imperial March", "Ewok Celebration", "Duel of the Fates", "The Five Sacred Trees", "Horn Concerto", "Liberty Fanfare", "For New York""American Journey", "Soundings", "Air and Simple Gifts")


def remove_toto_albums(mixed_list):
   if any(toto_albums) in mixed_list:
    return remove(toto_albums) from mixed_list 



print(remove_toto_albums("Old is New"))"""

# mixed_list = ['Fahrenheit', 'The Seventh One', 'Toto 10', 'Falling in Between', 'Toto 14', 'Old is New', "Star Wars (Main Title)", "Theme from Close Encounters of the Third Kind", "The Imperial March", "Ewok Celebration", "Duel of the Fates", "The Five Sacred Trees", "Horn Concerto", "Liberty Fanfare", "For New York""American Journey", "Soundings", "Air and Simple Gifts"]


question = 'How many roads must one walk down?'
for c in question:
    print(len(c))

"""example_list = ["Rob", "Thijs", "Edgar", "Bo"]
print(len(example_list))

def name_length(some_list):
    for name in range(some_list):
        if (len(name)) == ):
            return (name)
        else:
            return ("No name found")

print(name_length(example_list))"""

vowels = ['a', 'e', 'i', 'o', 'u']

example_list = ["Rob", "Thijs", "Edgar", "Bo"]

print(vowels.count(example_list))



