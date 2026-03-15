class Book:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    def __str__(self):
        return f"{self.title} - {self.author} (ISBN: {self.isbn})"
#Lista u koju cemo spremati knjige
library_inventory = []
#Funkcija za dodavanje knjige
def add_book(title,author,isbn):
    new_book = Book(title,author,isbn)
    library_inventory.append(new_book)
    print(f"Knjiga dodata: {new_book}")
#Funkcija za prikaz svih knjiga
def show_books():
    print("\nTrenutno u biblioteci:")
    for book in library_inventory:
        print(book)
#Testiranje koda
if __name__ == "__main__":
    add_book("Na Drini ćuprija","Ivo Andrić","123456")
    add_book("Seobe","Miloš Crnjanski","789012")
    show_books()