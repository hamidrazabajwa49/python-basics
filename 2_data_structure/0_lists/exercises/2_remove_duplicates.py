def remove_duplicates(lst):
    """
    Remove duplicates from list while preserving order.
    
    Args:
        lst (list): Input list
        
    Returns:
        list: List without duplicates
    """
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Test
numbers = [1, 2, 3, 1, 4, 5, 6, 2, 5, 6, 2, 4]
print(f"Original: {numbers}")
print(f"Unique: {remove_duplicates(numbers)}")
