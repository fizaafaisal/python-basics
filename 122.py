#add any iterable

#The object in the update() method does not have to be a set.
#it can be any iterable object (tuple, list, dictionaries etc)

myset = {"apple", "kiwi", "pomegranate"}
mylist = ["orange", "cherry"]
myset.update(mylist)
print(myset)
