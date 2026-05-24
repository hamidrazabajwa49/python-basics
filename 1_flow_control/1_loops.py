print("Basic For Loop\n")

# Print num from 0 to 4
for i in range(5):
    print(f"Number: {i}")


print("\nRange with Start and Stop \n")
for i in range(1, 6):
    print(i, end=" ")
print()  # for new line



print("\nRange with Step\n")
for i in range(0, 11, 2):
    print(i, end=" ")
print()

# Print countdown
for i in range(10, 0, -1):
    print(i, end=" ")
print("Taking off!")



print("\nIterating Over Strings\n")

name = "Python"
for char in name:
    print(char)



print("\nIterating Over Lists\n")

fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    print(f"I like {fruit}")




print("\nUsing Enumerate\n")

colors = ["red", "green", "blue"]

for index, color in enumerate(colors):
    print(f"Index {index}: {color}")

# Start enumerate from 1
for index, color in enumerate(colors, start=1):
    print(f"Color #{index}: {color}")




print("\nNested Loops\n")

# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print()  # blank line




print("\nBreak Statement\n")
numbers = [1, 3, 5, 7, 9, 11, 13]
target = 9

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
    print(f"Checking {num}...")




print("\nContinue Statement\n")
for i in range(1, 11):
    if i % 2 == 0:
        continue  
    print(f"Odd number: {i}")


print("\nLoop with Else\n")
for i in range(5):
    print(i)
else:
    print("Loop completed successfully!")

# Examples


# Sum of Numbers
print("\nSum of Numbers\n")

numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print(f"Numbers: {numbers}")
print(f"Sum: {total}")



# Find Max
print("\nFind Maximum\n")

numbers = [45, 23, 67, 12, 89, 34]
maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print(f"Numbers: {numbers}")
print(f"Maximum: {maximum}")




# Count Vowels
print("\nCount Vowels\n")

text = "Hello World"
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print(f"Text: '{text}'")
print(f"Vowel count: {count}")



# Pattern
print("\nPattern Printing\n")

# Right triangle
for i in range(1, 6):
    print("*" * i)

print()

# Pyramid
for i in range(1, 6):
    spaces = " " * (5 - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)



# Factorial of a number
print("\nFactorial Calculator\n")

n = 5
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"{n}! = {factorial}")