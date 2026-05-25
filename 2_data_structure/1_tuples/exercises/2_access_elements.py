def get_first_last(t):
    """
    Get first and last elements.
    
    Args:
        t (tuple): Input tuple
        
    Returns:
        tuple: (first, last)
    """
    if not t:
        return None, None
    return t[0], t[-1]

# Test
t = (1, 2, 3, 4, 5)
first, last = get_first_last(t)
print(f"Tuple: {t}")
print(f"First: {first}, Last: {last}")
