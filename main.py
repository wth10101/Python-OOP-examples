class Item:
    """
    Superclass for all items in the library catalog (e.g., Book, DVD).
    """
    def __init__(self, title):
        # All items must have a title
        self.title = title
        # Type will be set by the subclass, but initialized here
        #self.item_type = 'General Item'

    def display_info(self):
        """ Abstract method to be overridden by subclasses to display specific item details."""
        print(f"\nTitle: **{self.title}**")
        print(f"Type: {self.item_type}")
        print("-" * 20)


class Book(Item):
    def __init__(self, title, author, isbn):
        # Call the superclass constructor
        super().__init__(title)
        self.author = author
        self.isbn = isbn
        self.item_type = 'Book' # Set the specific item type

    def display_info(self):
        # Override the superclass method to include book-specific details
        print(f"\nTitle: **{self.title}**")
        print(f"Type: {self.item_type}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print("-" * 20)


class DVD(Item):
    def __init__(self, title, director, runtime):
        # Call the superclass constructor
        super().__init__(title)
        self.director = director
        # Store runtime in minutes or a descriptive string
        self.runtime = runtime 
        self.item_type = 'DVD' # Set the specific item type

    def display_info(self):
        # Override the superclass method to include DVD-specific details
        print(f"\nTitle: **{self.title}**")
        print(f"Type: {self.item_type}")
        print(f"Director: {self.director}")
        print(f"Runtime: {self.runtime}")
        print("-" * 20)


class Library: 
    def __init__(self):
        self.catalog = []

    def add_item(self, item): # Renamed to add_item for flexibility
        # Check if the item is an instance of the Item superclass or a subclass
        if isinstance(item, Item):
            self.catalog.append(item)
            # Accessing item_type property from the Item class (or its subclasses)
            print(f"\n[SUCCESS] Added {item.item_type}: {item.title}") 
        else:
            print("[ERROR] Item is not a valid library Item object.")

    # Renamed to list_catalog for flexibility
    def list_catalog(self): 
        if not self.catalog:
            print("\nThe library catalog is currently empty.")
            return
        print("\n*** Library Catalog Summary ***")
        for index, item in enumerate(self.catalog, 1):
            # Accessing item_type property
            print(f"{index}. ({item.item_type}) {item.title}")
        print("-------------------------------")

    # Renamed to display_catalog_details for clarity, implementation stays the same
    def display_catalog_details(self):
        if not self.catalog:
            return
        
        print("\n*** Detailed Catalog View ***")
        for item in self.catalog:
            # Polymorphism in action: calling item.display_info()
            # executes the correct method based on the object's actual type (Book or DVD).
            item.display_info()
        print("*****************************")

def main_run():
    # Creating an Object (Instance of Library)
    my_library = Library()

    # --- Creating Objects (Instances of Book) ---
    book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "978-0345391803")
    book2 = Book("Pride and Prejudice", "Jane Austen", "978-0141439518")

    # --- Creating Objects (Instances of DVD) ---
    dvd1 = DVD("Inception", "Christopher Nolan", "148 minutes")
    dvd2 = DVD("The Matrix", "The Wachowskis", "136 minutes")
    
    # Adding all items (Books and DVDs) to the library using the universal method
    my_library.add_item(book1)
    my_library.add_item(book2)
    my_library.add_item(dvd1)
    my_library.add_item(dvd2)

    # Listing the catalog (Summary View)
    my_library.list_catalog()

    # Displaying details (Polymorphism)
    my_library.display_catalog_details()

main_run()