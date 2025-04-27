# Assignment:
# Create a class Book with a class variable total_books. Add a
#  class method increment_book_count() to increase the count when a new book is added.

class Book:
  total_books=0
  def __init__(self,name,publish_date) -> None:
     self.name = name 
     self.publish_date = publish_date
  @classmethod
  def count_books(cls):
    cls.total_books += 1
    print(cls.total_books ,"total no of books created with this instance." )
book1:Book = Book("Game of thrones" ,"12/12/12")
book2:Book = Book("Game of thrones" ,"12/12/12")
book3:Book = Book("Game of thrones" ,"12/12/12")
print(book1.count_books())
print(book2.count_books())
print(book3.count_books())

book1.total_books

 
