import csv

class Book:
  # has to be a better way to do this since its repetative
  publishers = []
  with open("books.csv", encoding='utf-8') as file:
      reader = csv.reader(file)
      for row in reader:
        publishers.append(row[3])


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
      
