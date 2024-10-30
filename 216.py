#Nested If

# If statements inside if statement,
# this is called nested if statement.

x = 41
if x > 20:
    print("10")
    if x > 20:
        print("and also above 20")
    else:
        print("but not above 20")
else:
    print("less than 10")