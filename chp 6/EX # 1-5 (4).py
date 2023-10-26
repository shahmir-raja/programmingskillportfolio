# -*- coding: utf-8 -*-
"""
chapter 6
Excercise 4

Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.

Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made,

move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.
"""
# Creating a list of sandwiches
sandwich_orders = ["chicken", "Beef", "cheese", "tuna", "salmon"]

# Creating an empty list for finished sandwiches
finished_sandwiches = []

# Loop through the sandwich orders
while sandwich_orders:
    current_order = sandwich_orders.pop(0) 
# Take the first order
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

# Print a message listing the made sandwiches
print("\nFinished Sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
