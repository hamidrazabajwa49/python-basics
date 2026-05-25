print("Basic List Comprehension\n")

# General way
squares_traditional = []
for x in range(1, 6):
    squares_traditional.append(x ** 2)

# List comprehension way
squares = [x ** 2 for x in range(1, 6)]

print(f"Traditional: {squares_traditional}")
print(f"Comprehension: {squares}")



print("\nWith Conditional\n")

# Eeven numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {evens}")

# Odd numbers
odds = [x for x in numbers if x % 2 != 0]
print(f"Odd numbers: {odds}")

# Num greater than 5
greater_than_5 = [x for x in numbers if x > 5]
print(f"Greater than 5: {greater_than_5}")



print("\nWith Transformation\n")

# Double each number
numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers]
print(f"Doubled: {doubled}")


# Convert to uppercase
words = ["hello", "world", "python"]
uppercase = [word.upper() for word in words]
print(f"Uppercase: {uppercase}")

# Get length
lengths = [len(word) for word in words]
print(f"Lengths: {lengths}")



print("\nWith If-Else\n")

# Label numbers as even or odd
numbers = [1, 2, 3, 4, 5]
labels = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(f"Labels: {labels}")


# Replace negative with 0
numbers = [5, -3, 8, -1, 10]
non_negative = [x if x >= 0 else 0 for x in numbers]
print(f"Non-negative: {non_negative}")




print("\nNested List Comprehensions\n")

# Create a matrix
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("Multiplication table:")
for row in matrix:
    print(row)


# Flatten a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"\nFlattened: {flattened}")



print("\nWith Functions\n")

# Using built-in functions
numbers = [1, 2, 3, 4, 5]
strings = [str(x) for x in numbers]
print(f"Strings: {strings}")

# Using a custom function
def square(x):
    return x ** 2

squared = [square(x) for x in numbers]
print(f"Squared: {squared}")



print("\nPractical Examples\n")

# Extract first letters
names = ["Alice", "Bob", "Charlie", "David"]
initials = [name[0] for name in names]
print(f"Initials: {initials}")


# Filter and transform
prices = [10.5, 25.0, 5.75, 30.0, 15.25]
expensive = [f"${price:.2f}" for price in prices if price > 15]
print(f"Expensive items: {expensive}")



# Create coordinate pairs
coordinates = [(x, y) for x in range(3) for y in range(3)]
print(f"Coordinates: {coordinates}")



# Remove vowels from string
text = "Hello World"
no_vowels = [char for char in text if char.lower() not in "aeiou"]
result = "".join(no_vowels)
print(f"No vowels: {result}")




print("\nTraditional vs Comprehension\n")

# Example: Get squares of even numbers

# Traditional
result_trad = []
for x in range(1, 11):
    if x % 2 == 0:
        result_trad.append(x ** 2)

# Comprehension
result_comp = [x ** 2 for x in range(1, 11) if x % 2 == 0]

print(f"Traditional: {result_trad}")
print(f"Comprehension: {result_comp}")