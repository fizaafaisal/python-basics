#3. Add a Key-Value Pair
#Add a new key-value pair ("publisher": "Penguin") to the book dictionary created in Question 1.

book = {
    "title": "The Lord of the Rings",
    "author": "J.R.R. Tolkien",
    "year": 1954,
    "genre": "fantasy"
}
x = book.values()
print(x)

book["publisher"] = "JRR"
print(x)


