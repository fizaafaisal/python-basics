# Global variables:

#create a variable outside of a function,and
# use it inside the function & outside the function.

x = "awesome"

def funcname():
    print("python is " + x)

funcname()
print(x)
