class Library:
    def __init__(self):
        self.books=[]
        self.users=[]

    def add_book(self, book): 
        if book not in self.books:
            self.books.append(book)
            print(f'El libro {book.title} fue agregado')
    
    def register_user(self, user):
         if user not in self.users:
            self.users.append(user)
            print(f'El usuario {user.name} fue registrado')       
    
    def show_available_books(self):
        print("Libros Disponibles:")
        for book in self.books:
            if book.available:
                print(f'{book.title} por {book.author}')
