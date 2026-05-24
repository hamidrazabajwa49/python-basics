name = input("What is your name? ")
print(f"Hello, {name}! Nice to meet you.")


color = input("What is your favorite color? ")
print(f"{name} likes {color}.")


age_input = input("Enter your age: ")
print(f"You entered: {age_input}")
print(f"Type of input: {type(age_input)}") 


first_name = input("First name: ")
last_name = input("Last name: ")
city = input("City: ")

print(f"\nProfile:")
print(f"Name: {first_name} {last_name}")
print(f"City: {city}")



email = input("Enter your email address:\n>>> ")
print(f"Email saved: {email}")



print("Please enter your address:")
street = input("Street: ")
zip_code = input("ZIP Code: ")
print(f"Address: {street}, {zip_code}")


#Examples

username = input("Choose a username: ")
favorite_food = input("Favorite food: ")
hobby = input("Favorite hobby: ")

print("\n" + "="*40)
print("USER PROFILE")
print("\n")
print(f"Username: {username}")
print(f"Favorite Food: {favorite_food}")
print(f"Hobby: {hobby}")
print("\n")