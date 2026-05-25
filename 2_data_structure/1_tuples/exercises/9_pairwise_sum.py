def pairwise_sum(t1, t2):
    """
    Sum elements pairwise.
    
    Args:
        t1 (tuple): First tuple
        t2 (tuple): Second tuple
        
    Returns:
        tuple: Tuple of sums
    """
    return tuple(x + y for x, y in zip(t1, t2))

# Test
t1 = (1, 2, 3, 4, 5)
t2 = (1, 2, 3, 4, 5)
print(f"T1: {t1}")
print(f"T2: {t2}")
print(f"Sum: {pairwise_sum(t1, t2)}")
