# -*- coding: utf-8 -*-
"""
chapter 5
excercise 5

Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the

owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about

each pet
"""
# creating dictionaries with different pets and owners
pets = [
    {"kind": "snake", "owner": "Bayla"},
    {"kind": "rooster", "owner": "yang"},
    {"kind": "Cat", "owner": "Ken"},
    {"kind": "Dog", "owner": "Sam"},
    {"kind": "Rabbit", "owner": "Lee"}
]

# loop and print info abt each pet
for pet in pets:
    print(f"Kind of Animal: {pet['kind']}")
    print(f"Owner's Name: {pet['owner']}")
    print()  
# Print a blank line to separate pet information

