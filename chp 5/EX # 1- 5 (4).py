# -*- coding: utf-8 -*-
"""
Chapter 5
Excercise 4
Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

Use a loop to print the name of each river included in the dictionary.

Use a loop to print the name of each country included in the dictionary.
"""
# creating dictionaries of rivers and countaries they are in.
rivers = {
    'Tay': 'Scotland',
    'Amazon': 'Brazil',
    'Indus': 'Pakistan'
}

# Printing the sentences about the rivers
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country}.")

# Printing names of each river
print("\nRivers:")
for river in rivers.keys():
    print(river.title())

# Printing names of each country
print("\nCountries:")
for country in rivers.values():
    print(country)
