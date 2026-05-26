"""
Problem:
Given a string, find the character that appears most frequently.

Example:
Input: "mississippi"
Output: 'i' (appears 4 times)

Solution:
Use a dictionary to count frequencies, then find the max.
"""

def most_frequent_char(s):
    # Find the most frequent character in a string.
    if not s:
        return None
        
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
        
    # Find key with maximum value
    return max(freq, key=freq.get)



# Test cases
print("\nMost Frequent Character\n")

# Test 1
s1 = "mississippi"
print(f"String: '{s1}'")
print(f"Most frequent: '{most_frequent_char(s1)}'")

# Test 2
s2 = "banana"
print(f"String: '{s2}'")
print(f"Most frequent: '{most_frequent_char(s2)}'")

# Test 3
s3 = "aaaaabbb"
print(f"String: '{s3}'")
print(f"Most frequent: '{most_frequent_char(s3)}'")

"""
Alternative Solution:

from collections import Counter
def most_frequent_v2(s):
    return Counter(s).most_common(1)[0][0]
"""
