print("Creating Dictionaries\n")

# Using curly braces
student = {
    "name": "Ali",
    "age": 20,
    "course": "Python"
}

# Using dict() constructor
person = dict(name="Sara", age=25, city="Karachi")

# Empty dictionary
empty = {}
also_empty = dict()

# From list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
from_pairs = dict(pairs)

print(f"Student: {student}")
print(f"Person: {person}")
print(f"From pairs: {from_pairs}")




print("\nAccessing Values\n")

student = {"name": "Ali", "age": 22, "grade": "A"}

# Using square brackets
name = student["name"]
print(f"Name: {name}")

# Using get() method (safer - returns None if key doesn't exist)
age = student.get("age")
email = student.get("email")  # Returns None
email_default = student.get("email", "not provided")

print(f"Age: {age}")
print(f"Email: {email}")
print(f"Email with default: {email_default}")





print("\nAdding and Updating\n")

student = {"name": "Ali", "age": 20}
print(f"Original: {student}")

# Add new key-value pair
student["email"] = "ali@example.com"
print(f"After adding email: {student}")

# Update existing value
student["age"] = 21
print(f"After updating age: {student}")

# Update multiple values
student.update({"age": 22, "grade": "A"})
print(f"After update(): {student}")




print("\nRemoving Items\n")

student = {"name": "Ali", "age": 22, "grade": "A", "email": "ali@example.com"}
print(f"Original: {student}")

# pop() - Remove and return value
grade = student.pop("grade")
print(f"Popped grade: {grade}")
print(f"After pop: {student}")

# popitem() - Remove and return last inserted item
last = student.popitem()
print(f"Popped item: {last}")
print(f"After popitem: {student}")

# del - Remove by key
del student["age"]
print(f"After del: {student}")

# clear() - Remove all items
student.clear()
print(f"After clear: {student}")




print("\nChecking Membership\n")

student = {"name": "Ali", "age": 22, "grade": "A"}

print(f"'name' in student: {'name' in student}")
print(f"'email' in student: {'email' in student}")
print(f"'Ali' in student: {'Ali' in student}")  # Checks keys, not values

# Check in values
print(f"'Ali' in student.values(): {'Ali' in student.values()}")




print("\nIterating\n")

student = {"name": "Ali", "age": 22, "grade": "A"}

# Iterate over keys (default)
print("Keys:")
for key in student:
    print(f"  {key}")

# Iterate over values
print("\nValues:")
for value in student.values():
    print(f"  {value}")

# Iterate over key-value pairs
print("\nKey-Value Pairs:")
for key, value in student.items():
    print(f"  {key}: {value}")




print("\nNested Dictionaries\n")

students = {
    "student1": {"name": "Ali", "grade": "A"},
    "student2": {"name": "Sara", "grade": "B"},
    "student3": {"name": "Ahmed", "grade": "A"}
}

print(f"All students: {students}")
print(f"Student 1 name: {students['student1']['name']}")

# Iterate over nested dictionary
for student_id, info in students.items():
    print(f"{student_id}: {info['name']} - Grade {info['grade']}")




print("\nDictionary with Lists\n")

marks = {
    "math": [90, 92, 85],
    "science": [88, 84, 89],
    "english": [95, 91, 93]
}

print(f"Math marks: {marks['math']}")
print(f"Average math: {sum(marks['math']) / len(marks['math']):.2f}")




print("\nPractical Example: Word Frequency\n")

text = "hello world hello python world"
words = text.split()

frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(f"Word frequency: {frequency}")