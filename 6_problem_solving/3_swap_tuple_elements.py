"""
Problem:
Given a list of tuples, swap the elements of each tuple.

Example:
Input: [(1, 2), (3, 4)]
Output: [(2, 1), (4, 3)]

Solution:
Use list comprehension to create new tuples with swapped order.
"""

def swap_tuples(lst):
    # Swap elements in each tuple of a list.

    return [(b, a) for (a, b) in lst]



# Test cases
print("Swap Tuple Elements\n")

# Test 1
l1 = [(1, 2), (3, 4), (5, 6)]
print(f"Input: {l1}")
print(f"Output: {swap_tuples(l1)}")

# Test 2
l2 = [('a', 1), ('b', 2)]
print(f"Input: {l2}")
print(f"Output: {swap_tuples(l2)}")
