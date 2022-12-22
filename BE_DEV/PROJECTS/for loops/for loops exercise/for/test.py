# OPPOSITE (CONSONANTS) WORKING SNIPPET
"""def consonants_per_country(country_list):
    country_list = get_countries()
    country_list_lower = [x.lower() for x in country_list]
    vowels = ['a', 'e', 'i', 'o', 'u']

    for country in range(len(country_list_lower)):
        for char in vowels:
            country_list_lower[country] = country_list_lower[country].replace(char,"")
    print(country_list_lower)

consonants_per_country(country_list)"""
# END OF OPPOSITE (CONSONANTS) WORKING SNIPPET

# WORKING SNIPPET
"""def vowels_per_country(country_list):
    country_list = get_countries()
    country_list_lower = [x.lower() for x in country_list]
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', ' ', '-', '.', ',', '(', ')']

    for country in range(len(country_list_lower)):
        for char in consonants:
            country_list_lower[country] = country_list_lower[country].replace(char,"")
    print(country_list_lower)

print(country_list)
vowels_per_country(country_list)
"""
# END OF WORKING SNIPPET

# BEST SNIPPET SO FAR
"""def get_max_vowels_per_country(country_list):
    country_list_lower = [x.lower() for x in country_list]
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', ' ', '-', '.', ',', '(', ')']
    most_vowels = []

    for country in range(len(country_list_lower)):
        for char in consonants:
            country_list_lower[country] = country_list_lower[country].replace(char,"")
    return max(country_list_lower, key=len)
                 
print(get_max_vowels_per_country(country_list))"""
# END OF BEST SNIPPET SO FAR

# WORKING SNIPPET MAX FUNCTION ALL CHARACTERS
"""def most_characters_country(country_list):
    return max(country_list, key=len)
                 

print(most_characters_country(country_list))"""
# END WORKING SNIPPET MAX FUNCTION ALL CHARACTERS

# VERY BEST WORKING SNIPPET TO FIND COUNTRY WITH MOST VOWELS
"""def most_vowels(country_list):
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r',
    's', 't', 'v', 'w', 'x', 'y', 'z', ' ', '-', '.', ',', '(', ')', 'B', 'C', 'D', 'F',
    'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    most_vowels_ranked = []

    for country in range(len(country_list)):
        for char in consonants:
            country_list[country] = country_list[country].replace(char,"")
        most_vowels_ranked.append(max(country_list, key=len))
        break
    return most_vowels_ranked
                 
print(most_vowels(country_list))"""
# END OF VERY BEST WORKING SNIPPET TO FIND COUNTRY WITH MOST VOWELS

"""               if j not in alphabet_set_list:
                    alphabet_set_list.append(j)
    return alphabet_set_list
    
        countries_lower = [x.lower() for x in country_list]
    
    """

# CLOSEST RESULT OWN PRODUCTION SO FAR
"""
def most_vowels(country_list):
    
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r',
    's', 't', 'v', 'w', 'x', 'y', 'z', ' ', '-', '.', ',', '(', ')', 'B', 'C', 'D', 'F',
    'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

    for country in range(len(country_list)):
        for char in consonants:
            country_list[country] = country_list[country].replace(char,"")
    return sorted(country_list, key=len, reverse=True)[0:3]
       
print(most_vowels(country_list))"""
# END 

# TEST SNIPPET TO MATCH STRING OF VOWEL WITH ORIGINAL NAME
"""lst1 = ['oueoiaaeouaiIa', 'ioeiaeeaeaeo', 'UieaeioOuiIa']
lst2 = ['Micronesia, Federated States of', 'The Democratic Republic of Congo', 'Saint Vincent and the Grenadines', 'Heard Island and McDonald Islands', 'United States Minor Outlying Islands', 'South Georgia and the South Sandwich Islands']
lst3 = []

for i in lst1:
    for j in lst2:
        if i in j:
            lst3.append(j)
    
print(lst3)"""
# END   


some_countries = ['Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica']

def alphabet_set(L):

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z']
    L2 = []

    for j in L:
        for i in alphabet:
            if i in j.lower():
                alphabet.remove(i)
            continue
    return alphabet

print(alphabet_set(some_countries))

import string

L = ['Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'The Democratic Republic of Congo', 'Cook Islands', 'Costa Rica', 'Ivory Coast', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt', 'England', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands', 'Faroe Islands', 'Fiji Islands', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Isle of Man', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libyan Arab Jamahiriya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'North Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova', 'Monaco', 'Mongolia', 'Montserrat', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'Netherlands Antilles', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'North Korea', 'Northern Ireland', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Reunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Helena', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Scotland', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'South Korea', 'South Sudan', 'Spain', 'SriLanka', 'Sudan', 'Suriname', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wales', 'Wallis and Futuna', 'Western Sahara', 'Yemen', 'Yugoslavia', 'Zambia', 'Zimbabwe']

def alphabet_set(countries):

    alphabet_string = string.ascii_lowercase

    alphabet_list = list(alphabet_string)

    alphabet_set_list = []

    for j in countries:
        for k in j:
            for i in alphabet_list:
                if i == k.lower():
                    alphabet_list.remove(i)
                    if j not in alphabet_set_list:
                        alphabet_set_list.append(j)
                continue
            continue
        continue
    return alphabet_set_list

print(alphabet_set(L))

def alphabet_set2(countries):

    alphabet_list = list(string.ascii_lowercase)

    alphabet_set_list = []

    for c in countries:
        for letter in c:
            for i in alphabet_list:
                if i == letter.lower():
                    alphabet_list.remove(i)
                    if c not in alphabet_set_list:
                        alphabet_set_list.append(c)
                continue
            continue
        continue
    return alphabet_set_list

print(alphabet_set2(L))



"""def alphabet_set(countries):

    alphabet_string = string.ascii_lowercase

    alphabet_list = list(alphabet_string)

    alphabet_set_list = []

    for j in countries:
        for i in alphabet_list:
            if i in j.lower():
                alphabet_list.remove(i)
                if j not in alphabet_set_list:
                    alphabet_set_list.append(j)
            continue
        continue
    return alphabet_set_list"""