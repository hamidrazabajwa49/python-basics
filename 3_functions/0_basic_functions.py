print("Basic Functions\n")

# Simple function with no parameters(input)
def greet():
    print("Hello, World!")

# Call the function
greet()

# Function with parameter(inputs)
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Ali")
greet_person("Sara")




print("\nReturn Values\n")

def add(a, b):
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")

# Function with multiple return values
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([1, 5, 3, 9, 2])
print(f"Min: {minimum}, Max: {maximum}")





print("\nDefault Parameters\n")

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Ali"))  # Uses default greeting
print(greet("Sara", "Hi"))  # Custom greeting




print("\nKeyword Arguments\n")

def describe_person(name, age, city):
    return f"{name} is {age} years old and lives in {city}"

# Positional arguments
print(describe_person("Ali", 22, "Karachi"))

# Keyword arguments (order doesn't matter)
print(describe_person(city="Lahore", name="Sara", age=25))





print("\nDocstrings\n")

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length: The length of the rectangle
        width: The width of the rectangle
        
    Returns:
        The area of the rectangle
    """
    return length * width

area = calculate_area(5, 3)
print(f"Area: {area}")
print(f"Docstring: {calculate_area.__doc__}")



# Examples
print("\nPractical Examples\n")

# Temperature converter
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

# Check if number is even
def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

print(f"Is 4 even? {is_even(4)}")
print(f"Is 7 even? {is_even(7)}")

# Calculate factorial
def factorial(n):
    """Calculate factorial of n."""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(f"5! = {factorial(5)}")