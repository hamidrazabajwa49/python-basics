"""
Problem:
Given a string in format "key=value,key=value", convert it to 
a list of tuples [(key, value), ...].

Example:
Input: "a=1,b=2,c=3"
Output: [('a', 1), ('b', 2), ('c', 3)]

Solution:
Split by comma, then split each pair by equals sign.
"""

def string_to_tuple_list(s):
    # Convert string format 'k=v,k=v' to list of tuples.

    if not s:
        return []
        
    pairs = s.split(',')
    result = []
    
    for pair in pairs:
        if '=' in pair:
            key, value = pair.split('=')
            # Convert value to int if possible, else keep as string
            try:
                value = int(value)
            except ValueError:
                pass
            result.append((key.strip(), value))
            
    return result




# Test cases
print("String to Tuple List\n")

# Test 1
s1 = "a=1,b=2,c=3"
print(f"Input: '{s1}'")
print(f"Output: {string_to_tuple_list(s1)}")

# Test 2
s2 = "name=Ali,age=22,city=Karachi"
print(f"Input: '{s2}'")
print(f"Output: {string_to_tuple_list(s2)}")

"""
Alternative Solution (List Comprehension):

def string_to_tuple_v2(s):
    return [(k, int(v)) for k, v in (pair.split('=') for pair in s.split(','))]
"""
