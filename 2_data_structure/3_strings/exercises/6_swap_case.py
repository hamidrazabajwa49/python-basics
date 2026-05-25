def manual_swap_case(text):
    """
    Swap case of characters manually.
    
    Args:
        text (str): Input string
        
    Returns:
        str: String with swapped case
    """
    result = ""
    for char in text:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char
    return result

# Test
text = "HeLLo World"
print(f"Original: {text}")
print(f"Swapped:  {manual_swap_case(text)}")
