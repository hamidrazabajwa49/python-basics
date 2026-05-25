def is_valid_palindrome(text):
    """
    Check if string is palindrome (ignoring non-alphanumeric).
    
    Args:
        text (str): Input string
        
    Returns:
        bool: True if palindrome
    """
    # Filter only alphanumeric and convert to lower
    clean = ''.join(char.lower() for char in text if char.isalnum())
    return clean == clean[::-1]

# Test
text = "A man, a plan, a canal: Panama"
print(f"String: '{text}'")
print(f"Is palindrome: {is_valid_palindrome(text)}")
