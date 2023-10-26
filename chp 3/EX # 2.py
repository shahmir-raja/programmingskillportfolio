"""
Start with the list you used in Exercise 1, but instead of just

printing each person’s name, print a message to them. The text of each message should be the same, but each message should be

personalized with the person’s name.
"""
names = ["Sam", "Chris", "val", "ravid", "steve"]

# Print a personalized message to each person
for name in names:
    message = f"Hello, {name}! Have a great day."
    print(message)
