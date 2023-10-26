
"""
Chapter 5
Excercise 2

A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store
their meanings as values.

Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print
the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between

each word-meaning pair in your output.    
"""
# Create a glossary of programming terms and their meanings
glossary = {
    "variable": "Container that can store data in a program.",
    "function": "A block of code that performs a specific task",
    "loop": "a repeating block of function.",
    "list": "number of items that can be stored in different types",
    "dictionary": "collections of keys used to store and use data."
}

# Printing each term and its meaning with a newline between each pair
for term, meaning in glossary.items():
    print(f"{term}:\n{meaning}\n")

