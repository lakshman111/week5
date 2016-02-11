import csv

class Book:
  publishers = []

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
          Book.publishers.append(book.publisher)
          books.append(book)
    for book in books:
      if term.lower() in book.title.lower():
        return book

    return None
      
