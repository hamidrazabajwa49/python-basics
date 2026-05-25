# 📁 0 — Basics

The starting point of your Python journey. This module covers the absolute fundamentals — from printing your first line to handling user input and converting between data types. Every concept here will be used in every module that follows.

---

## 📂 Files in This Module

| File | Topic |
|---|---|
| `0_hello_world.py` | Your first Python program |
| `1_variables_and_types.py` | Variables, data types, and type checking |
| `2_arithmetic_operations.py` | Math operators and expressions |
| `3_user_input.py` | Reading input from the user |
| `4_type_conversion.py` | Converting between data types |

---

## 📄 File Breakdown

### `0_hello_world.py` — Hello, World!

The classic starting point for any programming language. Covers how Python executes code top-to-bottom and how to display output to the terminal.

**Concepts covered:**
- `print()` function
- Strings and string literals
- Comments (`#` single-line, `""" """` multi-line)
- Running a Python script

**Practical Example:** Displaying a welcome message for a CLI application.

**Exercises include:**
1. Print your name and city on separate lines
2. Print a formatted address block
3. Print a simple ASCII art shape
4. Display a welcome banner with your name
5. Print the lyrics of a short rhyme using multiple `print()` calls
6. Print numbers 1 through 10 each on its own line (without loops)
7. Print a multiplication table row (e.g., table of 5)
8. Display a simple receipt with item names and prices
9. Print a countdown from 10 to 1
10. Build a "business card" in the terminal with name, role, and contact info

---

### `1_variables_and_types.py` — Variables & Data Types

Variables are containers for storing data. Python is dynamically typed, meaning you don't need to declare a type — Python figures it out automatically.

**Concepts covered:**
- Variable declaration and assignment
- Core data types: `int`, `float`, `str`, `bool`, `NoneType`
- The `type()` function
- Variable naming conventions (snake_case)
- Multiple assignment and swapping variables

**Practical Example:** Storing and displaying a user's profile — name, age, height, and membership status.

**Exercises include:**
1. Declare variables for your personal info and print them
2. Use `type()` to check and print the type of 5 different values
3. Swap the values of two variables without a third variable
4. Predict the type of expressions like `True + 1` or `"3" * 3`
5. Store `None` in a variable and explain when you'd use it
6. Create variables for a product (name, price, in_stock) and display them
7. Demonstrate that variable names are case-sensitive
8. Assign the same value to three variables in a single line
9. Calculate your age in days using a variable for your age in years
10. Build a "student record" with name, grade, GPA, and enrolled status

---

### `2_arithmetic_operations.py` — Arithmetic Operations

Python supports all standard math operations and a few you might not expect. This file explores how Python handles numbers under the hood.

**Concepts covered:**
- Basic operators: `+`, `-`, `*`, `/`
- Integer division `//` and modulo `%`
- Exponentiation `**`
- Operator precedence (BODMAS/PEMDAS)
- Augmented assignment: `+=`, `-=`, `*=`, `/=`
- The `math` module — `math.sqrt()`, `math.ceil()`, `math.floor()`

**Practical Example:** Building a simple invoice calculator — subtotal, tax, discount, and final total.

**Exercises include:**
1. Calculate the area and perimeter of a rectangle
2. Convert temperature from Celsius to Fahrenheit (and back)
3. Find the remainder when dividing a number — use case: checking even/odd
4. Calculate compound interest given principal, rate, and time
5. Find the hypotenuse of a right triangle using `math.sqrt()`
6. Compute the average of 5 hardcoded numbers
7. Use `//` and `%` together to convert total seconds into hours, minutes, seconds
8. Calculate the power bill: units used × rate per unit + fixed charge
9. Round a float to 2 decimal places using `round()` and `math.ceil()`
10. Compute BMI given weight (kg) and height (m): `weight / height ** 2`

---

### `3_user_input.py` — User Input

Real programs interact with users. This file covers how to read input from the terminal and use it in your program.

**Concepts covered:**
- The `input()` function
- Why `input()` always returns a string
- Prompting the user with a message
- Storing and reusing input in variables
- Combining `input()` with `print()` for interactive programs

**Practical Example:** A personalized greeting app — asks for your name and age, then replies with a custom message.

**Exercises include:**
1. Ask for the user's name and greet them by name
2. Ask for two numbers and print their sum
3. Build a "Mad Libs" style program with 4 user inputs
4. Ask for a city name and print "I'd love to visit [city]!"
5. Collect first name, last name, and print the full name
6. Ask for a radius and calculate the area of a circle (π r²)
7. Build a simple "Tell me about yourself" form with 5 fields
8. Ask for the user's birth year and print their approximate age
9. Take a sentence as input and print how many characters it has (using `len()`)
10. Collect 3 subject marks, compute and display the average — all from input

---

### `4_type_conversion.py` — Type Conversion

Since `input()` returns strings, and operations require the right types, converting between types is something you'll do constantly.

**Concepts covered:**
- Implicit conversion (Python does it automatically)
- Explicit conversion: `int()`, `float()`, `str()`, `bool()`
- What values are truthy vs falsy
- Common errors when conversion fails — and how to avoid them
- Chaining conversions

**Practical Example:** A tip calculator — reads bill amount and tip percentage from input, converts them, and outputs the final amount.

**Exercises include:**
1. Read two numbers from input and print their sum (not concatenation)
2. Convert a float like `9.99` to int and explain what happens to the decimal
3. Convert `0`, `""`, `None`, and `[]` to bool and print the results
4. Read a price and quantity, compute total cost, display with 2 decimal places
5. Convert the string `"3.14"` → float → int and print each step
6. Check: what does `int("hello")` do? Handle it gracefully with a message
7. Build a unit converter: read cm from input, convert and display in inches
8. Take a number input, check if it's even using `%` after converting to int
9. Read a temperature in Celsius from input and display it in Fahrenheit
10. Chain conversions: input → float → round → int → str → print with a label

---

## 🚀 How to Run

Navigate into the `0_basics/` directory and run any file with:

```bash
python 0_hello_world.py
python 1_variables_and_types.py
```

No installations needed — this module uses Python built-ins only (except `math`, which is part of the standard library).

---

## 💡 Key Takeaways from This Module

- Every Python program starts executing from the top line and goes down
- Python is **dynamically typed** — you assign values, not types
- `input()` **always returns a string** — convert it before doing math
- Use `type()` anytime you're unsure what you're working with
- The `%` (modulo) operator is more useful than it looks — remember it

---

## ➡️ What's Next

Once you're comfortable with the basics, move on to:

**`01_flow_control/`** — Python's  built-in data structures

```bash
cd ../01_flow_control
python 0_if statement.py
```
