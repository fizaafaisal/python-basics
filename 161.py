#Update Dictionary
#The update() method will update the dictionary
# with the items from the given argument.

#The argument must be a dictionary,
# or an iterable object with key:value pairs.
#Update the year of the car by using the update() method:

thisdict = {
    "brand": "ford",
    "model": "mustang",
    "year": 1984
}

thisdict.update({"year": 2020})
print(thisdict)
