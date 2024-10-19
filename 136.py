#The intersection_update() method

# will also keep ONLY the duplicates,
# but it will change the original set instead of returning a new set.

#KEEP the items thet exist in both set1, set2?

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)
print(set1)
