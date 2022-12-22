# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

# 1

golden_globe_nominees = ["The Poseidon Adventure", "Cinderella Libery", "Tom Sayer", "Earthquake", "Jaws", 
                        "Close Encounters of the Third Kind", "Star Wars: Episode IV - A New Hope", "Superman",
                        "Star Wars: Episode V - The Empire Strikes Back", "E.T. the Extra-Terrestrial",
                        "If We Were in Love", "The River", "Empire of the Sun", "The Accidental Tourist",
                        "Born on the Fourth of July", "Schindler's List", "Moonlight", "Seven Years in Tibet",
                        "Saving Private Ryan", "Angela's Ashes", "A.I. Artificial Intelligence", "Memoirs of a Geisha",
                        "War Horse", "Lincoln", "The Book Thief", "The Post"]

def alphabetical_order(x):
    return sorted(x)

# 2

golden_globe_winners = ['Jaws', 'Star Wars: Episode IV - A New Hope', 'E.T. the Extra-Terrestrial', 'Memoirs of a Geisha']

def won_golden_globe(x):
  return x.lower() in str(golden_globe_winners).lower()

# 3

def remove_toto_albums(mixed_list):
    toto_albums = ["Fahrenheit", "The Seventh One", "Toto 10", "Falling in Between", "Toto 14", "Old Is New"]
    
    filtered_list = []
    
    for album in mixed_list:
        if album not in toto_albums:
                filtered_list.append(album)
    return filtered_list
            