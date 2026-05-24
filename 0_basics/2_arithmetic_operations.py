a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"Addition: {a} + {b} = {a + b}")           
print(f"Subtraction: {a} - {b} = {a - b}")        
print(f"Multiplication: {a} * {b} = {a * b}")     
print(f"Division: {a} / {b} = {a / b}")           
print(f"Floor Division: {a} // {b} = {a // b}")   
print(f"Modulus (Remainder): {a} % {b} = {a % b}")  
print(f"Exponentiation: {a} ** {b} = {a ** b}")   


result = 2 + 3 * 4         
print(f"2 + 3 * 4 = {result}")

result = (2 + 3) * 4        
print(f"(2 + 3) * 4 = {result}")

result = 10 + 5 * 2 - 3 / 3  
print(f"10 + 5 * 2 - 3 / 3 = {result}")





counter = 10
print(f"Initial counter: {counter}")

counter += 5  
print(f"After += 5: {counter}")

counter -= 3  
print(f"After -= 3: {counter}")

counter *= 2  
print(f"After *= 2: {counter}")

counter //= 4  
print(f"After //= 4: {counter}")


price = 19.99
tax_rate = 0.08
tax = price * tax_rate
total = price + tax

print(f"Price: ${price:.2f}")
print(f"Tax (8%): ${tax:.2f}")
print(f"Total: ${total:.2f}")


# Math Module
import math

x = 2.95

print(f"Original number: {x}")
print(f"math.ceil({x}) = {math.ceil(x)}")    
print(f"math.floor({x}) = {math.floor(x)}")  
print(f"math.sqrt(16) = {math.sqrt(16)}")    
print(f"math.pow(2, 3) = {math.pow(2, 3)}")  
print(f"math.pi = {math.pi}")                



# Examples

# Calculate area of a circle
radius = 5
area = math.pi * radius ** 2
print(f"Circle with radius {radius}: Area = {area:.2f}")

# Calculate compound interest
principal = 1000
rate = 0.05  # 5%
time = 3     # years
amount = principal * (1 + rate) ** time
print(f"Investment: ${principal} at {rate*100}% for {time} years = ${amount:.2f}")

# Temperature conversion: Celsius to Fahrenheit
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")