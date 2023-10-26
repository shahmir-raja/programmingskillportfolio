# -*- coding: utf-8 -*-
"""
Chapter 5
excercise 1
Use a dictionary to store information about a person you know.Store their first name, last name, age, and the city in which they live. You

should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.
"""
#Creating dictionary
person_info = {
    "first_name": "Captain",
    "last_name": "Sparrow",
    "age": 34,
    "city": "London"
}

# Printing information stored in the dictionary
print("First Name: " + person_info["first_name"])
print("Last Name: " + person_info["last_name"])
print("Age: " + str(person_info["age"]))
print("City: " + person_info["city"])

