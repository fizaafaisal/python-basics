#The value True and 1 are considred the same value
#The same goes for false and 0.

#Join sets that contain the value
#True, false, 1, and 0 and see what is considered as duplication?

set1 = {"apple", "banana", 1, 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)
print(set3)
