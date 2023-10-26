# -*- coding: utf-8 -*-
"""
chapter 7 
excercise 4

Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a

medium shirt with the default message, and a shirt of any size with a different message.
"""
def make_shirt(size="large", message="I love Python"):
    print(f"Making a {size}-sized shirt with the message: '{message}'")

# Creating a large shirt with the default message
make_shirt()

# Creating a medium shirt with the default message
make_shirt(size="medium")

# Creating a small shirt with a different message
make_shirt(size="small", message="Python rules")
