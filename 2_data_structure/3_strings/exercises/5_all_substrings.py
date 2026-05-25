def get_all_substrings(text):
    """
    Get all substrings.
    
    Args:
        text (str): Input string
        
    Returns:
        list: List of all substrings
    """
    substrings = []
    length = len(text)
    
    for i in range(length):
        for j in range(i + 1, length + 1):
            substrings.append(text[i:j])
            
    return substrings

# Test
text = "abc"
print(f"String: {text}")
print(f"Substrings: {get_all_substrings(text)}")
