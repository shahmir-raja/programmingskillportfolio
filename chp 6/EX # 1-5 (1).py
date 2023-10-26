# -*- coding: utf-8 -*-
"""
Chapter 6
Excercise 1

Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,

print a message saying you’ll add that topping to their pizza.
"""
# Make an empty list to store pizza toppings
pizza_toppings = []

while True:
    topping = input("choose a pizza topping (or 'stop' to finish): ")

    if topping.lower() == 'stop':
        break  
    # Exit the loop if the user enters 'quit'
    else:
        pizza_toppings.append(topping)
        print(f"adding {topping} to your pizza.")

# Printing the selected pizza toppings
if pizza_toppings:
    print("Your pizza will have the following toppings:")
    for topping in pizza_toppings:
        print(topping)
else:
    print("You didn't choose any toppings for your pizza.")
    
