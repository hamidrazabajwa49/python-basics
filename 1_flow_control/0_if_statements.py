print("If Statement\n")

age = 20

if age >= 18:
    print("You are an adult.")



print("\nIf-Else Statement\n")

temperature = 25

if temperature > 30:
    print("It's hot outside!")
else:
    print("The weather is pleasant.")



print("\n=== If-Elif-Else Statement ===\n")

score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Score: {score}, Grade: {grade}")



print("\nComparison Operators\n")

x = 10
y = 20

print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")  # Equal to
print(f"x != y: {x != y}")  # Not equal to
print(f"x > y: {x > y}")    # Greater than
print(f"x < y: {x < y}")    # Less than
print(f"x >= y: {x >= y}")  # Greater than or equal to
print(f"x <= y: {x <= y}")  # Less than or equal to



print("\nLogical Operators\n")

age = 25
has_license = True

# AND operator (both conditions must be True)
if age >= 18 and has_license:
    print("You can drive.")

# OR operator (at least one condition must be True)
is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("You can relax!")

# NOT operator (reverses the condition)
is_raining = False

if not is_raining:
    print("You don't need an umbrella.")



print("\nNested If Statements\n")

age = 25
has_ticket = True

if age >= 18:
    if has_ticket:
        print("You can enter the concert.")
    else:
        print("You need a ticket to enter.")
else:
    print("You must be 18 or older.")




# Examples: 

# Login System
print("\nLogin System Example\n")

correct_username = "admin"
correct_password = "pass123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login successful! Welcome back.")
elif username == correct_username:
    print("Incorrect password.")
elif password == correct_password:
    print("Incorrect username.")
else:
    print("Both username and password are incorrect.")



# BMI Calculator
print("\nBMI Calculator\n")

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

print(f"Your BMI: {bmi:.2f}")

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"Category: {category}")


# Grade Calculator
print("\nGrade Calculator\n")

score = int(input("Enter your score (0-100): "))

if score < 0 or score > 100:
    print("Invalid score! Must be between 0 and 100.")
elif score >= 90:
    print("Grade: A - Excellent!")
elif score >= 80:
    print("Grade: B - Good job!")
elif score >= 70:
    print("Grade: C - Fair")
elif score >= 60:
    print("Grade: D - Needs improvement")
else:
    print("Grade: F - Failed")




print("\nTernary Operator\n")

age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Age: {age}, Status: {status}")

# Same as:
# if age >= 18:
#     status = "Adult"
# else:
#     status = "Minor"