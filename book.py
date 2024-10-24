class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    
    def borrow(self):
        if self.available:
            self.available=False
        else:
            print(f'El libro {self.title} no se encuentra disponible')
    
    def return_book(self):
        if not self.available:
            self.available=True
        else: 
            print('No puedes retornar un libro que no esté prestado')
    