"""
OOP - Encapsulation

Learn about encapsulation: hiding internal details and controlling access.

Encapsulation bundles data and methods together and restricts direct access
to some components.
"""



print("Public vs Private \n")

class BankAccount:
    """Demonstrates encapsulation."""
    
    def __init__(self, owner, balance):
        self.owner = owner  # Public attribute
        self.__balance = balance  # Private attribute (name mangling with __)
    
    def deposit(self, amount):
        """Public method to modify private attribute."""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}")
        else:
            print("Invalid amount!")
    
    def withdraw(self, amount):
        """Controlled access to private data."""
        if amount > self.__balance:
            print("Insufficient funds!")
        elif amount <= 0:
            print("Invalid amount!")
        else:
            self.__balance -= amount
            print(f"Withdrew ${amount}")
    
    def get_balance(self):
        """Getter method for private attribute."""
        return self.__balance

account = BankAccount("Hamid", 1000)
print(f"Owner: {account.owner}")  # Public - accessible

# This would cause an error:
# print(account.__balance)  # Private - not directly accessible

# Use getter method instead
print(f"Balance: ${account.get_balance()}")

account.deposit(500)
account.withdraw(200)
print(f"New balance: ${account.get_balance()}")






print("\nProperty Decorators\n")

class Person:
    """Using @property for controlled access."""
    
    def __init__(self, name, age):
        self._name = name  # Protected attribute (convention: single _)
        self._age = age
    
    @property
    def name(self):
        """Getter for name."""
        return self._name
    
    @name.setter
    def name(self, value):
        """Setter for name with validation."""
        if len(value) < 2:
            print("Name too short!")
        else:
            self._name = value
    
    @property
    def age(self):
        """Getter for age."""
        return self._age
    
    @age.setter
    def age(self, value):
        """Setter for age with validation."""
        if value < 0 or value > 120:
            print("Invalid age!")
        else:
            self._age = value

person = Person("Ali", 22)

# Access like attributes, but using getter/setter methods
print(f"Name: {person.name}")
print(f"Age: {person.age}")

# Validation in action
person.name = "A"  # Too short
person.age = 150   # Invalid

person.name = "Ahmed"  # Valid
person.age = 25        # Valid
print(f"Updated: {person.name}, {person.age}")



# Practical Examples


# Temprature Class
print("\nTemperature Class\n")

class Temperature:
    """Temperature with automatic conversion."""
    
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            print("Temperature below absolute zero!")
        else:
            self._celsius = value
    
    @property
    def fahrenheit(self):
        """Auto-calculated from celsius."""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set celsius from fahrenheit."""
        self._celsius = (value - 32) * 5/9

temp = Temperature(25)
print(f"{temp.celsius}°C = {temp.fahrenheit}°F")

temp.fahrenheit = 98.6
print(f"{temp.celsius:.1f}°C = {temp.fahrenheit}°F")





print("\nBenefits\n")

class Rectangle:
    """Encapsulation ensures data integrity."""
    
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    
    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, value):
        if value > 0:
            self.__length = value
        else:
            print("Length must be positive!")
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if value > 0:
            self.__width = value
        else:
            print("Width must be positive!")
    
    @property
    def area(self):
        """Calculated property (no setter)."""
        return self.__length * self.__width

rect = Rectangle(5, 3)
print(f"Area: {rect.area}")

rect.length = 10
print(f"New area: {rect.area}")

rect.width = -5  # Validation prevents invalid data
