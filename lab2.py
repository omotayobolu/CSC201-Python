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
         #covert the string to lowercase, for case sensitivity
        title= title.lower()

        # to find the book to be borrowed using the book title
        for book in self.books:
            if title == book.title.lower():
                self.books.remove(book)
                return book
             
        return None    

# create a library instance
library = Library()

# to read the book information from the books file created, add them to the library instance, then print the books in the library

with open('books.txt', 'r') as books:
    for line in books:
        title, author, no_of_pages, type = line.strip().split(',')
        #.strip() is used to remove extra white spaces in the string, and split(',') is used to split a string into a comma-separated list
        book = Book(title, author, no_of_pages, type) #create an instance of Book
        library.add_book(book) #to add the book to the library

library.print_books() #to print books in the library


#to borrow a book, use the input function to ask the user for the book they want to borrow
# it is best to use a while loop so it can keep asking the user for a current input that is, a title of a book currently in the library then can terminate the loop after getting our required answer.
while True:
    book_to_borrow = input("Enter the title of the book you want to borrow: ")
    borrowed_book = library.borrow_book(book_to_borrow)
    if borrowed_book:
        print("You borrowed: ")
        print("")
        borrowed_book.print_info()
        print("")
        print("Remaining books in the library after you borrowed: ")
        print("")
        library.print_books()
        break
    else:
        print(f"There is no book titled {book_to_borrow} in the library. Try looking for another book")
