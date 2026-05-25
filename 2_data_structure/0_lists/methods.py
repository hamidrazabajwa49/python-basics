print("Adding Elements\n")

fruits = ["apple", "banana"]
print(f"Original: {fruits}")

# append() - single item to end
fruits.append("cherry")
print(f"After append('cherry'): {fruits}")

# insert() - item at specific index
fruits.insert(1, "mango")
print(f"After insert(1, 'mango'): {fruits}")

# extend() - multiple items
fruits.extend(["orange", "grape"])
print(f"After extend(['orange', 'grape']): {fruits}")



print("\nRemoving Elements\n")

numbers = [1, 2, 3, 4, 5, 3]
print(f"Original: {numbers}")

# remove() - Remove first occurrence of value
numbers.remove(3)
print(f"After remove(3): {numbers}")

# pop() - Remove and return item at index (default: last)
last = numbers.pop()
print(f"Popped: {last}, List: {numbers}")

first = numbers.pop(0)
print(f"Popped index 0: {first}, List: {numbers}")

# clear() - Remove all items
numbers_copy = [1, 2, 3]
numbers_copy.clear()
print(f"After clear(): {numbers_copy}")

# del statement - Remove by index or slice
items = [0, 1, 2, 3, 4, 5]
del items[2]
print(f"After del items[2]: {items}")




print("\nFinding Elements\n")

colors = ["red", "green", "blue", "green", "yellow"]

# index() - Find first index of value
idx = colors.index("green")
print(f"Index of 'green': {idx}")

# count() - Count occurrences
count = colors.count("green")
print(f"Count of 'green': {count}")




print("\nSorting\n")

numbers = [5, 2, 8, 1, 9, 3]
print(f"Original: {numbers}")

# sort() - Sort in place (modifies original)
numbers.sort()
print(f"After sort(): {numbers}")

# sort(reverse=True) - Descending order
numbers.sort(reverse=True)
print(f"After sort(reverse=True): {numbers}")

# sorted() - Returns new sorted list (doesn't modify original)
original = [5, 2, 8, 1]
sorted_list = sorted(original)
print(f"Original: {original}, Sorted: {sorted_list}")




print("\nReversing\n")

letters = ["a", "b", "c", "d"]
print(f"Original: {letters}")

# reverse() - Reverse in place
letters.reverse()
print(f"After reverse(): {letters}")

# Using slicing (creates new list)
original = [1, 2, 3, 4]
reversed_list = original[::-1]
print(f"Original: {original}, Reversed: {reversed_list}")




print("\nCopying Lists\n")

original = [1, 2, 3]

# Method 1: copy()
copy1 = original.copy()

# Method 2: list() constructor
copy2 = list(original)

# Method 3: slicing
copy3 = original[:]

# Modify original
original.append(4)

print(f"Original: {original}")
print(f"Copy 1: {copy1}")
print(f"Copy 2: {copy2}")
print(f"Copy 3: {copy3}")




print("\nBuilt-in Functions\n")

numbers = [10, 20, 30, 40, 50]

print(f"List: {numbers}")
print(f"len(numbers): {len(numbers)}")      # Length
print(f"max(numbers): {max(numbers)}")      # Maximum
print(f"min(numbers): {min(numbers)}")      # Minimum
print(f"sum(numbers): {sum(numbers)}")      # Sum
print(f"any([0, 0, 1]): {any([0, 0, 1])}")  # True if any element is True
print(f"all([1, 1, 1]): {all([1, 1, 1])}")  # True if all elements are True



# Examples


# Shopping Cart
print("\nPractical Example: Shopping Cart\n")

cart = []

# Add items
cart.append("Laptop")
cart.append("Mouse")
cart.append("Keyboard")
print(f"Cart: {cart}")

# Remove item
cart.remove("Mouse")
print(f"After removing Mouse: {cart}")

# Add more items
cart.extend(["Monitor", "Headphones"])
print(f"Final cart: {cart}")
print(f"Total items: {len(cart)}")