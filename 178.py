#Loop through Nested Dictionaries

#You can loop through a dictionary
#by using the item() method like this.

#Loop through the keys and value of all nested dictionaries?

myfam = {
    "child1": {
        "name": "emil",
        "year": 2004
    },
    "child2": {
        "name": "tobias",
        "year": 2005
    },
    "child3": {
        "name": "linus",
        "year": 2010
    }
}

for x, z in myfam.items():
    print(x)

    for y in z:
        print(y + ':', z[y])

