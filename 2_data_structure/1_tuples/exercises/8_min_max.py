def min_max(t):
    """
    Find min and max values.
    
    Args:
        t (tuple): Input tuple
        
    Returns:
        tuple: (min_val, max_val)
    """
    if not t:
        return None, None
        
    min_val = max_val = t[0]
    for num in t[1:]:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
            
    return min_val, max_val

# Test
t = (5, 1, 9, 2, 8)
print(f"Tuple: {t}")
print(f"Min/Max: {min_max(t)}")
