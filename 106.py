#Remove Items
#Note: you cannot remove items in a tuple

#Tuples are unchangeable, so ypu cannot remove items from it,
#but you can use the same workaround as we ussed for changing
# and adding tuple items:

#convert the tuple into a list, remove "apple",
# and convert it back into a tuple?

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
