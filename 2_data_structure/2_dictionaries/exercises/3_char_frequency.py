def char_frequency(text):
    """
    Count character frequency.
    
    Args:
        text (str): Input string
        
    Returns:
        dict: Character frequencies
    """
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq

# Test
text = 'Hamid Raza'
print(f"String: '{text}'")
print(f"Frequency: {char_frequency(text)}")
