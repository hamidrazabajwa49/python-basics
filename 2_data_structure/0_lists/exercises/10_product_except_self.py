def product_except_self(lst):
    """
    Calculate product of array except self.
    
    Args:
        lst (list): Input list
        
    Returns:
        list: List of products
    """
    result = []
    n = len(lst)
    
    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:  # Compare indices, not values!
                product *= lst[j]
        result.append(product)
    return result

# Test
numbers = [1, 2, 3, 4]
print(f"Original: {numbers}")
print(f"Products: {product_except_self(numbers)}")
