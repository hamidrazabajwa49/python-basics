print("Creating Strings\n")

# Single quotes
single = 'Hello'

# Double quotes
double = "World"

# Triple quotes (multi-line)
multi = """This is a
multi-line
string"""

# String concatenation
full = single + " " + double
print(f"Concatenated: {full}")

# String repetition
repeated = "Ha" * 3
print(f"Repeated: {repeated}")




print("\nIndexing and Slicing\n")

text = "Python Programming"

print(f"First char: {text[0]}")
print(f"Last char: {text[-1]}")
print(f"Slice [0:6]: {text[0:6]}")
print(f"Every 2nd char: {text[::2]}")
print(f"Reversed: {text[::-1]}")




print("\nCase Methods\n")

text = "Hello World"

print(f"upper(): {text.upper()}")
print(f"lower(): {text.lower()}")
print(f"title(): {text.title()}")
print(f"capitalize(): {text.capitalize()}")
print(f"swapcase(): {text.swapcase()}")




print("\nSearch Methods\n")

text = "Hello World, Welcome to Python"

print(f"find('World'): {text.find('World')}")
print(f"index('Python'): {text.index('Python')}")
print(f"count('o'): {text.count('o')}")
print(f"startswith('Hello'): {text.startswith('Hello')}")
print(f"endswith('Python'): {text.endswith('Python')}")




print("\nModification Methods\n")

text = "  Hello World  "

print(f"strip(): '{text.strip()}'")
print(f"replace('World', 'Python'): {text.replace('World', 'Python')}")
print(f"split(): {text.split()}")

# Join
words = ["Python", "is", "awesome"]
joined = " ".join(words)
print(f"join(): {joined}")




print("\nString Formatting\n")

name = "Ali"
age = 22

# f-strings (recommended)
message = f"My name is {name} and I am {age} years old"
print(message)

# format() method
message = "My name is {} and I am {} years old".format(name, age)
print(message)

# % operator (old style)
message = "My name is %s and I am %d years old" % (name, age)
print(message)