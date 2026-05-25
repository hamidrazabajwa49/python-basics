def count_vowels_consonants(text):
    """
    Count vowels and consonants in a string.
    
    Args:
        text (str): Input string
        
    Returns:
        tuple: (vowel_count, consonant_count)
    """
    v_count = 0
    c_count = 0
    vowels = 'aeiou'
    
    for char in text.lower():
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
                
    return v_count, c_count

# Test
text = "Hamid Raza Bajwa"
v, c = count_vowels_consonants(text)
print(f"String: {text}")
print(f"Vowels: {v}")
print(f"Consonants: {c}")
