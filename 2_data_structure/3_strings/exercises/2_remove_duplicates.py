def remove_duplicates(text):
    """
    Remove duplicate characters from string.
    
    Args:
        text (str): Input string
        
    Returns:
        str: String with duplicates removed
    """
    # Remove spaces for this specific exercise logic if desired, 
    # or keep them. Original code removed spaces.
    text = text.replace(" ", "")
    
    result = ""
    seen = set()
    
    for char in text:
        if char not in seen:
            seen.add(char)
            result += char
            
    return result

# Test
text = "Hamid Raza Bajwa"
print(f"Original: {text}")
print(f"Unique: {remove_duplicates(text)}")
