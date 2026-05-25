print("Creating Lists\n")


# Empty list
empty_list = []
also_empty = list()


# With items
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True, [5, 6]]  # Can contain any type


# Using list() constructor
from_range = list(range(1, 6))
from_string = list("Python")    

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed: {mixed}")
print(f"From range: {from_range}")
print(f"From string: {from_string}")




print("\nIndexing\n")

colors = ["red", "green", "blue", "yellow", "purple"]

# From start for positive
print(f"First color: {colors[0]}")      
print(f"Second color: {colors[1]}")     
print(f"Third color: {colors[2]}")      

# Negative (from end)
print(f"Last color: {colors[-1]}")      
print(f"Second last: {colors[-2]}")     




print("\nSlicing\n")
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic: list[start:stop]
print(f"numbers[2:5] = {numbers[2:5]}")     
print(f"numbers[:4] = {numbers[:4]}")        
print(f"numbers[5:] = {numbers[5:]}")     
# With step: list[start:stop:step]
print(f"numbers[::2] = {numbers[::2]}")      
print(f"numbers[1::2] = {numbers[1::2]}")    
print(f"numbers[::-1] = {numbers[::-1]}")    # Reverse list

# Negative indices in slicing
print(f"numbers[-5:-2] = {numbers[-5:-2]}") 




print("\nModifying Lists\n")

fruits = ["apple", "banana", "cherry"]
print(f"Original: {fruits}")

# Change item
fruits[1] = "mango"
print(f"After change: {fruits}")

# Change multiple items
fruits[0:2] = ["orange", "grape"]
print(f"After slice change: {fruits}")



print("\nList Length\n")

numbers = [10, 20, 30, 40, 50]
print(f"List: {numbers}")
print(f"Length: {len(numbers)}")



print("\nMembership Testing\n")

fruits = ["apple", "banana", "cherry"]

print(f"'apple' in fruits: {'apple' in fruits}")      
print(f"'mango' in fruits: {'mango' in fruits}")        
print(f"'apple' not in fruits: {'apple' not in fruits}")  




print("\nIterating Over Lists\n")

colors = ["red", "green", "blue"]

# Simple iteration
for color in colors:
    print(f"Color: {color}")

# Iteration with index
for i, color in enumerate(colors):
    print(f"Index {i}: {color}")



print("\nNested Lists\n")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f"Matrix: {matrix}")
print(f"First row: {matrix[0]}")
print(f"Element [1][2]: {matrix[1][2]}") 

# Iterate 
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()



print("\nConcatenation and Repetition\n")

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
combined = list1 + list2
print(f"Combined: {combined}")

# Repetition 
repeated = [0] * 5
print(f"Repeated: {repeated}")