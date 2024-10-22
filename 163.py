#Remove Dictionary Items
# removing items
#there are several methods to remove items from a dictionary:

#The pop() method removes the item with the specified key name:

thisdict = {
    "brand": "ford",
    "model": "mustang",
    "year": 1984
}

thisdict.pop("model")
print(thisdict)
