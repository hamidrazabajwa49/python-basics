from collections import Counter

def is_anagram(s1, s2):
    """
    Check if strings are anagrams.
    
    Args:
        s1 (str): First string
        s2 (str): Second string
        
    Returns:
        bool: True if anagrams
    """
    # Normalize
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    return Counter(s1) == Counter(s2)

# Test
print(f"listen, silent: {is_anagram('listen', 'silent')}")
print(f"hello, world: {is_anagram('hello', 'world')}")
