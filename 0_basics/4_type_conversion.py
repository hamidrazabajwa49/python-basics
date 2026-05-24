# Convert string to int
age_str = "25"
age_int = int(age_str)

print(f"Original: '{age_str}' (type: {type(age_str)})")
print(f"Converted: {age_int} (type: {type(age_int)})")

# Practical example: Calculate birth year
current_year = 2025
birth_year = current_year - age_int
print(f"If you're {age_int}, you were born around {birth_year}")


# Convert string to float
price_str = "19.99"
price_float = float(price_str)

print(f"Original: '{price_str}' (type: {type(price_str)})")
print(f"Converted: {price_float} (type: {type(price_float)})")


# Calculate with tax
tax = price_float * 0.08
total = price_float + tax
print(f"Price: ${price_float:.2f}")
print(f"Total with tax: ${total:.2f}")



age = 22
score = 95.5

# Convert to string for concatenation
age_str = str(age)
score_str = str(score)

# String concatenation (+ only works with strings)
message = "Age: " + age_str + ", Score: " + score_str
print(message)

# Better way: Use f-strings (no conversion needed)
message = f"Age: {age}, Score: {score}"
print(message)



# Any non-empty string is True
bool("Hello")  
bool("")      
bool("0")      

print(f"bool('Hello') = {bool('Hello')}")
print(f"bool('') = {bool('')}")
print(f"bool('0') = {bool('0')}")



# Age Calculator
birth_year_input = input("Enter your birth year: ")
birth_year = int(birth_year_input)  

current_year = 2025
age = current_year - birth_year

print(f"You are approximately {age} years old in 2025.")
print("\nWeight Converter (kg to lbs)\n")

weight_kg_input = input("Enter your weight in kg: ")
weight_kg = float(weight_kg_input) 

weight_lbs = weight_kg / 0.453592  
print(f"Your weight in pounds: {weight_lbs:.2f} lbs")


# Simple Calculator
num1_input = input("Enter first number: ")
num2_input = input("Enter second number: ")

num1 = float(num1_input)
num2 = float(num2_input)

print(f"\n{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2:.2f}")


# Handling Conversion Errors


# These would cause errors (commented out):
# int("hello")      # ValueError: invalid literal for int()
# float("12.5.3")   # ValueError: could not convert string to float
# int("12.5")       # ValueError: invalid literal for int()


print("Safe conversions:")
print(f"int('123') = {int('123')}")       
print(f"float('12.5') = {float('12.5')}")  
print(f"int(12.9) = {int(12.9)}")          
print(f"str(123) = '{str(123)}'")        