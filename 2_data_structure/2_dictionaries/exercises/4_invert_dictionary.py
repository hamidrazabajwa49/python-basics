def invert_dict(d):
    """
    Invert dictionary keys and values.
    
    Args:
        d (dict): Input dictionary
        
    Returns:
        dict: Inverted dictionary
    """
    return {v: k for k, v in d.items()}

# Test
data = {'a': 1, 'b': 2, 'c': 3}
print(f"Original: {data}")
print(f"Inverted: {invert_dict(data)}")
