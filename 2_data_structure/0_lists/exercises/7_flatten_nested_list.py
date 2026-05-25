def flatten_list(nested_list):
    """
    Flatten a nested list.
    
    Args:
        nested_list (list): List of lists
        
    Returns:
        list: Flattened list
    """
    flat = []
    for sublist in nested_list:
        for item in sublist:
            flat.append(item)
    return flat

# Test
nested = [[1, 2], [3, 4], [5]]
print(f"Nested: {nested}")
print(f"Flat: {flatten_list(nested)}")
