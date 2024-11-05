#Recursion
#Python also accepts function recursion,
# which means a define function can call itself.

#Example of a recursion funtion.
def factorial(x):

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
num = 3
print("The factorial of", num, "is", factorial(num))
