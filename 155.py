#Add a new items to the original dictionary,
#and see thet the values list gets updated as well:

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1984
}

x = car.values()
print(x)

car["color"] = "red"
print(x)
