def is_rotation(s1, s2):
    """
    Check if s2 is a rotation of s1.
    
    Args:
        s1 (str): First string
        s2 (str): Second string
        
    Returns:
        bool: True if rotation
    """
    if len(s1) != len(s2):
        return False
        
    # Check if s2 is substring of s1 + s1
    return s2 in (s1 + s1)

# Test
s1 = "waterbottle"
s2 = "erbottlewat"
print(f"{s1}, {s2}: {is_rotation(s1, s2)}")
