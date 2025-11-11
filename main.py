class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        print(f"\nTitle: **{self.title}**")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print("-" * 20)
        

class Library:  
    def __init__(self):
        self.catalog = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.catalog.append(book)
            print(f"\n[SUCCESS] Added: {book.title}")
        else:
            print("[ERROR] Item is not a valid Book object.")

    def list_books(self):
        if not self.catalog:
            print("\nThe library catalog is currently empty.")
            return
        print("\n*** Library Catalog Summary ***")
        for index, book in enumerate(self.catalog, 1):
            print(f"{index}. {book.title}")
        print("-------------------------------")

    def display_catalog_details(self):
        if not self.catalog:
            return
        
        print("\n*** Detailed Catalog View ***")
        for book in self.catalog:
            book.display_info()
        print("*****************************")

def main_run():
    # Creating an Object (Instance of Library)
    my_library = Library()
    # Creating Objects (Instances of Book)
    book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "978-0345391803")
    
    book2 = Book("Pride and Prejudice", "Jane Austen", "978-0141439518")
    book3 = Book("Sapiens: A Brief History of Humankind", "Yuval Noah Harari", "978-0062316097")


    # Adding the books to the library
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)

    # Listing the books (Summary View)
    my_library.list_books()

    # Displaying details (calling Book's method via Library)
    my_library.display_catalog_details()

main_run()
