def find_duplicates(t):
    """
    Find duplicate values.
    
    Args:
        t (tuple): Input tuple
        
    Returns:
        tuple: Tuple of duplicate values
    """
    seen = set()
    duplicates = set()
    
    for i in t:
        if i in seen:
            duplicates.add(i)
        else:
            seen.add(i)
            
    return tuple(duplicates)

# Test
t = (1, 2, 3, 4, 5, 6, 2, 3, 6, 8)
print(f"Tuple: {t}")
print(f"Duplicates: {find_duplicates(t)}")
