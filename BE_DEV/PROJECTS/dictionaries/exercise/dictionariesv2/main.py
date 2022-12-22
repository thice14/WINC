# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line

# 1. Create Passport

def create_passport(name, date_of_birth, place_of_birth, height, nationality):

    passport = {
        "name": str(name),
        "date_of_birth": str(date_of_birth),
        "place_of_birth": str(place_of_birth),
        "height": float(height),
        "nationality": str(nationality)
    }
    
    return passport

# 2. Add Stamp

thijs = create_passport('Thijs Smeets', '1988-06-25', 'Rotterdam', 1.88, 'Netherlands')

def add_stamp(passport, nation):
    
    if nation == passport['nationality']:
        return passport
    elif 'stamps' in passport:    
        if nation not in passport['stamps']:
            passport['stamps']+=[nation]
    else:
        passport['stamps']=[nation]
    return passport

add_stamp(thijs, 'Chile')
add_stamp(thijs, 'Brazil')
add_stamp(thijs, 'Argentina')
add_stamp(thijs, 'Netherlands')


# 3. Add Biometric Data

# OWN SOLUTION, GOOD OUTPUT, NOT PASSING WINCPY CHECK

def add_biometric_data(passport, biometric_type, biometric_value, date_bio_added):

    if 'biometric' not in passport:
        passport['biometric'] = {biometric_type:{'date':date_bio_added, 'value':biometric_value}}
        return passport
    elif 'biometric' in passport:
        passport['biometric'][biometric_type] = {'date':date_bio_added, 'value':biometric_value}
        return passport

# OFFICIAL SOLUTION, PASSING WINCPY CHECK, BELOW

def add_biometric_data_official(passport, biometric_data_type, value, date):
    if not "biometric" in passport:
        passport["biometric"] = {}
    biometric_data = {"date": date, "value": value}
    passport["biometric"][biometric_data_type] = biometric_data
    return passport

if __name__ == "__main__":
    # add_biometric_data(thijs, 'eye_color_left', 'green', '2022-10-03')
    # add_biometric_data(thijs, 'eye_color_right', 'green', '2022-10-03')
    # add_biometric_data(thijs, 'eye_color_left', 'blue', '2022-10-04')
    # print(thijs)
   
    # Part 3: Add biometric data
    omari = create_passport("Omari Muchumba", "1995-07-16", "Kampala", 184.31, "Uganda")
    omari = add_biometric_data(omari, "eye_color_left", "blue", "2020-05-05")
    omari = add_biometric_data(omari, "eye_color_right", "blue", "2020-05-05")
    print(omari)

    # Omari gets a new left eye because of an accident
    omari = add_biometric_data(omari, "eye_color_left", "brown", "2022-01-10")
    print(omari)

    # Add fingerprints too: just another value, but this is also a dict.
    fingerprint_data = {
        "left_pinky": "2378945",
        "left_ring": "2349081",
        "left_middle": "132890",
        "left_index": "9823234",
        "left_thumb": "0924131",
        "right_thumb": "6234923",
        "right_index": "13249734",
        "right_middle": "34023784",
        "right_ring": "12332538",
        "right_pinky": "32458970",
    }
    omari = add_biometric_data(omari, "finger_prints", fingerprint_data, "2022-01-12")
    print(omari)

    # Add the amount of testicals
    omari = add_biometric_data(omari, "testicals", 2, "2022-10-03")
    print(omari)