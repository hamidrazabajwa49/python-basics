# 📁 2 — Data Structures

Data structures are how you organize and store information in your programs. Python has four powerful built-in data structures — each with its own strengths, use cases, and quirks. Mastering them is the single biggest step you can take toward writing real Python.

---


## 📂 Module Structure

```
2_data_structures/
│
├── 0_lists/
│   ├── basics.py
│   ├── methods.py
│   ├── comprehensions.py
│   └── exercises/
│
├── 1_tuples/
│   ├── basics.py
│   └── exercises/
│
├── 2_dictionaries/
│   ├── basics.py
│   ├── comprehensions.py
│   └── exercises/
│
└── 3_strings/
    ├── basics.py
    └── exercises/
```

---

## 📁 0 — Lists

> An ordered, mutable collection. The most used data structure in Python.

| File | Topic |
|---|---|
| `basics.py` | Creating lists, indexing, slicing, nesting |
| `methods.py` | Built-in list methods and their behaviours |
| `comprehensions.py` | List comprehensions and filtered comprehensions |
| `exercises/` | 10+ practice problems |

### `basics.py`

The foundation of working with lists — how to create them, access elements, slice them, and nest them inside each other.

**Concepts covered:**
- Creating lists with mixed and same-type elements
- Positive and negative indexing
- Slicing: `list[start:stop:step]`
- Nested lists and accessing inner elements
- Checking membership with `in`
- Getting the length with `len()`

**Practical Examples:**
- **Student roster** — stores a class list and retrieves students by position and slice
- **Weekly planner** — a nested list representing days and their scheduled tasks

---

### `methods.py`

Python lists come packed with built-in methods. This file goes through all of them with clear examples of when and why to use each one.

**Concepts covered:**
- Adding elements: `append()`, `insert()`, `extend()`
- Removing elements: `remove()`, `pop()`, `clear()`
- Searching: `index()`, `count()`
- Reordering: `sort()`, `reverse()`, `sorted()`
- Copying: `copy()` vs direct assignment — and why it matters

**Practical Examples:**
- **Task manager** — adds, removes, and reorders tasks in a to-do list using various methods
- **Leaderboard sorter** — takes a list of scores and sorts them in descending order to display a ranked board

---

### `comprehensions.py`

List comprehensions are one of Python's most loved features — a concise way to build lists that would otherwise need a loop.

**Concepts covered:**
- Basic comprehension syntax: `[expression for item in iterable]`
- Filtered comprehensions: `[expression for item in iterable if condition]`
- Nested comprehensions
- When to use a comprehension vs a regular loop (readability trade-off)

**Practical Examples:**
- **Even number extractor** — builds a list of even numbers from a range in one line
- **Grade filter** — extracts only passing scores from a class result list
- **Matrix transposer** — uses nested comprehensions to transpose a 2D list (rows become columns)

---

### `exercises/`

10+ practice problems covering indexing, slicing, list manipulation, and algorithmic thinking with lists — from summing elements to finding pairs with a target sum.

---

## 📁 1 — Tuples

> An ordered, immutable collection. Fast, safe, and perfect for fixed data.

| File | Topic |
|---|---|
| `basics.py` | Creating, accessing, and unpacking tuples |
| `exercises/` | 10+ practice problems |

### `basics.py`

Tuples look like lists but can't be changed after creation. That immutability isn't a limitation — it's a feature that makes your data safer and your code more predictable.

**Concepts covered:**
- Creating tuples (including single-element tuples with a trailing comma)
- Indexing and slicing — same as lists
- Tuple unpacking and extended unpacking with `*`
- Swapping variables using tuple unpacking
- Returning multiple values from a function using tuples
- Named tuples with `collections.namedtuple`
- Tuples vs lists — when to choose which

**Practical Examples:**
- **Coordinate system** — represents (x, y) and (x, y, z) points as tuples and performs distance calculations
- **Function returning multiple values** — a `min_max()` function that returns both the minimum and maximum of a list as a tuple
- **RGB colour store** — stores colour values as immutable tuples and unpacks them for display

---

### `exercises/`

10+ problems on tuple creation, unpacking, working with `namedtuple`, and using tuples as dictionary keys.

---

## 📁 2 — Dictionaries

> An unordered collection of key-value pairs. The go-to structure for labelled data.

| File | Topic |
|---|---|
| `basics.py` | Creating, reading, updating, and deleting from dicts |
| `comprehensions.py` | Dictionary comprehensions |
| `exercises/` | 10+ practice problems |

### `basics.py`

Dictionaries map keys to values — think of them as a lookup table. Any time your data has labels or names attached to it, a dictionary is probably the right tool.

**Concepts covered:**
- Creating dictionaries with `{}` and `dict()`
- Accessing values: `dict[key]` vs `.get(key, default)`
- Adding and updating key-value pairs
- Deleting entries: `del`, `.pop()`, `.popitem()`
- Looping with `.keys()`, `.values()`, `.items()`
- Checking key existence with `in`
- Nested dictionaries
- `.update()` and merging dicts with `**`

**Practical Examples:**
- **Student record system** — stores and retrieves student data (name, age, grades) with full CRUD operations
- **Word frequency counter** — counts how many times each word appears in a sentence using a dictionary
- **Phone book** — looks up, adds, and removes contacts by name with `.get()` for safe access

---

### `comprehensions.py`

Dictionary comprehensions let you build dictionaries from iterables in a single clean expression.

**Concepts covered:**
- Basic dict comprehension: `{key: value for item in iterable}`
- Filtered dict comprehensions with conditions
- Inverting a dictionary (swapping keys and values)
- Building a dict from two parallel lists using `zip()`

**Practical Examples:**
- **Square mapper** — builds `{1: 1, 2: 4, 3: 9, ...}` from a range in one line
- **Passing students filter** — builds a dict of only students who scored above 50 from a full results dictionary
- **Inverted index** — flips a `{name: id}` dictionary into `{id: name}` using a comprehension

---

### `exercises/`

10+ problems covering dictionary CRUD, nested dicts, frequency counting, grouping data, and merging dictionaries.

---

## 📁 3 — Strings

> An immutable sequence of characters. More powerful than they first appear.

| File | Topic |
|---|---|
| `basics.py` | String creation, indexing, slicing, methods, and formatting |
| `exercises/` | 10+ practice problems |

### `basics.py`

Strings are everywhere — user input, file contents, API responses, display output. Python gives you a rich set of tools to work with them.

**Concepts covered:**
- String creation: single, double, and triple quotes
- Indexing and slicing strings (same rules as lists)
- Immutability — why you can't change a character in place
- Essential methods: `upper()`, `lower()`, `strip()`, `replace()`, `split()`, `join()`, `find()`, `count()`, `startswith()`, `endswith()`
- String formatting: `%`, `.format()`, and f-strings (preferred)
- Checking string content: `isdigit()`, `isalpha()`, `isalnum()`
- Raw strings with `r""` and escape characters

**Practical Examples:**
- **Username formatter** — strips whitespace, lowercases, and validates a username entered by the user
- **CSV row parser** — splits a comma-separated string into a list of cleaned values using `split()` and `strip()`
- **Simple cipher** — replaces each letter in a message using `replace()` to encode a string

---

### `exercises/`

10+ problems on string manipulation, palindrome checking, anagram detection, character counting, and formatting output.

---

## 🚀 How to Run

```bash
cd 2_data_structures

# Run any concept file
python 0_lists/basics.py
python 1_tuples/basics.py
python 2_dictionaries/basics.py
python 3_strings/basics.py

# Run any exercise
python 0_lists/exercises/01_sum_elements.py
```

---

## 💡 Key Takeaways from This Module

- **Lists** — ordered, mutable, for sequences that change
- **Tuples** — ordered, immutable, for fixed data and multiple return values
- **Dictionaries** — key-value pairs, for labelled and structured data
- **Strings** — immutable sequences, with a rich set of built-in methods
- Comprehensions work for both lists and dictionaries — prefer them over loops when the intent stays readable
- `.get(key, default)` is almost always better than `dict[key]` — it won't crash on missing keys

---

## ➡️ What's Next

You now have the tools to store and organize data. Next up, learn how to package logic into reusable blocks:

**`3_functions/`** — Writing clean, reusable, and efficient functions

```bash
cd ../3_functions
python 0_basics.py
```
