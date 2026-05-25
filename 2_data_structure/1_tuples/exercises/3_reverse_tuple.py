def reverse_tuple(t):
    """
    Reverse a tuple.
    
    Args:
        t (tuple): Input tuple
        
    Returns:
        tuple: Reversed tuple
    """
    return t[::-1]

# Test
t = (1, 2, 3, 4)
print(f"Original: {t}")
print(f"Reversed: {reverse_tuple(t)}")
