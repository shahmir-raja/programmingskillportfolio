# -*- coding: utf-8 -*-
"""
chapter 6
excercise 5

Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code

near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all

occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

   
"""
# Creating list of sandwiches with 'pastrami' repeated at least three times
sandwich_orders = ["chicken", "tuna", "pastrami", "cheese", "beef", "pastrami", "pastrami", "vegetarian", "pastrami"]

# Creating an empty list for finished sandwiches
finished_sandwiches = []

# Print message displaying the deli doesnt have pastrami
print("sorry!, there arent any pastrami sandwiches left")

# Removing all occurrences of 'pastrami' from sandwich_orders
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Loop in the list of sandwich orders
while sandwich_orders:
    current_order = sandwich_orders.pop(0)  
# Take the first order
    print(f"Here is your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

# Print a message listing each sandwich that was made
print("\nFinished Sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)

