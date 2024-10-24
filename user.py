 user:
    def __init__(self, name, user_id):
        self.name = name 
        self.user_id = user_id
        self.borrowed_books=[]
    
    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book.title)
            print(f'El usuario {user_id} ha prestado {book.title}')
        else: 
            print(f'El libro {book.title} no está disponible')
    
    def return_book(self, book):
        if book.title in self.borrowed_books: 
            book.return_book()
            self.borrowed_books.remove(book.title)
            print(f'El usuario {user_id} ha retornado {book.name}')
        else: 
            print(f'El usuario {user_id} no ha prestado el libro {book.title}')
