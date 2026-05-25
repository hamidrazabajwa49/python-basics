# Basic Tuple Creation
print("1. Basic Tuple Creation")
t1 = (10, 20, 30)
t2 = ("apple", "banana", "cherry")
t3 = (1, "hello", 3.14, True)

print("Tuple 1:", t1)
print("Tuple 2:", t2)
print("Tuple 3:", t3)

# Tuple Packing and Unpacking
print("\n2. Packing and Unpacking")
packed = 1, 2, "packed"
a, b, c = packed
print("Packed Tuple:", packed)
print("Unpacked:", a, b, c)

# Accessing Elements and Slicing
print("\n3. Accessing Elements and Slicing")
t = (10, 20, 30, 40, 50)
print("t[0]:", t[0])
print("t[1:4]:", t[1:4])
print("t[-2]:", t[-2])

# Tuple Immutability
print("\n4. Tuple Immutability")
try:
    t[0] = 100
except TypeError as e:
    print("Error:", e)

# Using Tuples in Loops
print("\n5. Looping through Tuples")
for item in t2:
    print("Fruit:", item)

# Tuple Methods
print("\n6. Tuple Methods")
nums = (1, 2, 2, 3, 4, 2)
print("Count of 2:", nums.count(2))
print("Index of 3:", nums.index(3))

# Tuple with Single Element
print("\n7. Single Element Tuple")
single = (10,)  # must include comma
not_tuple = (10)
print("Type of single:", type(single))
print("Type of not_tuple:", type(not_tuple))

# Nested Tuples
print("\n8. Nested Tuples")
nested = ((1, 2), (3, 4), (5, 6))
for pair in nested:
    print("Pair:", pair)

# Tuple as Dictionary Keys
print("\n9. Tuples as Dictionary Keys")
location = {
    (31.5497, 74.3436): "Lahore",
    (33.6844, 73.0479): "Islamabad"
}
print("City at (31.5497, 74.3436):", location[(31.5497, 74.3436)])

# Tuple Operations
print("\n10. Tuple Operations")
a = (1, 2, 3)
b = (4, 5)
print("Concatenation:", a + b)
print("Repetition:", a * 2)

# Convert between Tuple and List
print("\n11. Conversion")
list1 = list(t1)
print("List from Tuple:", list1)
tuple1 = tuple(list1)
print("Tuple from List:", tuple1)

# Functions Returning Tuples
print("\n12. Functions Returning Tuples")
def divide(x, y):
    return x // y, x % y

quotient, remainder = divide(17, 5)
print("Quotient:", quotient)
print("Remainder:", remainder)

# Membership Test
print("\n13. Membership Test")
print("20 in t1:", 20 in t1)
print("100 not in t1:", 100 not in t1)

# Tuple Sorting (indirectly by converting to list)
print("\n14. Sorting Tuple")
unsorted_tuple = (3, 1, 4, 2)
sorted_tuple = tuple(sorted(unsorted_tuple))
print("Sorted Tuple:", sorted_tuple)
