def lists_to_dict(keys, values):
    """
    Convert two lists to a dictionary.
    
    Args:
        keys (list): List of keys
        values (list): List of values
        
    Returns:
        dict: Combined dictionary
    """
    return dict(zip(keys, values))

# Test
l1 = ['a', 'b', 'c']
l2 = [1, 2, 3]
print(f"Keys: {l1}")
print(f"Values: {l2}")
print(f"Dictionary: {lists_to_dict(l1, l2)}")
