def reverse_words(sentence):
    """
    Reverse words in a sentence.
    
    Args:
        sentence (str): Input sentence
        
    Returns:
        str: Sentence with reversed words
    """
    return ' '.join(sentence.split()[::-1])

# Test
text = "Hello from Python"
print(f"Original: {text}")
print(f"Reversed: {reverse_words(text)}")
