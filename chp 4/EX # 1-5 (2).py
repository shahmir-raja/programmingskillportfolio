"""
Chapter 4:
Exercise 2: Alien Colors #2 
Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.

•If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.

•If the alien’s color isn’t green, print a statement that the player just earned 10 points.

•Write one version of this program that runs the if block and another that runs the else block.
"""
#assign alien color
alien_color='green'
#if color is green print statement and if itsnt green print else statement
if alien_color=='green':
    print('player earned 5 points')
else:
    print('player earned 10 points for shooting a different colored alien.')
#assign alien color    
alien_color='Blue'
#if alien color isnt green print else statement version
if alien_color=='red':
    print('Player earned 5 points')
else:
    print('player earned 10 points for shooting a red colored alien')
    


      
