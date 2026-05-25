def is_isomorphic(s, t):
    """
    Check if strings are isomorphic.
    
    Args:
        s (str): First string
        t (str): Second string
        
    Returns:
        bool: True if isomorphic
    """
    if len(s) != len(t):
        return False

    map_st, map_ts = {}, {}
    
    for a, b in zip(s, t):
        # Check existing mappings
        if (a in map_st and map_st[a] != b) or \
            (b in map_ts and map_ts[b] != a):
            return False
            
        map_st[a] = b
        map_ts[b] = a
        
    return True

# Test
print(f"egg, add: {is_isomorphic('egg', 'add')}")
print(f"foo, bar: {is_isomorphic('foo', 'bar')}")
