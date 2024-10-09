#Remove list item
#the remove () method removes the specified item.

#Remove "banana"?

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#if there are more than one item with the specified values,
#the removes() method removes the first occurence:

#remove the first occurence of "banana" ?
thislist1 = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist1.remove("banana")
print(thislist1)
