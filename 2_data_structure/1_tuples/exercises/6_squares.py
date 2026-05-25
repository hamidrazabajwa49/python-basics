def square_tuple(t):
    """
    Square each element.
    
    Args:
        t (tuple): Input tuple
        
    Returns:
        tuple: Tuple of squares
    """
    return tuple(x**2 for x in t)

# Test
t = (1, 2, 3, 4, 5)
print(f"Original: {t}")
print(f"Squares: {square_tuple(t)}")
