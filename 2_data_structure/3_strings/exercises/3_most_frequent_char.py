
from collections import Counter

def most_frequent_char(text):
    """
    Find most frequent character.
    
    Args:
        text (str): Input string
        
    Returns:
        str: Most frequent character
    """
    text = text.replace(" ", "")
    if not text:
        return None
        
    counter = Counter(text)
    return counter.most_common(1)[0][0]

# Test
text = "Hamid Raza Bajwa"
print(f"String: {text}")
print(f"Most frequent: {most_frequent_char(text)}")
