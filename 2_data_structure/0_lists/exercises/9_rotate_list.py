def rotate_list(lst, k):
    """
    Rotate list by k steps.
    
    Args:
        lst (list): Input list
        k (int): Number of steps
        
    Returns:
        list: Rotated list
    """
    if not lst:
        return lst
        
    k = k % len(lst)
    # Slicing method is more efficient than popping in loop
    return lst[-k:] + lst[:-k]

# Test
numbers = [1, 2, 3, 4, 5]
k = 2
print(f"Original: {numbers}")
print(f"Rotated by {k}: {rotate_list(numbers, k)}")
