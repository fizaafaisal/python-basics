#Make a change in the original dictionary,
# and see thet the value list gets updated as well:

car = {
    "brand": "ford",
    "model": "mustang",
    "year": 1984
}
x = car.values()
print(x)

car["year"] = 2020
print(x)
