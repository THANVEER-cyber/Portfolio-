class Library:
    def _init_(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("List of books in the library:")
            for book in self.books:
                print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}")

    def search_book(self, search_term):
        found_books = [book for book in self.books if search_term.lower() in book['title'].lower() or search_term.lower() in book['author'].lower()]
        if found_books:
            for book in found_books:
                print(f"Found - Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}")
        else:
            print("No books found.")

    def delete_book(self, isbn):
        self.books = [book for book in self.books if book['isbn'] != isbn]
        print(f"Book with ISBN {isbn} has been deleted.")

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            library.add_book({"title": title, "author": author, "isbn": isbn})
            print(f"Book '{title}' added to the library.")
        
        elif choice == '2':
            library.display_books()

        elif choice == '3':
            search_term = input("Enter title or author to search: ")
            library.search_book(search_term)

        elif choice == '4':
            isbn = input("Enter ISBN of book to delete: ")
            library.delete_book(isbn)

        elif choice == '5':
            print("Exiting the library management system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__== "_main_":
    main()