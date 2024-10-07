#the format() method takes unlimited number of arguements
# and are placed into the perspective placeholders:

quantity = 3
itemno = 567
price = 50

myorder = "I want {} pieces of item {} for {} dollars."

print(myorder.format(quantity, itemno, price))
