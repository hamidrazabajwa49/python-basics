def encode(strings):
    """Encode list of strings to single string."""
    return '|~|'.join(strings)

def decode(s):
    """Decode string back to list of strings."""
    return s.split('|~|')

# Test
original = ["hello", "world", "python"]
encoded = encode(original)
decoded = decode(encoded)

print(f"Original: {original}")
print(f"Encoded: {encoded}")
print(f"Decoded: {decoded}")
