import json

# File to store library data
LIBRARY_FILE = "library.txt"

# Load library from file (if exists)
def load_library():
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save library to file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Add a book to the library
def add_book(library):
    title = input("Enter book title: ").strip()
    author = input("Enter author: ").strip()
    year = input("Enter publication year: ").strip()
    genre = input("Enter genre: ").strip()
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    
    book = {"Title": title, "Author": author, "Year": int(year), "Genre": genre, "Read": read_status}
    library.append(book)
    save_library(library)
    print("Book added successfully!\n")

# Remove a book from the library
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip()
    for book in library:
        if book["Title"].lower() == title.lower():
            library.remove(book)
            save_library(library)
            print("Book removed successfully!\n")
            return
    print("Book not found.\n")

# Search for a book
def search_book(library):
    choice = input("Search by:\n1. Title\n2. Author\nEnter your choice: ")
    query = input("Enter search term: ").strip().lower()
    
    results = [book for book in library if book["Title"].lower() == query or book["Author"].lower() == query]
    if results:
        print("Matching Books:")
        for book in results:
            status = "Read" if book["Read"] else "Unread"
            print(f"{book['Title']} by {book['Author']} ({book['Year']}) - {book['Genre']} - {status}")
    else:
        print("No matching books found.\n")

# Display all books
def display_books(library):
    if not library:
        print("Your library is empty.\n")
        return
    print("Your Library:")
    for i, book in enumerate(library, 1):
        status = "Read" if book["Read"] else "Unread"
        print(f"{i}. {book['Title']} by {book['Author']} ({book['Year']}) - {book['Genre']} - {status}")

# Display statistics
def display_statistics(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book["Read"])
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
    
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.2f}%\n")

# Main menu
def main():
    library = load_library()
    while True:
        print("\nMenu")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

# Run the program
if __name__ == "__main__":
    main()
