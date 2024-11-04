#Arbitrary Arguments, *args

#If you do not know how many arguments that will
# be passed into your function,
# add a * before the parameter name in the function definition.

#This way the function will receive a tuple of arguments,
# and can access the items accordingly:

#If the number of arguments is unknown,
# add a * before the parameter name:

def myfunc(*kids):
    print("The youngest child is " + kids[1])
myfunc("fiza", "ayman", "dhiya", "najah", "rasal")
