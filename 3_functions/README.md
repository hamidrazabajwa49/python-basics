# 📁 3 — Functions

Functions are the backbone of clean, reusable code. Instead of writing the same logic over and over, you wrap it in a function, give it a name, and call it whenever you need it. This module covers how to define functions, work with all kinds of parameters, and write compact anonymous functions using `lambda`.

---

## 📂 Files in This Module

| File | Topic |
|---|---|
| `0_basic_functions.py` | Defining and calling functions, return values, scope |
| `1_parameters_arguments.py` | All the ways to pass data into a function |
| `2_lambda_functions.py` | Anonymous functions and functional programming tools |

---

## 📄 File Breakdown

### `0_basic_functions.py` — Basic Functions

Everything starts here — how to define a function, how to call it, how to get a value back out of it, and how Python decides what variables a function can see.

**Concepts covered:**
- Defining functions with `def`
- Calling a function and reusing it
- The `return` statement — returning single and multiple values
- `return` vs `print()` — and why the difference matters
- Docstrings — documenting what a function does with `""" """`
- Scope — local vs global variables
- The `global` keyword and why to avoid overusing it
- Default return value (`None`) when no `return` is written

**Practical Examples:**
- **Area calculator** — separate functions for the area of a circle, rectangle, and triangle; each takes dimensions and returns the result cleanly
- **Temperature converter** — `celsius_to_fahrenheit()` and `fahrenheit_to_celsius()` functions that return converted values, demonstrated with a range of temperatures
- **Even/odd checker** — a reusable `is_even(n)` function that returns a boolean, called in a loop over a list of numbers
- **Simple invoice generator** — functions for calculating subtotal, applying tax, and applying a discount, chained together to produce a final bill
- **Min/Max without built-ins** — a function that manually finds the minimum and maximum of a list and returns both values as a tuple

---

### `1_parameters_arguments.py` — Parameters & Arguments

Python gives you a lot of flexibility in how you pass data into functions. This file covers every kind — from the basics to `*args` and `**kwargs`.

**Concepts covered:**
- Positional arguments — order matters
- Keyword arguments — named, order doesn't matter
- Default parameter values — making arguments optional
- Mixing positional, keyword, and default arguments (and the rules for ordering them)
- `*args` — accepting any number of positional arguments as a tuple
- `**kwargs` — accepting any number of keyword arguments as a dictionary
- Combining `*args` and `**kwargs` in one function
- Passing a list or dict to a function with `*` and `**` unpacking

**Practical Examples:**
- **Flexible greeter** — `greet(name, greeting="Hello")` demonstrates default parameters; called with and without the optional argument
- **Shopping bill calculator** — uses `*args` to accept any number of item prices and returns the total, showing how the function works with 2 items or 20
- **User profile builder** — uses `**kwargs` to accept any combination of profile fields (name, age, city, email) and prints a formatted profile card
- **Math operations dispatcher** — a single function that takes an operation name and `*args`, then routes to addition, multiplication, or average accordingly
- **Order summary printer** — combines `*args` for item names and `**kwargs` for order metadata (customer, address, paid) in one unified function call

---

### `2_lambda_functions.py` — Lambda Functions

Lambda functions are small, anonymous functions written in a single line. On their own they're handy; paired with `map()`, `filter()`, and `sorted()`, they become very powerful.

**Concepts covered:**
- Lambda syntax: `lambda arguments: expression`
- How a lambda is equivalent to a one-line `def` function
- Assigning lambdas to variables
- Lambdas as arguments passed directly into other functions
- `map()` — applying a function to every item in an iterable
- `filter()` — keeping only items that pass a condition
- `sorted()` with a `key=` lambda — custom sort logic
- When to use a lambda vs a named function (readability rule)

**Practical Examples:**
- **Price tax applier** — uses `map()` with a lambda to apply an 8% tax to every price in a list in one line
- **Adult filter** — uses `filter()` with a lambda to extract only users aged 18 and above from a list of dictionaries
- **Student leaderboard** — uses `sorted()` with `key=lambda s: s["score"]` to rank students by score in descending order
- **String length sorter** — sorts a list of words by their length using a lambda as the sort key, demonstrating custom sorting without a named function
- **Discount pipeline** — chains `map()` and `filter()` together: first filters products above a price threshold, then applies a discount to each — all without defining a single named function

---

## 🚀 How to Run

```bash
cd 3_functions
python 0_basic_functions.py
python 1_parameters_arguments.py
python 2_lambda_functions.py
```

No external libraries needed — everything here is pure Python.

---

## 💡 Key Takeaways from This Module

- Always `return` a value from a function rather than printing inside it — it makes the function reusable and testable
- Write a docstring for every function — one line is enough, but future you will thank present you
- Default parameters make functions flexible; just remember they must come after non-default parameters
- `*args` collects extra positional arguments into a **tuple**; `**kwargs` collects extra keyword arguments into a **dict**
- Use a `lambda` when the logic is a single expression and you're passing it directly into another function — if it needs a name or a second line, write a proper `def` instead

---

## ➡️ What's Next

Functions organize your logic — classes organize your entire program. Time to think in objects:

**`4_oops/`** — Object-Oriented Programming in Python

```bash
cd ../4_oops
python 0_classes_objects.py
```
