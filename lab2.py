class Book:
    def __init__(self, title, author, no_of_pages, type):
        self.title = title
        self.author = author
        self.no_of_pages = no_of_pages
        self.type = type

    def print_info(self):
        print(f"Title of book: {self.title}")
        print(f"Author of book: {self.author}")
        print(f"Number of pages in the book: {self.no_of_pages}")
        print(f"Type of book: {self.type}")

book_info = Book("Rest", "Bolu", 150, "novel")
print(book_info.print_info())            

book1 = Book("Sleep", "Dan", 200, "comic")
book2 = Book("Dance", "Joe", 321, "comedy")

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)


    def print_books(self):
        # self.books.print_info() #this gave an attribute error, so i used a for loop
        for book in self.books:
            book.print_info()

    def borrow_book(self, title):
         #covert the string to lowercase, since the capitalization may not be correct
        title= title.lower()

        # to find the book to be borrowed using the book title
        for book in self.books:
            if title == book.title.lower():
                self.books.remove(book)
                return book
            else: 
                return None    



library = Library()
library.add_book(book1)
library.add_book(book2)
library.print_books()

borrow_a_book = library.borrow_book("dance")

if borrow_a_book:
    print(f"Borrowed book: {borrow_a_book.print_info()}")