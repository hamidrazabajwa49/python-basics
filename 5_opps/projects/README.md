# 🗂️ Projects

This folder contains six fully working Python projects — each one built entirely using Object-Oriented Programming. They aren't exercises with a single right answer; they're complete, runnable applications that demonstrate how the four OOP pillars come together in real software.

Every project lives in its own folder and runs from a single `main.py` file.

---

## 📂 Folder Structure

```
projects/
│
├── chatbot/
│   └── main.py
├── expense_tracker/
│   └── main.py
├── library_management/
│   └── main.py
├── password_manager/
│   └── main.py
├── student_management/
│   └── main.py
└── todo_list/
    └── main.py
```

---

## 💬 Chatbot

**Folder:** `chatbot/`

A rule-based conversational chatbot you can talk to in the terminal. It recognises greetings, farewells, questions, and common phrases — and falls back gracefully when it doesn't understand something.

**What it does:**
- Greets the user and starts a conversation loop
- Matches user input against predefined patterns and responds accordingly
- Handles unknown input with a polite fallback message
- Ends the session cleanly when the user says goodbye

**OOP concepts used:**
- `Chatbot` class encapsulating all response logic and conversation state
- Methods for greeting, pattern matching, and farewell handling
- Private response dictionaries hidden behind public `respond()` method

**Run it:**
```bash
python chatbot/main.py
```

**Sample interaction:**
```
Chatbot: Hello! I'm your Python chatbot. How can I help you?
You: hi
Chatbot: Hey there! What's on your mind?
You: what is python?
Chatbot: Python is a powerful, beginner-friendly programming language!
You: bye
Chatbot: Goodbye! Have a great day!
```

---

## 💸 Expense Tracker

**Folder:** `expense_tracker/`

A personal finance tool for logging daily expenses, organising them by category, and seeing exactly where your money is going.

**What it does:**
- Add an expense with an amount, category, and optional description
- View all logged expenses in a clean, formatted list
- Get a category-wise spending summary (Food, Transport, Shopping, etc.)
- Delete an expense by its ID
- See the total amount spent across all entries

**OOP concepts used:**
- `Expense` class representing a single transaction with its own attributes
- `ExpenseTracker` class managing the full list of expense objects
- Encapsulated add, remove, and filter logic inside the tracker class
- `__str__()` on `Expense` for clean formatted output

**Run it:**
```bash
python expense_tracker/main.py
```

**Sample interaction:**
```
1. Add Expense
2. View All Expenses
3. View Summary by Category
4. Delete Expense
5. Exit

> 1
Amount: 450
Category: Food
Description: Dinner at restaurant
✅ Expense added!

> 3
📊 Spending Summary:
  Food         : Rs. 450
  Transport    : Rs. 120
  Total        : Rs. 570
```

---

## 📚 Library Management System

**Folder:** `library_management/`

A complete library system for managing a collection of books and member borrowing records — the kind of backend logic that powers real library software.

**What it does:**
- Add new books to the library catalogue
- Register members to the system
- Issue a book to a member (marks it as unavailable)
- Return a book (marks it as available again)
- View all books — available and borrowed separately
- View a member's currently borrowed books

**OOP concepts used:**
- `Book` class with attributes for title, author, ISBN, and availability status
- `Member` class tracking member name, ID, and list of borrowed books
- `Library` class managing collections of both `Book` and `Member` objects
- Encapsulated issue/return logic with availability checks
- `isinstance()` checks to validate object types before operations

**Run it:**
```bash
python library_management/main.py
```

**Sample interaction:**
```
1. Add Book
2. Register Member
3. Issue Book
4. Return Book
5. View All Books
6. View Member's Books
7. Exit

> 5
📚 Available Books:
  [001] Clean Code — Robert C. Martin
  [002] Python Crash Course — Eric Matthes

📕 Borrowed Books:
  [003] Atomic Habits — James Clear  →  Borrowed by: Ali
```

---

## 🔐 Password Manager

**Folder:** `password_manager/`

A terminal-based password manager for storing and retrieving credentials for different services — with basic protection so passwords aren't displayed carelessly.

**What it does:**
- Save a password for any service (e.g., Gmail, GitHub, Netflix)
- Retrieve a stored password by service name
- Update an existing password entry
- Delete a saved entry
- List all services with stored credentials (without showing passwords)

**OOP concepts used:**
- `PasswordEntry` class encapsulating service name, username, and password
- `PasswordManager` class with a private `__vault` dictionary storing all entries
- Passwords accessed only through controlled `get_password()` method — never directly
- Update and delete methods with existence checks before modifying state

**Run it:**
```bash
python password_manager/main.py
```

**Sample interaction:**
```
1. Save Password
2. Retrieve Password
3. Update Password
4. Delete Entry
5. List All Services
6. Exit

> 1
Service: Gmail
Username: ali@gmail.com
Password: ••••••••
✅ Saved!

> 5
🔑 Stored Services:
  - Gmail
  - GitHub
  - Netflix
```

---

## 🎓 Student Management System

**Folder:** `student_management/`

A student record system for managing a classroom — adding students, recording their grades, computing averages, and generating a ranked report.

**What it does:**
- Add a new student with a name and roll number
- Add subject-wise grades for any student
- View a student's full grade report with their average
- Display a class leaderboard ranked by average grade
- Compute the overall class average

**OOP concepts used:**
- `Student` class with private grade list, exposed through methods and `@property` for the average
- `Classroom` class managing the full list of student objects
- `__str__()` on `Student` for formatted individual reports
- Polymorphic `display_report()` method behaving appropriately per student's data

**Run it:**
```bash
python student_management/main.py
```

**Sample interaction:**
```
1. Add Student
2. Add Grade
3. View Student Report
4. View Class Leaderboard
5. View Class Average
6. Exit

> 4
🏆 Class Leaderboard:
  1. Sara        — Avg: 91.5
  2. Ali         — Avg: 87.0
  3. Zain        — Avg: 74.3

> 5
📊 Class Average: 84.3
```

---

## ✅ To-Do List

**Folder:** `todo_list/`

A task manager with priorities and status tracking — add tasks, mark them done, filter by status, and keep your work organised.

**What it does:**
- Add a task with a title, priority (High / Medium / Low), and due date
- Mark a task as completed
- Delete a task
- View all tasks — with status and priority displayed clearly
- Filter to show only pending or only completed tasks

**OOP concepts used:**
- `Task` class with attributes for title, priority, due date, and a completion status flag
- `TodoList` class managing the collection of task objects
- Encapsulated status transitions — completion toggled only through a `complete()` method, not by setting the attribute directly
- `__str__()` on `Task` for clean single-line display in the list view

**Run it:**
```bash
python todo_list/main.py
```

**Sample interaction:**
```
1. Add Task
2. Mark Task as Done
3. Delete Task
4. View All Tasks
5. View Pending Tasks
6. Exit

> 4
📋 All Tasks:
  [1] ✅ Buy groceries         — Low    — Due: 25 May
  [2] ⏳ Finish Python module  — High   — Due: 28 May
  [3] ⏳ Call the bank         — Medium — Due: 30 May
```

---

## 🚀 Running Any Project

All projects are self-contained. Navigate to the `projects/` folder and run directly:

```bash
cd projects

python chatbot/main.py
python expense_tracker/main.py
python library_management/main.py
python password_manager/main.py
python student_management/main.py
python todo_list/main.py
```

No third-party libraries required — every project runs on Python's standard library.

---

## 💡 What These Projects Teach You

| Project | Primary OOP Focus |
|---|---|
| Chatbot | Classes, methods, encapsulation of logic |
| Expense Tracker | Object collections, `__str__()`, encapsulation |
| Library Management | Multiple interacting classes, object relationships |
| Password Manager | Private attributes, controlled access, encapsulation |
| Student Management | `@property`, polymorphism, object sorting |
| To-Do List | State management, encapsulation, filtering |

The jump from writing single-class examples to building multi-class applications that interact with each other is the most important step in learning OOP. These projects are that step.
