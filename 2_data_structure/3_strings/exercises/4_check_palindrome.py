def is_palindrome(text):
    """
    Check if string is palindrome.
    
    Args:
        text (str): Input string
        
    Returns:
        bool: True if palindrome, False otherwise
    """
    # Normalize: remove spaces and convert to lower case
    clean_text = text.replace(" ", "").lower()
    
    # Check if equal to reverse
    return clean_text == clean_text[::-1]

# Test
text = "Hamid Raza Bajwa"
if is_palindrome(text):
    print(f"'{text}' is a palindrome.")
else:
    print(f"'{text}' is NOT a palindrome.")
    
# Test 2
text2 = "madam"
if is_palindrome(text2):
    print(f"'{text2}' is a palindrome.")
else:
    print(f"'{text2}' is NOT a palindrome.")
