# -*- coding: utf-8 -*-
"""
Chapter 6
Excercise 2

A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if

they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their

age, and then tell them the cost of their movie ticket
"""
while True:
    age = input("Enter your age (or 'stop' to exit): ")

    if age.lower() == 'stop':
        break

    age = int(age)  
    # Convert the input to an integer

    if age < 3:
        ticket_price = 0
    elif 3 <= age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15

    print(f"this movie will cost you ${ticket_price}")

