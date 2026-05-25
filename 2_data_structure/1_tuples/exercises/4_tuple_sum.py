def tuple_sum(t):
    """
    Sum elements of a tuple.
    
    Args:
        t (tuple): Input tuple
        
    Returns:
        int: Sum of elements
    """
    total = 0
    for i in t:
        total += i
    return total

# Test
t = (1, 2, 3, 4, 5)
print(f"Tuple: {t}")
print(f"Sum: {tuple_sum(t)}")
