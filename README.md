# 🐍 Python Basics

A structured, beginner-to-intermediate Python learning repository covering core concepts from the ground up — with practical real-world examples and 10+ hands-on practice problems in every module.

---

## 📚 Table of Contents

- [About This Repository](#about-this-repository)
- [Repository Structure](#repository-structure)
- [Modules Overview](#modules-overview)
  - [01 — Lists](#01--lists)
  - [02 — Dictionaries & Sets](#02--dictionaries--sets)
  - [03 — Tuples & Strings](#03--tuples--strings)
  - [04 — Flow Control](#04--flow-control)
  - [05 — Functions](#05--functions)
  - [06 — File Handling](#06--file-handling)
  - [07 — Object-Oriented Programming](#07--object-oriented-programming)
  - [08 — Problem Solving](#08--problem-solving)
- [How to Use This Repo](#how-to-use-this-repo)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Practice Problem Format](#practice-problem-format)
- [Contributing](#contributing)

---

## About This Repository

This repository is a self-contained Python learning resource built around the philosophy of **learn → practice → apply**. Every module includes:

- **Concept files** — clean, well-commented code explaining the fundamentals
- **Practical examples** — real-world use cases that show *why* a concept matters
- **10+ exercises** — graded practice problems with clear problem statements

Whether you're picking up Python for the first time or solidifying your foundations, this repo gives you a structured path to follow at your own pace.

---

## Repository Structure

```
python-basics/
│
├── 01_lists/
│   ├── basics.py               # Core list concepts
│   ├── methods.py              # Built-in list methods
│   ├── comprehensions.py       # List comprehensions
│   └── exercises/
│       ├── 00_list_reference.py
│       ├── 01_sum_elements.py
│       ├── 02_remove_duplicates.py
│       ├── 03_reverse_list.py
│       ├── 04_min_max.py
│       ├── 05_count_occurrences.py
│       ├── 07_find_pairs_with_sum.py
│       ├── 08_flatten_nested_list.py
│       ├── 09_cumulative_sum.py
│       ├── 10_rotate_list.py
│       └── 11_product_except_self.py
│
├── 02_data_structures/
│   ├── dictionaries.py
│   ├── sets.py
│   ├── tuples.py
│   └── exercises/
│
├── 03_flow_control/
│   ├── conditionals.py
│   ├── loops.py
│   ├── comprehensions.py
│   └── exercises/
│
├── 04_functions/
│   ├── basics.py
│   ├── args_kwargs.py
│   ├── lambda_map_filter.py
│   ├── recursion.py
│   └── exercises/
│
├── 05_file_handling/
│   ├── reading_files.py
│   ├── writing_files.py
│   ├── working_with_csv.py
│   ├── working_with_json.py
│   └── exercises/
│
├── 06_oops/
│   ├── classes_objects.py
│   ├── inheritance.py
│   ├── encapsulation.py
│   ├── polymorphism.py
│   └── exercises/
│
├── 07_problem_solving/
│   ├── arrays_strings.py
│   ├── searching_sorting.py
│   ├── recursion_problems.py
│   └── challenges/
│
└── README.md
```

---

## Modules Overview

### 01 — Lists

> **Files:** `basics.py` · `methods.py` · `comprehensions.py` · `exercises/`

Lists are Python's most versatile data structure. This module starts from the very basics and builds up to advanced patterns.

| File | What You'll Learn |
|---|---|
| `basics.py` | Creating lists, indexing, slicing, nested lists |
| `methods.py` | `append`, `extend`, `insert`, `remove`, `sort`, `pop`, and more |
| `comprehensions.py` | List comprehensions, filtered comprehensions, nested comprehensions |

**Practical Example:** Building a shopping cart system using list operations.

**Exercises include:** Sum of elements, removing duplicates, reversing a list, finding min/max without built-ins, counting occurrences, finding pairs with a target sum, flattening nested lists, cumulative sum, rotating a list, and product-except-self.

---

### 02 — Dictionaries & Sets

> Covers Python's key-value store and unordered unique collections.

| Concept | Topics |
|---|---|
| Dictionaries | CRUD operations, nested dicts, `.get()`, `.items()`, `.keys()`, dict comprehensions |
| Sets | Set creation, union, intersection, difference, symmetric difference |

**Practical Example:** Building a word frequency counter; managing student grade records.

---

### 03 — Tuples & Strings

> Immutable sequences and Python's powerful string toolkit.

| Concept | Topics |
|---|---|
| Tuples | Packing/unpacking, named tuples, use cases vs lists |
| Strings | Slicing, formatting (`f-strings`), common methods, regex basics |

**Practical Example:** Parsing and formatting user input; coordinate systems with tuples.

---

### 04 — Flow Control

> Decision-making and loops — the building blocks of any program.

| File | What You'll Learn |
|---|---|
| `conditionals.py` | `if/elif/else`, ternary expressions, truthy/falsy values |
| `loops.py` | `for`, `while`, `break`, `continue`, `else` on loops |
| `comprehensions.py` | Generator expressions, conditional comprehensions |

**Practical Example:** Building a number guessing game; FizzBuzz variations; pattern printing.

---

### 05 — Functions

> Writing reusable, clean, and efficient code.

| File | What You'll Learn |
|---|---|
| `basics.py` | Defining functions, return values, scope, docstrings |
| `args_kwargs.py` | `*args`, `**kwargs`, positional vs keyword arguments |
| `lambda_map_filter.py` | Anonymous functions, functional programming patterns |
| `recursion.py` | Base cases, recursive thinking, memoization intro |

**Practical Example:** A decorator for timing function execution; recursive directory traversal.

---

### 06 — File Handling

> Reading from and writing to files — an essential real-world skill.

| File | What You'll Learn |
|---|---|
| `reading_files.py` | `open()`, context managers, reading line by line |
| `writing_files.py` | Writing, appending, file modes |
| `working_with_csv.py` | `csv` module, reading/writing tabular data |
| `working_with_json.py` | `json` module, serialization and deserialization |

**Practical Example:** Building a simple contact book saved to a JSON file; reading and summarizing a CSV dataset.

---

### 07 — Object-Oriented Programming

> Modeling real-world problems with classes and objects.

| File | What You'll Learn |
|---|---|
| `classes_objects.py` | Class definition, `__init__`, instance vs class attributes |
| `inheritance.py` | Parent/child classes, `super()`, method overriding |
| `encapsulation.py` | Private attributes, getters/setters, `@property` |
| `polymorphism.py` | Duck typing, method overriding, `__str__`, `__repr__` |

**Practical Example:** Designing a `BankAccount` class hierarchy; modeling a library system with `Book`, `Member`, and `Library` classes.

---

### 08 — Problem Solving

> Putting it all together — algorithmic thinking and coding challenges.

| File | What You'll Learn |
|---|---|
| `arrays_strings.py` | Two-pointer technique, sliding window, string manipulation |
| `searching_sorting.py` | Linear search, binary search, bubble/insertion sort |
| `recursion_problems.py` | Fibonacci, factorial, tower of Hanoi, tree traversal |

**Challenges include:** Anagram checker, palindrome validator, balanced parentheses, matrix rotation, and more.

---

## How to Use This Repo

**If you're a beginner**, work through the modules in order (01 → 08). Each module builds on the previous one.

**If you want to practice**, jump straight to the `exercises/` folder in any module. Each file has a problem statement in the comments at the top.

**If you're reviewing**, the concept files (`basics.py`, `methods.py`, etc.) serve as quick references — everything is commented and clearly organized.

---

## Prerequisites

- Python 3.8 or higher
- No third-party libraries required — this repo uses the Python standard library only

Check your Python version:
```bash
python --version
```

---

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/python-basics.git
   cd python-basics
   ```

2. **Navigate to a module**
   ```bash
   cd 01_lists
   ```

3. **Run any file**
   ```bash
   python basics.py
   python exercises/01_sum_elements.py
   ```

4. **Work through the exercises** — open an exercise file, read the problem statement at the top, and write your solution below the prompt.

---

## Practice Problem Format

Every exercise file follows this consistent structure:

```python
# ============================================================
# Exercise XX: Problem Title
# ============================================================
# Problem:
#   Clear description of what needs to be done.
#
# Example:
#   Input:  [1, 2, 3, 4, 5]
#   Output: 15
#
# Constraints:
#   - Any relevant constraints or edge cases
# ============================================================

def solve():
    # Your solution here
    pass

# Practical Use Case:
# Brief note on where this pattern appears in real software.
```

---

## Contributing

Found a bug, want to add a solution, or have a better example? Contributions are welcome!

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-improvement`)
3. Commit your changes (`git commit -m "Add: better example for recursion"`)
4. Push to your branch (`git push origin feature/your-improvement`)
5. Open a Pull Request

---

<div align="center">

Made with ❤️ for anyone learning Python from scratch.

**Happy Coding! 🚀**

</div>
