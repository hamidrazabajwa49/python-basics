def reverse_list(lst):
    """
    Reverse a list manually.
    
    Args:
        lst (list): Input list
        
    Returns:
        list: Reversed list
    """
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

# Test
numbers = [1, 2, 3, 4]
print(f"Original: {numbers}")
print(f"Reversed (manual): {reverse_list(numbers)}")

# Built-in
numbers.reverse()
print(f"Reversed (built-in): {numbers}")
