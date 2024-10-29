#5. Remove a Key-Value Pair
#Remove the "genre" key from the book dictionary.

book = {
    "title": "The Lord of the Rings",
    "author": "J.R.R. Tolkien",
    "year": 1954,
    "genre": "fantasy"
}
del book["genre"]
print(book)
