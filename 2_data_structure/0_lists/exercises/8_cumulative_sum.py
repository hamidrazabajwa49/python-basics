def cumulative_sum(lst):
    """
    Calculate cumulative sum.
    
    Args:
        lst (list): Input list
        
    Returns:
        list: Cumulative sum list
    """
    result = []
    total = 0
    for num in lst:
        total += num
        result.append(total)
    return result

# Test
numbers = [1, 2, 3, 4, 5]
print(f"Original: {numbers}")
print(f"Cumulative: {cumulative_sum(numbers)}")
