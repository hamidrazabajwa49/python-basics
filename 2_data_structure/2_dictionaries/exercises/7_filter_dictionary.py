def filter_marks(students, threshold):
    """
    Filter students with marks above threshold.
    
    Args:
        students (dict): Dictionary of {name: marks}
        threshold (int): Minimum marks
        
    Returns:
        dict: Filtered dictionary
    """
    return {name: marks for name, marks in students.items() if marks > threshold}

# Test
students = {"Ali": 90, "Sara": 45, "Ahmed": 78, "Zara": 66}
print(f"Students: {students}")
print(f"Above 75: {filter_marks(students, 75)}")
