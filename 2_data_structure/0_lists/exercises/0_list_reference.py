
# List Creation 
fruits = ["apple", "banana", "cherry"]
numbers = list(range(1, 6))  # [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]

print("Original Fruits:", fruits)
print("Numbers List:", numbers)
print("Mixed List:", mixed)

# Indexing and Slicing 
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Fruits slice:", fruits[1:3])  

# Modifying Lists 
fruits[1] = "mango"
print("Modified Fruits:", fruits)

# List Methods 
fruits.append("orange")              # Add to end
fruits.insert(1, "grape")           # Add at index
fruits.remove("apple")              # Remove by value
popped = fruits.pop()               # Remove last
fruits.sort()                       # Sort alphabetically
fruits.reverse()                    # Reverse list

print("Updated Fruits:", fruits)
print("Popped Element:", popped)

# More Methods 
fruits.extend(["kiwi", "pear"])     # Extend list
count = fruits.count("mango")       # Count occurrences
index = fruits.index("grape")       # Find index
fruits.clear()                      # Clear all items

print("Final Fruits (cleared):", fruits)
print("Count of 'mango':", count)
print("Index of 'grape':", index)

# Useful Functions 
print("Length of numbers:", len(numbers))
print("Max value:", max(numbers))
print("Min value:", min(numbers))
print("Sum:", sum(numbers))
print("Sorted list:", sorted(numbers, reverse=True))

# Iteration 
print("Numbers:")
for num in numbers:
    print(num, end=' ')
print()

# List Comprehension 
squares = [x**2 for x in numbers]  # [1, 4, 9, 16, 25]
evens = [x for x in numbers if x % 2 == 0]

print("Squares:", squares)
print("Evens:", evens)

# Nested Lists 
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:", matrix)
print("Element at [1][2]:", matrix[1][2])

# Copying Lists Safely 
original = [1, 2, 3]
copy1 = original.copy()
copy2 = list(original)
copy3 = original[:]

original.append(4)
print("Original:", original)
print("Copies:", copy1, copy2, copy3)
