#add a new item to the original dictionary,
# and see that the item list gets updated as well

car = {
    "brand": "ford",
    "model": "mustang",
    "year": 1984
}

x = car.items()
print(x)

car["color"] = "red"
print(x)
