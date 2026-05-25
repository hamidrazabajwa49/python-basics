def group_values(data):
    """
    Group values by key.
    
    Args:
        data (list): List of (key, value) tuples
        
    Returns:
        dict: Dictionary with list of values for each key
    """
    grouped = {}
    for key, value in data:
        grouped.setdefault(key, []).append(value)
    return grouped

# Test
data = [("a", 10), ("b", 20), ("a", 15), ("b", 25), ("c", 30)]
print(f"Input: {data}")
print(f"Grouped: {group_values(data)}")
