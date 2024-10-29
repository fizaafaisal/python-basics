# Task 17: Default Value for Missing Key
# 17: "Write a program that tries to access the key 'publisher' from the book dictionary.
# "If it doesn’t exist, return a default message: 'Key not found'.
book = {
    "title": "The Lord of the Rings",
    "author": "J.R.R. Tolkien",
    "year": 1954,
    "genre": "fantasy"
}
if "publisher" in book:
       print("yes, publisher is present")
else:
       print("key not found")
