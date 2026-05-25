def count_occurrences(lst, target):
    """
    Count occurrences of target in list.
    
    Args:
        lst (list): Input list
        target: Value to count
        
    Returns:
        int: Count of occurrences
    """
    count = 0
    for item in lst:
        if item == target:
            count += 1
    return count

# Test
numbers = [1, 2, 3, 42, 1, 2, 3, 5, 6, 2, 1, 3, 2, 4]
target = 2
print(f"List: {numbers}")
print(f"Count of {target}: {count_occurrences(numbers, target)}")
