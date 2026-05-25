print("Basic Lambda\n")

# Regular function
def square(x):
    return x ** 2

# Lambda equivalent
square_lambda = lambda x: x ** 2

print(f"Regular: square(5) = {square(5)}")
print(f"Lambda: square_lambda(5) = {square_lambda(5)}")




print("\nMultiple Arguments\n")
add = lambda a, b: a + b
multiply = lambda a, b, c: a * b * c

print(f"add(3, 5) = {add(3, 5)}")
print(f"multiply(2, 3, 4) = {multiply(2, 3, 4)}")





print("\nLambda with map()\n")
numbers = [1, 2, 3, 4, 5]

# Square all numbers
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared: {squared}")

# Convert to strings
strings = list(map(lambda x: str(x), numbers))
print(f"Strings: {strings}")




print("\nLambda with filter()\n")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens: {evens}")

# Filter numbers > 5
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(f"Greater than 5: {greater_than_5}")





print("\nLambda with sorted()\n")

# Sort by second element
pairs = [(1, 5), (3, 2), (2, 8), (4, 1)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(f"Sorted by second element: {sorted_pairs}")

# Sort strings by length
words = ["python", "is", "awesome", "fun"]
sorted_words = sorted(words, key=lambda x: len(x))
print(f"Sorted by length: {sorted_words}")





print("\nWhen to Use Lambda\n")

# Good use: Simple, one-time operations
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(f"Doubled: {doubled}")

# Bad use: Complex logic (use regular function instead)
# Don't do this:
# complex_lambda = lambda x: x ** 2 if x > 0 else -x ** 2 if x < 0 else 0

# Do this instead:
def complex_function(x):
    if x > 0:
        return x ** 2
    elif x < 0:
        return -x ** 2
    else:
        return 0