#Using a while loop
#You can loop through the tuple items by using a while loop.

#Use the le() func to dtermine the length of the tuple,
#then start at 0 and loop your way through the tuple item by
# reffering to their indexes.

#Remember to increase the index by 1 after each iteration.

#print all items, using a while loop to go through all the index numbers:

thistuple = ("apple", "mango", "orange")
i = 0
while i <len(thistuple):
    print(thistuple[i])
    i = i + 1
