#perform a case- insensitive sort of the list:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)

print(thislist)

#The key parameter is set to str.lower,
# which means that the list will be sorted based
# on the lower case version of each string element.

#"banana".lower() returns "banana"
#"Orange".lower() return "orange"
#"Kiwi".lower() return "kiwi"
#"cherry".lower() return "cherry"
