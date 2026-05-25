def find_min_max_keys(data):
    """
    Find keys for min and max values.
    
    Args:
        data (dict): Input dictionary
        
    Returns:
        tuple: (min_key, max_key)
    """
    if not data:
        return None, None
        
    max_key = max(data, key=data.get)
    min_key = min(data, key=data.get)
    return min_key, max_key

# Test
data = {'a': 100, 'b': 200, 'c': 50}
min_k, max_k = find_min_max_keys(data)

print(f"Data: {data}")
print(f"Key with max value: {max_k}")
print(f"Key with min value: {min_k}")
