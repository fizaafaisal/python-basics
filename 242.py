#number of arguments

#By default, a funtion must be called with the correct
# number of argument.
# Meaning that if your function expects 2 argument,
# you have to call the funtion with 2 argument, mot more,
# and not less.

#This function expects 2 args, and get 2 args?

def myfunc(fname, lname):
    print(fname + " " + lname)
myfunc("emil", "tomas")
