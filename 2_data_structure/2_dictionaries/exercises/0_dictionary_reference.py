# Creating a dictionary
student = {
    "name": "Ali",
    "age": 20,
    "course": "Python"
}
print("Student:", student)

# Accessing values
print("Name:", student["name"])
print("Age using get():", student.get("age"))

# Adding and updating items
student["email"] = "ali@example.com"
student["age"] = 21
print("Updated Student:", student)

# Removing items
student.pop("course")               # removes by key
student.popitem()                   # removes the last inserted item
del student["age"]                  # removes by key using del
print("After deletions:", student)

# Looping through dictionary
student = {"name": "Ali", "age": 22, "grade": "A"}

print("\nLooping through keys:")
for key in student:
    print(key)

print("\nLooping through values:")
for value in student.values():
    print(value)

print("\nLooping through items:")
for key, value in student.items():
    print(f"{key}: {value}")

# Checking existence
if "age" in student:
    print("\n'age' exists in dictionary")


# Intermediate Level Dictionary Code


# Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print("\nSquares using comprehension:", squares)

# Merging two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict1.update(dict2)
print("Merged dict1:", dict1)

# Nested dictionary
students = {
    "student1": {"name": "Ali", "grade": "A"},
    "student2": {"name": "Sara", "grade": "B"}
}
print("\nNested Dictionary Access:")
print(students["student1"]["name"])

# Dictionary with list values
marks = {
    "math": [90, 92, 85],
    "science": [88, 84, 89]
}
print("Math Marks:", marks["math"])

# Counting frequency of elements in a list
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
freq = {}
for fruit in fruits:
    freq[fruit] = freq.get(fruit, 0) + 1
print("\nFruit frequency:", freq)

# Inverting a dictionary (keys become values and vice versa)
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print("Inverted Dictionary:", inverted)

# Using setdefault() to initialize keys
words = {}
for word in ["cat", "dog", "cat", "rat", "dog"]:
    words.setdefault(word, 0)
    words[word] += 1
print("Word counts using setdefault():", words)

# Safe value retrieval using get()
name = student.get("name", "Unknown")
print("Safely retrieved name:", name)

# Clearing the entire dictionary
student.clear()
print("After clearing student:", student)
