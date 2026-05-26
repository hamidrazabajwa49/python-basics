"""
Problem:
Given a list of tuple pairs, filter those that are anagrams.
Two strings are anagrams if they contain the same characters.

Example:
Input: [("listen", "silent"), ("apple", "pale")]
Output: [("listen", "silent")]

Solution:
Check if sorted characters of both strings are equal.
"""


def find_anagram_pairs(pairs):
    # Find pairs that are anagrams.

    return [
        pair for pair in pairs 
        if sorted(pair[0].lower()) == sorted(pair[1].lower())
    ]



# Test cases
print("Anagram Pairs\n")

# Test 1
p1 = [("listen", "silent"), ("apple", "pale"), ("race", "care")]
print(f"Input: {p1}")
print(f"Anagrams: {find_anagram_pairs(p1)}")

# Test 2
p2 = [("hello", "world"), ("evil", "live")]
print(f"Input: {p2}")
print(f"Anagrams: {find_anagram_pairs(p2)}")
