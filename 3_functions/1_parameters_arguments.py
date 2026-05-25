print("Positional Arguments\n")

def greet(first_name, last_name):
    """Arguments passed by position."""
    return f"Hello, {first_name} {last_name}!"

print(greet("Hamid", "Raza"))




print("\nKeyword Arguments\n")
def describe_pet(animal_type, pet_name):
    """Arguments passed by name."""
    return f"I have a {animal_type} named {pet_name}."

# Order doesn't matter with keyword arguments
print(describe_pet(animal_type="dog", pet_name="Buddy"))
print(describe_pet(pet_name="Whiskers", animal_type="cat"))




print("\nDefault Parameters\n")
def make_pizza(size, topping="cheese"):
    """Default value for topping parameter."""
    return f"Making a {size}-inch {topping} pizza."

print(make_pizza(12))  # Uses default topping
print(make_pizza(16, "pepperoni"))  # Custom topping





print("\n*args\n")
def sum_all(*numbers):
    """Accept any number of positional arguments."""
    total = 0
    for num in numbers:
        total += num
    return total

print(f"sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")




print("\n**kwargs\n")
def build_profile(first, last, **user_info):
    """Accept any number of keyword arguments."""
    profile = {"first_name": first, "last_name": last}
    profile.update(user_info)
    return profile

user = build_profile("Hamid", "Raza", age=22, city="Karachi", occupation="Developer")
print(user)




print("\nCombining Parameters\n")
def complex_function(pos1, pos2, *args, default="value", **kwargs):
    """
    Demonstrates all parameter types together.
    Order: positional, *args, default, **kwargs
    """
    print(f"Positional: {pos1}, {pos2}")
    print(f"Args: {args}")
    print(f"Default: {default}")
    print(f"Kwargs: {kwargs}")

complex_function(1, 2, 3, 4, 5, default="custom", key1="val1", key2="val2")




print("\nUnpacking Arguments\n")

def add(a, b, c):
    return a + b + c

# Unpacking list/tuple with *
numbers = [1, 2, 3]
print(f"add(*numbers) = {add(*numbers)}")

# Unpacking dictionary with **
values = {"a": 10, "b": 20, "c": 30}
print(f"add(**values) = {add(**values)}")



# Examples
print("\nPractical Examples\n")


# Shoppinf Cart
def calculate_total(*prices, tax_rate=0.08, discount=0):
    """Calculate total with tax and discount."""
    subtotal = sum(prices)
    tax = subtotal * tax_rate
    total = subtotal + tax - discount
    return total

total = calculate_total(10.99, 25.50, 5.75, tax_rate=0.1, discount=5)
print(f"Total: ${total:.2f}")