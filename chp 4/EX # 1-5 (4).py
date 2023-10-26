# -*- coding: utf-8 -*-
"""
CHAPTER 4
EXCERCISE 4
Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:

•If the person is less than 2 years old, print a message that the person is a baby.

•If the person is at least 2 years old but less than 4, print a message that the person is a toddler.

•If the person is at least 4 years old but less than 13, print a message that the person is a kid.

•If the person is at least 13 years old but less than 20, print a message that the person is a teenager.

•If the person is at least 20 years old but less than 65, print a message that the person is an adult.

•If the person is age 65 or older, print a message that the person is an elder.
"""
# Enter your age
age = int(input("Enter your age: "))

#If age is less than 2
if age < 2:
    print("You are a baby.")
#If age is less than 4
elif age < 4:
    print("You are a toddler.")
#If age is less than 13
elif age < 13:
    print("You are a kid.")
#If age is less than 20
elif age < 20:
    print("You are a teenager.")
#If is less than 65    
elif age < 65:
    print("You are an adult.")
#Else age is greater
else:
    print("You are an elder.")
