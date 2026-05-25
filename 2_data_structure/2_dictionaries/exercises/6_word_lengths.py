def get_word_lengths(words):
    """
    Map words to their lengths.
    
    Args:
        words (list): List of words
        
    Returns:
        dict: {word: length}
    """
    return {word: len(word) for word in words}

# Test
words = ["apple", "banana", "cherry"]
print(f"Words: {words}")
print(f"Lengths: {get_word_lengths(words)}")
