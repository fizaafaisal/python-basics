#Exit the loop when x is "banana",
# but this time the break comes before the print:

fruits = ["apple", "mango", "litchi"]
for x in fruits:
    if x == "mango":
        break
    print(x)
