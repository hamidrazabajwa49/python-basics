def find_pairs_with_sum(lst, target_sum):
    """
    Find pairs that sum to target.
    
    Args:
        lst (list): Input list
        target_sum (int): Target sum
        
    Returns:
        list: List of tuples (a, b)
    """
    pairs = []
    # O(N^2) approach as in original exercise
    for i in lst:
        for j in lst:
            if i + j == target_sum:
                pairs.append((i, j))
    return pairs

# Test
numbers = [1, 5, 7, -1, 7]
target = 6
print(f"Numbers: {numbers}")
print(f"Target Sum: {target}")
print(f"Pairs: {find_pairs_with_sum(numbers, target)}")
