

class User:
    def __init__(self, uid, name, borrow_books):
        self.id = uid
        self.name = name
        self.borrow_books = borrow_books

    def add_book(self, book):
        if book.id not in self.borrow_books:
            self.borrow_books[book.id] = book

    def remove_book(self, id):
        if id in self.borrow_books:
            del self.borrow_books[id]



class Book:
    #constructor
    def _init_(self,id,title,amount):
        self.id = id
        self.title = title
        self.amount = amount
    
    def stock_update(self,amount_change):
        self.amount += amount_change




