#Read Only parts of the File

#By default the read() method returns the whole text,

#but you can also specify how many character you want to return:

#return the first characters of the file?

f = open("demo.rtf", "r")
print(f.read(5))

