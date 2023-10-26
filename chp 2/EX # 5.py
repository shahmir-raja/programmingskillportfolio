"""
Exercise 5: USB Shopper
A girl heads to a computer shop to buy some USB sticks. 
She loves USB sticks and wants as many as she can get for £50. They are £6 each.

Write a programme that calculates how many USB sticks she can buy
 and how many pounds she will have left.

You will to use the arithmetic operators to complete this exercise.
"""
budget = 50
Price = 6
#calculate how many she can afford
usb_count = budget // Price
#calculating her change
change = budget % Price
#results
print('total number of USB she can afford:', usb_count)
print('her remaining money:',change)

