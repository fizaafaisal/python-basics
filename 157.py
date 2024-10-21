#Make a change in the original dictionary,
# and see thet the item list gets updated as well:

car = {
    "brand": "ford",
    "model": "mustang",
    "year": 1984
}
x = car.items()
print(x)  #bfore the change

car["year"] = 2020
print(x)   # after the change

