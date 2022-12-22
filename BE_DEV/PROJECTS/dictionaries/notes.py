student_ages = {
    'bob': 10,
    'sharon': 9,
    'eli': 10,
    'preeti': 11
}

print(student_ages['bob'])
print(student_ages['eli'])

product = {
    "name": "tofu",
    "price": 2,
    "producer": {
        "name": "Tofu Company Limited",
        "country_of_origin": "France"
    },
}

print(product["producer"]["country_of_origin"])

students = [
    {
        "name": "Ali",
        "family_name": "Khan",
        "skills": {
            "Python": "beginner",
            "JavaScript": "expert",
        },
        "certificates": [
            {
                "name": "Back-end Development",
                "date_of_completion": "2022-01-17",
            },
            {
                "name": "Back-end Development",
                "date_of_completion": "2022-01-17",
            },
            {
                "name": "Data Analytics with Python",
                "date_of_completion": "",
            },
        ],
    },
    {
        "name": "Jessica",
        "family_name": "van Alphen",
        "skills": {
            "Python": "advanced beginner",
            "JavaScript": "beginner",
        },
        "certificates": [
            {
                "name": "Front-end Development",
                "date_of_completion": "",
            },
            {
                "name": "Back-end Development",
                "date_of_completion": "2022-01-17",
            },
            {
                "name": "Data Analytics with Python",
                "date_of_completion": "2020-01-17",
            },
        ],
    },
]

print(students[1]["skills"]["Python"])  # "advanced beginner"
print(students[0]["certificates"][1]["name"])  # "Back-end Development"

# YOUTUBE TUTORIAL
# Python Tutorial for Beginners 5: Dictionaries - Working with Key-Value Pairs
# youtube.com/watch?v=daefaLgNkw0

student = {
    'name': 'John', 
    'age': 25,
    'courses': ['Math', 'CompSci']
}

# student['phone'] = '555_5555' -> Hereby 'phone' gets added to the dictionary
# student['name'] = 'Jane' -> Hereby 'name gets updated from 'John' to 'Jane' in the dictionary
# student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'}) - Hereby all values get either updated or added if the key-value didn't exist yet altogether

# del student['age'] -> Hereby the key-value 'age' gets removed from the dictionary

# age = student.pop('age') -> Hereby the key-value 'age' gets removed as well, though it also gets added to the new value 'age'. Check with print statement below

print(student)
print(student['name'])
print(student['courses'])
print(student.get('name'))
# print(student['phone']) -> KeyError (since Key 'phone' does not exist in the dictionary)
print(student.get('phone')) # Results in: 'None' 
print(student.get('phone', 'Not Found')) # The second value in the get cmd will be displayed if the first value is not found and will replace the 'None' output
# print(age)
print(len(student)) # Shows the amount of keys in the dictionary
print(student.keys())
print(student.values())
print(student.items())

for key in student.items():
    print(key)

for key, value in student.items():
    print(key, value)