print("Basic Dictionary Comprehension\n")

# Create squares dictionary
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# From two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
combined = {k: v for k, v in zip(keys, values)}
print(f"Combined: {combined}")



print("\nWith Conditional\n")

# Only even numbers
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Filter dictionary
prices = {"apple": 0.5, "banana": 0.3, "cherry": 2.0, "date": 1.5}
expensive = {k: v for k, v in prices.items() if v > 1.0}
print(f"Expensive items: {expensive}")





print("\nTransforming Dictionaries\n")

# Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(f"Swapped: {swapped}")

# Transform values
temps_c = {"morning": 20, "afternoon": 25, "evening": 18}
temps_f = {k: (v * 9/5) + 32 for k, v in temps_c.items()}
print(f"Temperatures (F): {temps_f}")