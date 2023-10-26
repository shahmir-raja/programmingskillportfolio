
"""
CHP:3 EX:7
Think of at least five places in the world you’d like to visit. • Store the locations in a list. Make sure the list is not in alphabetical order.

• Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.

• Use sorted() to print your list in alphabetical order without modifying the actual list.

• Show that your list is still in its original order by printing it.

• Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.

• Show that your list is still in its original order by printing it again.

• Use reverse() to change the order of your list. Print the list to show that its order has changed.

• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.

• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.

• Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
"""
#Places I want to visit 
Placestovisit=['Greece','USA','UK','Japan','Egypt']

#use sorted() to put in Alpahbetical order without any modification
print("Alphabetical order:",sorted(Placestovisit))

#show the original list
print("Original order:",Placestovisit)

#use sort to change list in reverse alaphabetical order without changing original order
print("Reverse alphabetical order:",sorted(Placestovisit,reverse=True))

#show the original order
print("original order:",Placestovisit)

#using reverse() to chnage the order of the list
Placestovisit.reverse()

#print list that show changed order
print("Reverse order:",Placestovisit)

#using reverse( to chnage the order again to original
Placestovisit.reverse()

#print to show original order
print("Original order:",Placestovisit)

#using the sort to put in alphabetical order
Placestovisit.sort()

#print to show the alphabetical order
print("Alphabetical order:",Placestovisit)

# Using sorted to chnage the list in reverse alphabetical order
Placestovisit.sort(reverse=True)

#print the list to show that its order has changed
print("Reverse alphabetical order:", Placestovisit)






