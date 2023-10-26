# -*- coding: utf-8 -*-
"""
chapter 4 
excercise 5
Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.

•Make a list of your three favorite fruits and call it favorite_fruits.

•Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block

should print a statement,such as You really like bananas!
"""
# A list of my three favorite fruits

favorite_fruits = ["apple", "peach", "watermelon"]


# Check for specific fruits and print a statement if they are in the list
if "apple" in favorite_fruits:
    print("You really love bananas!")
#print from the list
if "peach" in favorite_fruits:
    print("You really love apples!")
#print from the list
if "watermelon" in favorite_fruits:
    print("You really love watermelon!")
#No print not in list
if "strawberry" in favorite_fruits:
    print("You like kiwis!")
#No print not in list
if "mango" in favorite_fruits:
    print("You like mangoes!")

