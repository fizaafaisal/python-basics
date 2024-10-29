#6. Check if Key Exists
#Write a program that checks if the key "author" exists in the book dictionary.

book = {
    "title": "The Lord of the Rings",
    "author": "J.R.R. Tolkien",
    "year": 1954,
    "genre": "fantasy"
}
if "author" in book:
    print("yes, author is present")
else:
    print("not present")
    