from models import Book
from models import User

class Library:
    def __init__(self):
        self.users = {}
        self.books = {}

    def add_book(self, id, title, amount):
        if id in self.books:
            self.books[id].stock_update(amount)
        else:
            self.books[id] = Book(id, title, amount)
        print(f"Kitap başarıyla eklendi: {title}")

    def add_user(self, id, name):
        if id not in self.users:
            self.users[id] = User(id, name, {})
            print(f"Kullanıcı başarıyla eklendi: {name}")
        else:
            print(f"Kullanıcı zaten mevcut: {name}")

    def show_books(self):
        for book in self.books:
            print(" kitap_id:{book.id} kitap_adı:{book.title} kitap_miktarı:{book.amount}")

    def borrow_book(self, kitap_id, kullanici_id):
        if kitap_id in self.books and kullanici_id in self.users:
            book = self.books[kitap_id]
            user = self.users[kullanici_id]
            if book.amount > 0:
                book.amount -= 1
                user.add_book(book)
                print(f"{book.title} adlı kitap ödünç alındı")
            else:
                print(f"{book.title} adlı kitap stokta yok")
        else:
            print("Geçersiz kitap veya kullanıcı ID")

    def return_book(self, uid, id):
        user = self.users[id]
        if id in user.borrow_books:
            book = user.borrow_books[uid]
            book.stock_update(1)
            user.remove_book(id)
            print(f"{book.title} adlı kitap iade edildi")
        else:
            print(f"{book.title} geri alınamıyor")

def LibraryAutomation():
    lib = Library()

    while True:
        print("\n1. Kitap Ekle")
        print("2. Kullanıcı Ekle")
        print("3. Kitap Ödünç Al")
        print("4. Kitap İade Et")
        print("5. Kütüphanedeki Kitapları Listele")
        print("6. Çıkış")

        islem = input("Bir işlem seçin: ")

        if islem == "1":
            kitap_id = int(input("Kitap ID: "))
            ad = input("Kitap Adı: ")
            miktar = int(input("Kitap Miktarı: "))
            lib.add_book(kitap_id, ad, miktar)

        elif islem == "2":
            kullanici_id = int(input("Kullanıcı ID: "))
            ad = input("Kullanıcı Adı: ")
            lib.add_user(kullanici_id, ad)

        elif islem == "3":
            kitap_id = int(input("Kitap ID: "))
            kullanici_id = int(input("Kullanıcı ID: "))
            lib.borrow_book(kitap_id, kullanici_id)

        elif islem == "4":
            kitap_id = int(input("Kitap ID: "))
            kullanici_id = int(input("Kullanıcı ID: "))
            lib.return_book(kullanici_id, kitap_id)

        elif islem == "5":
            lib.show_books()

        elif islem == "6":
            print("Sistemden çıkılıyor...")
            break

        else:
            print("Geçersiz seçim, tekrar deneyin.")



LibraryAutomation()


