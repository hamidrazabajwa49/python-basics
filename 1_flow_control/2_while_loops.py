print("Basic While Loop\n")

counter = 1

while counter <= 5:
    print(f"Count: {counter}")
    counter += 1



print("\nWhile Loop with Input\n")

password = ""

while password != "python123":
    password = input("Enter password: ")
    if password != "python123":
        print("Incorrect! Try again.")

print("Access granted!")





print("\nInfinite Loop with Break\n")

count = 0

while True:  # Infinite loop
    count += 1
    print(f"Iteration {count}")
    
    if count >= 5:
        print("Breaking out of loop!")
        break




print("\nWhile Loop with Continue\n")

number = 0

while number < 10:
    number += 1
    
    if number % 2 == 0:
        continue  
    
    print(f"Odd number: {number}")




print("\n=== While Loop with Else ===\n")

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    print(f"Attempt {attempts + 1}")
    attempts += 1
else:
    print("All attempts completed!")


print("\nInput Validation\n")

age = -1

while age < 0 or age > 120:
    age = int(input("Enter your age (0-120): "))
    if age < 0 or age > 120:
        print("Invalid age! Please try again.")

print(f"Valid age entered: {age}")


# Examples



# Menu Systems
print("\nMenu System\n")

choice = ""

while choice != "4":
    print("\n--- MENU ---")
    print("1. Option A")
    print("2. Option B")
    print("3. Option C")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print("You selected Option A")
    elif choice == "2":
        print("You selected Option B")
    elif choice == "3":
        print("You selected Option C")
    elif choice == "4":
        print("Goodbye!")
    else:
        print("Invalid choice!")



# Sum until zero
print("\nSum Until Zero\n")

total = 0
number = None

print("Enter numbers to sum (0 to stop):")

while number != 0:
    number = int(input("Enter a number: "))
    total += number

print(f"Total sum: {total}")




# Countdown Timer
print("\nCountdown Timer\n")

import time # built-in module

seconds = 5
print(f"Countdown from {seconds}...")

while seconds > 0:
    print(seconds)
    time.sleep(1) 
    seconds -= 1

print("Time's up!")


# Find 1st Divisor
print("\nFind First Divisor\n")

number = 100
divisor = 2

while number % divisor != 0:
    divisor += 1

print(f"First divisor of {number} (other than 1): {divisor}")




print("\nFor vs While\n")

# Use FOR when you know the number of iterations
print("FOR loop - known iterations:")
for i in range(5):
    print(f"  Iteration {i}")

# Use WHILE when iterations depend on a condition
print("\nWHILE loop - condition-based:")
count = 0
while count < 5:
    print(f"  Count: {count}")
    count += 1