def find_longest_word(sentence):
    """
    Find longest word in sentence.
    
    Args:
        sentence (str): Input sentence
        
    Returns:
        str: Longest word
    """
    words = sentence.split()
    if not words:
        return ""
    return max(words, key=len)

# Test
text = "Python is an amazing programming language"
print(f"Sentence: {text}")
print(f"Longest word: {find_longest_word(text)}")
