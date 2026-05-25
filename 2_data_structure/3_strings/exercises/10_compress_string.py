def compress_string(text):
    """
    Compress string using run-length encoding.
    
    Args:
        text (str): Input string
        
    Returns:
        str: Compressed string
    """
    if not text:
        return ""
        
    result = ""
    count = 1
    
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            count += 1
        else:
            result += text[i-1] + str(count)
            count = 1
            
    # Add last group
    result += text[-1] + str(count)
    return result

# Test
text = "aaaabbbcc"
print(f"Original: {text}")
print(f"Compressed: {compress_string(text)}")
