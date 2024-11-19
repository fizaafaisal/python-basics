#check if file exist?

#To avoid getting an error,
# you might want to check if
#the file exists before you try to delete it?

import os
if os.path.exists("myfile27.rtf"):
    os.remove("myfile27.txt")
else:
    print("the file does not exist")
