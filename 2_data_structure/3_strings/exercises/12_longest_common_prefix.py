def longest_common_prefix(strs):
    """
    Find longest common prefix.
    
    Args:
        strs (list): List of strings
        
    Returns:
        str: Longest common prefix
    """
    if not strs:
        return ""
    
    prefix = strs[0]
    for word in strs[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# Test
words = ["flower", "flow", "flight"]
print(f"Words: {words}")
print(f"Prefix: {longest_common_prefix(words)}")
