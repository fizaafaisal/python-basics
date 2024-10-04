#local variables
def myfunc1():
    z = "Fantastic"
    print(z)
myfunc1()


#Global keyword:
def myfunc():
    global x
    x = "Fantastic"
myfunc()
print("python is "+ x)
