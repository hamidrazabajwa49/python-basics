def longest_word(t):
    """
    Find longest word.
    
    Args:
        t (tuple): Tuple of strings
        
    Returns:
        str: Longest string
    """
    if not t:
        return None
    return max(t, key=len)

# Test
words = ("sun", "banana", "moon", "watermelon")
print(f"Words: {words}")
print(f"Longest: {longest_word(words)}")
