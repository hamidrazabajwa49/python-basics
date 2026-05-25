import math

def find_min_max(lst):
    """
    Find min and max values.
    
    Args:
        lst (list): Input list
        
    Returns:
        tuple: (min_val, max_val)
    """
    if not lst:
        return None, None
        
    min_val = float('inf')
    max_val = float('-inf')
    
    for num in lst:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
            
    return min_val, max_val

# Test
numbers = [1, 2, 3, 45, 6, 7, 8, 4, 32, 67, 8, 4, 3, 0]
min_v, max_v = find_min_max(numbers)

print(f"List: {numbers}")
print(f"Min: {min_v}")
print(f"Max: {max_v}")
