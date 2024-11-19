#4
#append-mode

f = open("myfile27.txt", "a")
f.write("Now the file has more content!")
f.close()

#write-mode

f = open("myfile27.txt", "w")
f.write("all gone")
f.close()
