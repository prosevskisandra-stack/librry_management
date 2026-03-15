class Book:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    def __str__(self):
        return f"{self.title} - {self.author} (ISBN: {self.isbn})"
#Lista u koju cemo spremati knjige
library_inventory = []
print("Sistem za upravljanje bibliotekom je prekinut.")