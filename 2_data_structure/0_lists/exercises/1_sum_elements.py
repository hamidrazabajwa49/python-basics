def sum_elements(numbers):
    """
    Calculate sum of list elements.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        int: Sum of numbers
    """
    total = 0
    for num in numbers:
        total += num
    return total

# Test
numbers = [1, 2, 3, 4, 5, 6]
print(f"Numbers: {numbers}")
print(f"Sum (manual): {sum_elements(numbers)}")
print(f"Sum (built-in): {sum(numbers)}")
