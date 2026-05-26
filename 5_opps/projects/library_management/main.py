import json
from datetime import date, timedelta



# Book Class 
class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.total_copies = copies
        self.available_copies = copies

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "total_copies": self.total_copies,
            "available_copies": self.available_copies
        }

    @staticmethod
    def from_dict(data):
        book = Book(data['title'], data['author'], data['total_copies'])
        book.available_copies = data['available_copies']
        return book


# User Class 
class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []  # list of dicts: {title, due_date}

    def to_dict(self):
        return {
            "name": self.name,
            "borrowed_books": [
                {"title": b['title'], "due_date": b['due_date'].isoformat()} for b in self.borrowed_books
            ]
        }

    @staticmethod
    def from_dict(data):
        user = User(data['name'])
        user.borrowed_books = [
            {"title": b['title'], "due_date": date.fromisoformat(b['due_date'])} for b in data['borrowed_books']
        ]
        return user

    def display_borrowed_books(self):
        for b in self.borrowed_books:
            print(f"Book: {b['title']} | Due Date: {b['due_date']}")


# Library Class
class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def register_user(self, user):
        self.users.append(user)

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_user(self, name):
        for user in self.users:
            if user.name.lower() == name.lower():
                return user
        return None

    def display_books(self):
        for book in self.books:
            print(f"Title: {book.title} | Author: {book.author} | Available: {book.available_copies}/{book.total_copies}")

    def borrow_book(self, title, user):
        book = self.find_book(title)
        if not book:
            print("Book not found.")
            return
        if book.available_copies < 1:
            print("Book not available.")
            return
        if len(user.borrowed_books) >= 3:
            print("User has already borrowed 3 books.")
            return

        due_date = date.today() + timedelta(days=7)
        user.borrowed_books.append({"title": book.title, "due_date": due_date})
        book.available_copies -= 1
        print(f"{user.name} successfully borrowed '{book.title}' until {due_date}.")

    def return_book(self, title, user):
        for b in user.borrowed_books:
            if b['title'].lower() == title.lower():
                book = self.find_book(title)
                if not book:
                    print("Book not found in library.")
                    return

                days_late = (date.today() - b['due_date']).days
                if days_late > 0:
                    fine = days_late * 10
                    print(f"Book is {days_late} day(s) late. Fine: {fine} PKR")
                else:
                    print("Returned on time. No fine.")

                book.available_copies += 1
                user.borrowed_books.remove(b)
                return
        print("Book not found in user's borrowed list.")

    def search_by_title(self, title):
        found = False
        for book in self.books:
            if title.lower() in book.title.lower():
                print(f"Found: {book.title} by {book.author}")
                found = True
        if not found:
            print("No book found with that title.")

    def search_by_author(self, author):
        found = False
        for book in self.books:
            if author.lower() in book.author.lower():
                print(f"Found: {book.title} by {book.author}")
                found = True
        if not found:
            print("No book found by that author.")

    def save_data(self):
        with open("books.json", "w") as f:
            json.dump([book.to_dict() for book in self.books], f, indent=2)
        with open("users.json", "w") as f:
            json.dump([user.to_dict() for user in self.users], f, indent=2)

    def load_data(self):
        try:
            with open("books.json", "r") as f:
                self.books = [Book.from_dict(b) for b in json.load(f)]
        except FileNotFoundError:
            self.books = []

        try:
            with open("users.json", "r") as f:
                self.users = [User.from_dict(u) for u in json.load(f)]
        except FileNotFoundError:
            self.users = []


# CLI 
def menu():
    lib = Library()
    lib.load_data()

    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Register User")
        print("3. Display Books")
        print("4. Search by Title")
        print("5. Search by Author")
        print("6. Borrow Book")
        print("7. Return Book")
        print("8. View Borrowed Books")
        print("9. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            copies = int(input("Enter number of copies: "))
            lib.add_book(Book(title, author, copies))

        elif choice == "2":
            name = input("Enter user name: ")
            lib.register_user(User(name))

        elif choice == "3":
            lib.display_books()

        elif choice == "4":
            title = input("Enter title to search: ")
            lib.search_by_title(title)

        elif choice == "5":
            author = input("Enter author to search: ")
            lib.search_by_author(author)

        elif choice == "6":
            user_name = input("Enter your name: ")
            user = lib.find_user(user_name)
            if not user:
                print("User not found.")
                continue
            title = input("Enter book title: ")
            lib.borrow_book(title, user)

        elif choice == "7":
            user_name = input("Enter your name: ")
            user = lib.find_user(user_name)
            if not user:
                print("User not found.")
                continue
            title = input("Enter book title: ")
            lib.return_book(title, user)

        elif choice == "8":
            user_name = input("Enter your name: ")
            user = lib.find_user(user_name)
            if user:
                user.display_borrowed_books()
            else:
                print("User not found.")

        elif choice == "9":
            lib.save_data()
            print("Data saved. Exiting...")
            break

        else:
            print("Invalid choice. Try again.")


# Main 
if __name__ == "__main__":
    menu()
