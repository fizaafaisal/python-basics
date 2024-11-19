#close files
# it is a good practice to always
#close the file when you are done with it.

#close the file when you are finish with it

f = open("demofile.rtf", "r")
print(f.readline())
f.close()

#open and read the file after the appending
f = open("demofile.rtf", "r")
print(f.read())
f.close()
