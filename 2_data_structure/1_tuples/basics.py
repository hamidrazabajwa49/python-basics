print("Creating Tuples\n")

# Using parentheses
coordinates = (10, 20)
rgb = (255, 128, 0)

# Without parentheses (tuple packing)
point = 5, 10

# Single element tuple 
single = (42,)  # Comma is required
not_tuple = (42)  # integer

# Empty tuple
empty = ()

# Using tuple() constructor
from_list = tuple([1, 2, 3])
from_string = tuple("abc")

print(f"Coordinates: {coordinates}")
print(f"RGB: {rgb}")
print(f"Point: {point}")
print(f"Single: {single}, type: {type(single)}")
print(f"Not tuple: {not_tuple}, type: {type(not_tuple)}")
print(f"From list: {from_list}")




print("\nAccessing Elements\n")

colors = ("red", "green", "blue", "yellow")

print(f"First: {colors[0]}")
print(f"Last: {colors[-1]}")
print(f"Slice: {colors[1:3]}")




print("\nTuple Unpacking\n")

# Basic unpacking
x, y = (10, 20)
print(f"x = {x}, y = {y}")

# Swap variables
a, b = 5, 10
a, b = b, a  # Swaping
print(f"After swap: a = {a}, b = {b}")

# Extended unpacking
first, *middle, last = (1, 2, 3, 4, 5)
print(f"First: {first}, Middle: {middle}, Last: {last}")




print("\nTuple Methods\n")

numbers = (1, 2, 3, 2, 4, 2, 5)

# count() - Count occurrences
count_2 = numbers.count(2)
print(f"Count of 2: {count_2}")

# index() - Find first index
index_3 = numbers.index(3)
print(f"Index of 3: {index_3}")





print("\nImmutability\n")

my_tuple = (1, 2, 3)
print(f"Original: {my_tuple}")

# This would cause an error:
# my_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment

# But you can create a new tuple
new_tuple = my_tuple + (4, 5)
print(f"New tuple: {new_tuple}")




print("\nWhen to Use Tuples\n")

# 1. For fixed collections 
position = (100, 200)
color = (255, 0, 0)

# 2. As dictionary keys 
locations = {
    (0, 0): "Origin",
    (1, 0): "East",
    (0, 1): "North"
}

# 3. Function returns
def get_min_max(numbers):
    return min(numbers), max(numbers)

result = get_min_max([1, 5, 3, 9, 2])
print(f"Min and Max: {result}")





print("\nTuple vs List\n")

# Tuples are faster for iteration
import sys

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

print(f"List size: {sys.getsizeof(my_list)} bytes")
print(f"Tuple size: {sys.getsizeof(my_tuple)} bytes")