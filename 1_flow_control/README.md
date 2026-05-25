# 📁 1 — Flow Control

Programs rarely run in a straight line. Flow control is what gives your code the ability to make decisions and repeat actions — the two most fundamental things any program does. This module covers conditionals and both types of loops Python offers.

---

## 📂 Files in This Module

| File | Topic |
|---|---|
| `0_if_statements.py` | Conditional logic and decision making |
| `1_loops.py` | Iterating with `for` loops |
| `2_while_loops.py` | Repeating with `while` loops |

---

## 📄 File Breakdown

### `0_if_statements.py` — If Statements

Code that always does the same thing regardless of the situation isn't very useful. `if` statements let your program react differently based on conditions.

**Concepts covered:**
- `if`, `elif`, `else` structure
- Comparison operators: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Logical operators: `and`, `or`, `not`
- Nested `if` statements
- Ternary (one-line) conditionals: `value if condition else other`
- Truthy and falsy values in conditions

**Practical Examples:**
- **Grade classifier** — takes a student's score and prints the corresponding letter grade (A, B, C, D, F)
- **Login system** — checks a username and password, grants or denies access with appropriate messages
- **Discount calculator** — applies different discount tiers based on the purchase amount (e.g., 5% over $50, 15% over $100)
- **Leap year checker** — determines whether a given year is a leap year using nested conditions
- **Traffic light simulator** — prints the action to take (stop / get ready / go) based on the light color

---

### `1_loops.py` — For Loops

When you need to do something repeatedly for every item in a sequence, `for` loops are the tool. They're clean, readable, and deeply integrated into Python's design.

**Concepts covered:**
- `for` loop syntax and iteration over lists, strings, and ranges
- `range()` — `range(n)`, `range(start, stop)`, `range(start, stop, step)`
- `enumerate()` for index + value together
- `zip()` for looping over two sequences in parallel
- `break` — exit the loop early
- `continue` — skip to the next iteration
- `else` on a `for` loop — runs only if the loop wasn't broken out of
- Nested `for` loops

**Practical Examples:**
- **Multiplication table printer** — prints a formatted times table for any number using `range()`
- **Shopping cart total** — iterates over a list of item prices and accumulates the total
- **Student grade report** — uses `enumerate()` to print a numbered list of students with their grades
- **Password validator** — loops through characters in a string to check for digits, uppercase, and special characters
- **Pattern printer** — uses nested loops to print triangle and pyramid shapes

---

### `2_while_loops.py` — While Loops

`while` loops repeat as long as a condition remains true. They're the right choice when you don't know in advance how many times something needs to run.

**Concepts covered:**
- `while` loop syntax and condition checking
- Infinite loops and how to avoid them
- Using a flag variable to control the loop
- `break` and `continue` inside `while` loops
- `else` on a `while` loop
- Counting and accumulating with `while`
- `while` vs `for` — when to choose which

**Practical Examples:**
- **Number guessing game** — generates a random number, keeps prompting the user until they guess correctly, and counts the attempts
- **ATM simulator** — loops through a menu (check balance, deposit, withdraw, exit) until the user chooses to quit
- **Input validator** — keeps asking for a positive number until the user actually enters one
- **Countdown timer** — counts down from a user-given number to zero, printing each value
- **Digit sum calculator** — extracts and sums digits from a number one by one using `%` and `//` until none remain

---

## 🚀 How to Run

```bash
cd 1_flow_control
python 0_if_statements.py
python 1_loops.py
python 2_while_loops.py
```

Some examples in this module use `input()`, so be ready to type values when prompted.

---

## 💡 Key Takeaways from This Module

- `if/elif/else` chains are checked top to bottom — the first `True` condition wins and the rest are skipped
- `for` loops are for **known sequences**; `while` loops are for **unknown repetitions**
- Always make sure a `while` loop has a way to become `False` — otherwise it runs forever
- `break` exits the loop immediately; `continue` skips just the current iteration
- `range(start, stop, step)` is more powerful than it looks — a negative step lets you count backwards

---

## ➡️ What's Next

With flow control under your belt, you're ready to start organizing code into reusable blocks:

**`2_data_structure/`** — Writing clean, reusable functions

```bash
cd ../2_data_structure
```
