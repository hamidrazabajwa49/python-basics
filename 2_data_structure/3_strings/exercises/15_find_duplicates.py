from collections import Counter

def find_duplicates(text):
    """
    Find duplicate characters.
    
    Args:
        text (str): Input string
        
    Returns:
        list: List of duplicate characters
    """
    count = Counter(text)
    return [char for char, freq in count.items() if freq > 1]

# Test
text = "programming"
print(f"String: {text}")
print(f"Duplicates: {find_duplicates(text)}")
