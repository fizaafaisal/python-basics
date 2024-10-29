#Create three dictionaries?
# then create one dictionary thet will contain
# the other three dictionaries?

child1 = {
    "name": "emil",
    "year": 2004
}
child2 = {
    "name": "tobias",
    "year": 2002
}
child3 = {
    "name": "Linus",
    "year": 2011
}
myfam = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myfam)
