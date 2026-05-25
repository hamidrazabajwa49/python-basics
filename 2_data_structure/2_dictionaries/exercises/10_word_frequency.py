def word_frequency(sentence):
    """
    Count word frequency in a sentence.
    
    Args:
        sentence (str): Input sentence
        
    Returns:
        dict: Word frequencies
    """
    words = sentence.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

# Test
text = "the quick brown fox jumps over the lazy dog the fox was quick"
print(f"Sentence: {text}")
print(f"Frequency: {word_frequency(text)}")
