# -*- coding: utf-8 -*-
"""
chapter 7 
excercise 5

Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence,

such as Reykjavik is in Iceland. Give the parameter for the country a default value.

Call your function for three different cities, at least one of which is not in the default country.

"""
def describe_city(city, country="Pakistan"):
    print(f"{city} is in {country}.")

# Calling the function for three different cities
describe_city("Karachi")
describe_city("New York", "USA")
describe_city("Dubai", "UAE")

