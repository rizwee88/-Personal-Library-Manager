# import json

# # File to store library data
# LIBRARY_FILE = "library.txt"

# # Load library from file (if exists)
# def load_library():
#     try:
#         with open(LIBRARY_FILE, "r") as file:
#             return json.load(file)
#     except (FileNotFoundError, json.JSONDecodeError):
#         return []

# # Save library to file
# def save_library(library):
#     with open(LIBRARY_FILE, "w") as file:
#         json.dump(library, file, indent=4)

# # Add a book to the library
# def add_book(library):
#     title = input("Enter book title: ").strip()
#     author = input("Enter author: ").strip()
#     year = input("Enter publication year: ").strip()
#     genre = input("Enter genre: ").strip()
#     read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    
#     book = {"Title": title, "Author": author, "Year": int(year), "Genre": genre, "Read": read_status}
#     library.append(book)
#     save_library(library)
#     print("Book added successfully!\n")

# # Remove a book from the library
# def remove_book(library):
#     title = input("Enter the title of the book to remove: ").strip()
#     for book in library:
#         if book["Title"].lower() == title.lower():
#             library.remove(book)
#             save_library(library)
#             print("Book removed successfully!\n")
#             return
#     print("Book not found.\n")

# # Search for a book
# def search_book(library):
#     choice = input("Search by:\n1. Title\n2. Author\nEnter your choice: ")
#     query = input("Enter search term: ").strip().lower()
    
#     results = [book for book in library if book["Title"].lower() == query or book["Author"].lower() == query]
#     if results:
#         print("Matching Books:")
#         for book in results:
#             status = "Read" if book["Read"] else "Unread"
#             print(f"{book['Title']} by {book['Author']} ({book['Year']}) - {book['Genre']} - {status}")
#     else:
#         print("No matching books found.\n")

# # Display all books
# def display_books(library):
#     if not library:
#         print("Your library is empty.\n")
#         return
#     print("Your Library:")
#     for i, book in enumerate(library, 1):
#         status = "Read" if book["Read"] else "Unread"
#         print(f"{i}. {book['Title']} by {book['Author']} ({book['Year']}) - {book['Genre']} - {status}")

# # Display statistics
# def display_statistics(library):
#     total_books = len(library)
#     read_books = sum(1 for book in library if book["Read"])
#     percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
    
#     print(f"Total books: {total_books}")
#     print(f"Percentage read: {percentage_read:.2f}%\n")

# # Main menu
# def main():
#     library = load_library()
#     while True:
#         print("\nMenu")
#         print("1. Add a book")
#         print("2. Remove a book")
#         print("3. Search for a book")
#         print("4. Display all books")
#         print("5. Display statistics")
#         print("6. Exit")
        
#         choice = input("Enter your choice: ")
#         if choice == "1":
#             add_book(library)
#         elif choice == "2":
#             remove_book(library)
#         elif choice == "3":
#             search_book(library)
#         elif choice == "4":
#             display_books(library)
#         elif choice == "5":
#             display_statistics(library)
#         elif choice == "6":
#             save_library(library)
#             print("Library saved. Goodbye!")
#             break
#         else:
#             print("Invalid choice, please try again.\n")

# # Run the program
# if __name__ == "__main__":
#     main()
import streamlit as st
import json

# File name for storing the library
db_file = "library.json"

# Load library from file if available
def load_library():
    try:
        with open(db_file, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save library to file
def save_library(library):
    with open(db_file, "w") as f:
        json.dump(library, f, indent=4)

# Initialize library
library = load_library()

st.title("📚 Personal Library Manager")

# Sidebar menu
menu = st.sidebar.selectbox("Menu", ["Add a book", "Remove a book", "Search for a book", "Display all books", "Display statistics"])

if menu == "Add a book":
    st.subheader("Add a New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Publication Year", min_value=0, step=1)
    genre = st.text_input("Genre")
    read_status = st.checkbox("Have you read this book?")
    
    if st.button("Add Book"):
        library.append({"title": title, "author": author, "year": int(year), "genre": genre, "read": read_status})
        save_library(library)
        st.success("Book added successfully!")

elif menu == "Remove a book":
    st.subheader("Remove a Book")
    titles = [book["title"] for book in library]
    book_to_remove = st.selectbox("Select a book to remove", titles)
    
    if st.button("Remove Book"):
        library = [book for book in library if book["title"] != book_to_remove]
        save_library(library)
        st.success("Book removed successfully!")

elif menu == "Search for a book":
    st.subheader("Search for a Book")
    search_by = st.radio("Search by", ("Title", "Author"))
    query = st.text_input("Enter search term")
    
    if st.button("Search"):
        results = [book for book in library if query.lower() in book[search_by.lower()].lower()]
        if results:
            for book in results:
                st.write(f"**{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
        else:
            st.warning("No matching books found.")

elif menu == "Display all books":
    st.subheader("Your Library")
    if library:
        for book in library:
            st.write(f"**{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    else:
        st.info("Your library is empty.")

elif menu == "Display statistics":
    st.subheader("Library Statistics")
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    st.write(f"Total books: {total_books}")
    st.write(f"Percentage read: {100 * read_books / total_books:.2f}%")
