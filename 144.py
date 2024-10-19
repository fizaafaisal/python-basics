#The symmetric_diffrence_update() method
# will also keep all but the duplicates,
#but it will change the original set instead of returning a new set.

#Use the symmetric_difference_update() method to
#Keep the item thet are not present in both sets?

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)
