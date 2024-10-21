#Check if key exist

# To determine if a specified key is present in
# a dictionary use the in keyword:

#Check if "model" is present in the dictionary?

thisdict = {
    "brand": "ford",
    "model": "mustang",
    "year": 1984
}
if "model" in thisdict:
    print("yes, 'model' is one of the keys ")
else:
    print("not present")
    