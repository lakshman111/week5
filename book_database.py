import csv

class Book:
  publishers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

  def search(term):
    books = []

    with open("books.csv", encoding='utf-8') as file:
      reader = csv.reader(file)
      for row in reader:
        if row:
          book = Book()
          book.id = row[0]
          book.title = row[1]
          book.author = row[2]
          book.publisher = row[3]
          books.append(book)
    for book in books:
      if term.lower() in book.title.lower():
        return book

    return None

      
