"""
Problem:
Given two strings, find all characters that appear in both strings.

Example:
Input: "apple", "grape"
Output: ['a', 'p', 'e']

Solution:
Use set intersection to find common elements.
"""

def common_chars(s1, s2):
    # Convert strings to sets and find intersection
    return list(set(s1) & set(s2))



# Test cases
print("=Common Characters\n")

# Test 1
result1 = common_chars("apple", "grape")
print(f"common_chars('apple', 'grape') = {result1}")

# Test 2
result2 = common_chars("hello", "world")
print(f"common_chars('hello', 'world') = {result2}")

# Test 3
result3 = common_chars("python", "java")
print(f"common_chars('python', 'java') = {result3}")

# Explanation
print("\nWorking......\n")
print(f"set('apple') = {set('apple')}")
print(f"set('grape') = {set('grape')}")
print(f"Intersection = {set('apple') & set('grape')}")


"""
Alternative Solutions:
# Using list comprehension
def common_chars_v2(s1, s2):
    return [char for char in set(s1) if char in s2]

# Using filter
def common_chars_v3(s1, s2):
    return list(filter(lambda x: x in s2, set(s1)))
"""
