# -*- coding: utf-8 -*-
"""
Chapter 4:
    excercise 3
Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.

• If the alien is green, print a message that the player earned 5 points.

• If the alien is yellow, print a message that the player earned 10 points.

• If the alien is red, print a message that the player earned 15 points.

• Write three versions of this program, making sure each message is printed for the appropriate color alien.
"""
#V1: Alien is Green (5 points)
alien_color = 'green'
#IF alien is green then message 5 points
if alien_color == 'green':
    print("+5 points for shooting the green alien.")
#IF alien is yellow then message 10 points
elif alien_color == 'yellow':
    print("+10 points for shooting the yellow alien.")
#ELSE alien is red then message 15 points
else:
    print("+15 points for shooting the red alien.")

#V2: Alien is Yellow (10 points)
alien_color = 'yellow'
#IF alien is green then message 5 points
if alien_color == 'green':
    print("+5 points for shooting the green alien.")
#IF alien is yellow then message 10 points
elif alien_color == 'yellow':
    print("+10 points for shooting the yellow alien.")
#ELSE alien is red then message 15 points
else:
    print("+15 points for shooting the red alien.")

# V3: Alien is Red (15 points)
alien_color = 'red'
#IF alien is green then message 5 points
if alien_color == 'green':
    print("+5 points for shooting the green alien.")
#IF alien is yellow then message 10 points    
elif alien_color == 'yellow':
    print("+10 points for shooting the yellow alien.")
#ELSE alien is red then message 15 points    
else:
    print("+15 points for shooting the red alien.")
