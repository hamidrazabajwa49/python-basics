def tuple_length(t):
    """
    Count elements in a tuple.
    
    Args:
        t (tuple): Input tuple
        
    Returns:
        int: Number of elements
    """
    count = 0
    for _ in t:
        count += 1
    return count

# Test
t = (1, 2, 3, 4, 5)
print(f"Tuple: {t}")
print(f"Length: {tuple_length(t)}")
