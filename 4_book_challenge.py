# ---------------------------------------------------------
#
# Do not change this file.
# Hints are provided at the bottom of this file.
#
# ---------------------------------------------------------


from book_database import Book
turing_book = Book.search('enigma')

print(turing_book.title)
# this prints <book_database.Book object at 0x1021046a0>

assert type(turing_book) is Book
assert turing_book.publisher == "Princeton University."
assert len(Book.publishers) == 15


#####

print("* All assertions passed. Nice work!")




### HINTS:
### -------
### 1. Before starting to code, run this file and read the error message.
### 2. Do the Simplest Thing That Can Possibly Work to resolve the error.
### 3. Run the file again. Use Error-Driven Development until all assertions pass.
### 4. To read a CSV-formatted file with Python's CSV facilities:
#
#      with open("books.csv", encoding='utf-8') as file:
#        reader = csv.reader(file)
#        for row in reader:
#           (your code goes here)
