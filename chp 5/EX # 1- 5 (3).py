# -*- coding: utf-8 -*-
"""
Chapter 5 
excercise 3

Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()

calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms

to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.

"""
# Creating glossary
glossary = {
    "variable": "container for program data.",
    "function": "Reusable code for tasks.",
    "loop": "Repeats code multiple times.",
    "list": "Stores various items.",
    "dictionary": "key-value data storage.",
    "module": "Contains Python code for functions and classes.",
    "class": "Object blueprint in OOP.",
    "inheritance": "OOP mechanism.",
    "algorithm": "Step-by-step problem-solving instructions.",
    "IDE": "Development software for coding."
}

# Printing the glossary with a header and newlines as explained
print("Python Programming Glossary:\n")
for term, meaning in glossary.items():
    print(f"{term}:\n{meaning}\n")