def flatten_tuple(nested):
    """
    Flatten a tuple of tuples.
    
    Args:
        nested (tuple): Nested tuple
        
    Returns:
        tuple: Flat tuple
    """
    return tuple(x for pair in nested for x in pair)

# Test
nested = ((1, 2), (3, 4), (5, 6))
print(f"Nested: {nested}")
print(f"Flat: {flatten_tuple(nested)}")
