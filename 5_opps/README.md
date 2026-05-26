# 📁 5 — Object-Oriented Programming

Object-Oriented Programming (OOP) is a completely different way of thinking about code. Instead of writing a sequence of instructions, you model your program as a collection of **objects** — each with its own data and behaviour. Every major Python framework, library, and real-world codebase is built on OOP. This module covers all four pillars of OOP and wraps up with six fully working projects that put everything together.

---

## 📂 Module Structure

```
5_oops/
│
├── 0_classes_objects.py
├── 1_inheritance.py
├── 2_encapsulation.py
├── 3_polymorphism.py
│
└── projects/
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

## 📄 File Breakdown

### `0_classes_objects.py` — Classes & Objects

A class is a blueprint. An object is what you build from it. This file starts from scratch and establishes the foundation that everything else in this module builds on.

**Concepts covered:**
- Defining a class with `class`
- The `__init__()` constructor — setting up an object's initial state
- Instance attributes — data that belongs to each individual object
- Class attributes — data shared across all objects of a class
- Instance methods — functions that belong to an object
- The `self` parameter — what it is and why every method needs it
- Creating multiple objects from the same class
- Magic (dunder) methods: `__str__()`, `__repr__()`, `__len__()`

**Practical Examples:**
- **`BankAccount` class** — models a bank account with attributes for owner and balance, and methods for deposit, withdrawal, and balance display; demonstrates creating two separate accounts that don't interfere with each other
- **`Student` class** — stores name, roll number, and a list of grades; includes methods to add a grade, compute the average, and print a formatted report card using `__str__()`
- **`Car` class** — tracks make, model, year, and mileage; includes a `drive(km)` method that updates mileage and a class attribute counting how many `Car` objects have been created

---

### `1_inheritance.py` — Inheritance

Inheritance lets one class acquire the attributes and methods of another — so you can build specialised classes without rewriting shared logic.

**Concepts covered:**
- Defining a child class: `class Child(Parent):`
- Inheriting attributes and methods automatically
- Overriding a parent method in a child class
- `super()` — calling the parent's `__init__()` or methods from the child
- Multi-level inheritance (A → B → C)
- Checking relationships with `isinstance()` and `issubclass()`
- When to use inheritance vs composition

**Practical Examples:**
- **Animal hierarchy** — a base `Animal` class with `name` and `sound`; `Dog`, `Cat`, and `Bird` subclasses each override a `speak()` method and add their own unique behaviours (`fetch()`, `purr()`, `fly()`)
- **Employee payroll system** — a base `Employee` class with name and base salary; `Manager` and `Developer` subclasses that override `calculate_pay()` with their own bonus logic and add role-specific attributes
- **Shape calculator** — a base `Shape` class with a placeholder `area()` method; `Circle`, `Rectangle`, and `Triangle` subclasses that each override `area()` with the correct formula

---

### `2_encapsulation.py` — Encapsulation

Encapsulation is about protecting an object's internal data — exposing only what's necessary and keeping the rest hidden from the outside world.

**Concepts covered:**
- Public, protected (`_`), and private (`__`) attributes — naming conventions and what they signal
- Why direct attribute access can be dangerous
- Getter and setter methods — controlling how data is read and changed
- The `@property` decorator — making getters feel like attributes
- `@attribute.setter` — adding validation logic when a value is set
- Read-only properties — defining a getter with no setter

**Practical Examples:**
- **`Person` class with age validation** — age is a private attribute; the setter rejects negative values or ages above 150 before assigning, preventing invalid state
- **`BankAccount` with protected balance** — the balance is private and can only be changed through `deposit()` and `withdraw()` methods that enforce business rules (no overdraft, positive amounts only)
- **`Temperature` class** — stores temperature internally in Celsius; exposes `@property` values for both `fahrenheit` and `kelvin`, computed on the fly without storing them separately

---

### `3_polymorphism.py` — Polymorphism

Polymorphism means many forms. It's the ability to call the same method on different objects and get behaviour that's appropriate for each one — without caring about which specific type you're dealing with.

**Concepts covered:**
- Method overriding — the same method name, different behaviour per class
- Duck typing — "if it walks like a duck and quacks like a duck, it's a duck"
- Polymorphism with functions — writing a function that works on any object with the right method
- Operator overloading with dunder methods: `__add__()`, `__eq__()`, `__lt__()`, `__len__()`
- Abstract base classes with `ABC` and `@abstractmethod` — enforcing that subclasses implement required methods

**Practical Examples:**
- **Payment processor** — a `Payment` base class with a `process()` method; `CreditCard`, `PayPal`, and `BankTransfer` classes each implement `process()` differently; a single `checkout(payment)` function works with all three without any `if/else` type checking
- **Shape area calculator** — a standalone `print_area(shape)` function that calls `shape.area()` on any shape object passed to it, demonstrating duck typing in action
- **`Vector` class with operator overloading** — overloads `__add__`, `__sub__`, `__mul__`, and `__eq__` so that two `Vector` objects can be added, subtracted, and compared using natural Python operators (`v1 + v2`, `v1 == v2`)

---

## 🗂️ Projects

Six complete OOP projects that each use classes, objects, and at least one of the four OOP pillars. Every project runs from its own `main.py` and is self-contained.

---

### 💬 Chatbot

A rule-based conversational chatbot that responds to user messages using pattern matching and predefined response logic.

**OOP concepts applied:** Classes and objects, encapsulation of response logic, methods for greeting, farewell, and fallback responses.

**How to run:**
```bash
python projects/chatbot/main.py
```

---

### 💸 Expense Tracker

Track your daily expenses by category, view summaries, and manage your spending — all persisted across sessions.

**OOP concepts applied:** `Expense` class with attributes for amount, category, and date; `ExpenseTracker` class managing a list of expense objects; encapsulated add/remove/filter logic; summary reporting by category.

**How to run:**
```bash
python projects/expense_tracker/main.py
```

---

### 📚 Library Management System

A complete library system for managing books, members, and borrowing records.

**OOP concepts applied:** Separate `Book`, `Member`, and `Library` classes; inheritance for different member types (e.g., student vs staff); encapsulated borrowing rules; methods for issuing, returning, and listing books.

**How to run:**
```bash
python projects/library_management/main.py
```

---

### 🔐 Password Manager

Securely store, retrieve, and manage passwords for different services — with basic encryption applied to stored values.

**OOP concepts applied:** `PasswordEntry` class encapsulating service, username, and password; `PasswordManager` class with private storage and methods for add, retrieve, update, and delete; encapsulation ensuring passwords aren't directly accessible.

**How to run:**
```bash
python projects/password_manager/main.py
```

---

### 🎓 Student Management System

A full student record system — add students, assign grades, compute averages, and generate reports.

**OOP concepts applied:** `Student` class with encapsulated grade data; `Classroom` class managing a collection of student objects; polymorphic `__str__()` for formatted output; methods for ranking students and computing class averages.

**How to run:**
```bash
python projects/student_management/main.py
```

---

### ✅ To-Do List

A task management app where you can add, complete, delete, and filter tasks — with priorities and due dates.

**OOP concepts applied:** `Task` class with attributes for title, priority, due date, and status; `TodoList` class managing all tasks; encapsulated status transitions (pending → done); filtering methods for completed vs pending tasks.

**How to run:**
```bash
python projects/todo_list/main.py
```

---

## 🚀 How to Run

```bash
cd 5_oops

# Run any concept file
python 0_classes_objects.py
python 1_inheritance.py
python 2_encapsulation.py
python 3_polymorphism.py

# Run any project
python projects/expense_tracker/main.py
python projects/library_management/main.py
```

---

## 💡 Key Takeaways from This Module

- A **class** is the blueprint; an **object** is the instance — you can create as many objects as you need from the same class
- Always use `super().__init__()` in a child class to make sure the parent is properly set up before adding the child's own attributes
- Prefix private attributes with `__` and use `@property` to expose them safely — this is encapsulation done the Python way
- Polymorphism means writing functions that work on *behaviour*, not *type* — if the object has the right method, the function doesn't care what class it belongs to
- The four pillars work together — the projects in this module use all of them simultaneously, which is exactly how real-world code works

---

## ➡️ What's Next

OOP is the last core concept. Time to put everything together and tackle real algorithmic challenges:

**`6_problem_solving/`** — Algorithms, patterns, and coding challenges

```bash
cd ../6_problem_solving
python main.py
```
