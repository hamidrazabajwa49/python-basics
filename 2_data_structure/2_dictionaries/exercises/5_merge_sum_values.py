def merge_and_sum(d1, d2):
    """
    Merge two dictionaries and sum values for common keys.
    
    Args:
        d1 (dict): First dictionary
        d2 (dict): Second dictionary
        
    Returns:
        dict: Merged dictionary
    """
    merged = d1.copy()
    for key, value in d2.items():
        merged[key] = merged.get(key, 0) + value
    return merged

# Test
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

print(f"Dict 1: {d1}")
print(f"Dict 2: {d2}")
print(f"Merged: {merge_and_sum(d1, d2)}")
