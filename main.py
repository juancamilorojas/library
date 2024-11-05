from book import Book
from user import User
from library import Library

#Create books
book_1= Book('Fundamentos de Python', 'Carli Platzi')
book_2= Book('Fundamentos de frontend', 'Estefania Platzi')

#Create user
user_0 = User('Juan Camilo', '0')

#Create library
library = Library()
library.add_book(book_1)
library.add_book(book_2)
library.register_user(user_0)
library.show_available_books()