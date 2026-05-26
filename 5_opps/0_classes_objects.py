"""
OOP - Classes and Objects

Learn the fundamentals of Object-Oriented Programming in Python.

Classes are blueprints for creating objects. Objects are instances of classes.
"""


print("Basic Class\n")

class Person:
    """A simple Person class."""
    
    def __init__(self, name, age):
        """Constructor - called when creating a new object."""
        self.name = name  # Instance variable
        self.age = age
    
    def greet(self):
        """Instance method."""
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating objects (instances)
person1 = Person("Hamid", 22)
person2 = Person("Ali", 25)

person1.greet()
person2.greet()





print("\nClass with Methods\n")

class BankAccount:
    """A simple bank account class."""
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        """Add money to account."""
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")
    
    def withdraw(self, amount):
        """Remove money from account."""
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
    
    def get_balance(self):
        """Return current balance."""
        return self.balance

# Using the class
account = BankAccount("Hamid", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Final balance: ${account.get_balance()}")




print("\nClass vs Instance Variables\n")

class Counter:
    """Demonstrates class vs instance variables."""
    
    count = 0  # Class variable (shared by all instances)
    
    def __init__(self):
        Counter.count += 1  # Modify class variable
        self.id = Counter.count  # Instance variable (unique to each instance)

c1 = Counter()
c2 = Counter()
c3 = Counter()

print(f"Object 1 ID: {c1.id}")
print(f"Object 2 ID: {c2.id}")
print(f"Object 3 ID: {c3.id}")
print(f"Total objects created: {Counter.count}")





print("\nStudent Class\n")

class Student:
    """Represents a student with grades."""
    
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
    
    def add_grade(self, grade):
        """Add a grade to the student's record."""
        self.grades.append(grade)
    
    def get_average(self):
        """Calculate average grade."""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def display_info(self):
        """Display student information."""
        avg = self.get_average()
        print(f"Student: {self.name} (ID: {self.student_id})")
        print(f"Grades: {self.grades}")
        print(f"Average: {avg:.2f}")

# Using the Student class
student = Student("Ali", "CS001")
student.add_grade(85)
student.add_grade(90)
student.add_grade(88)
student.display_info()


# Practical Examples



# Rectangle Class
print("\nRectangle Class\n")

class Rectangle:
    """Represents a rectangle with length and width."""
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        """Calculate area."""
        return self.length * self.width
    
    def perimeter(self):
        """Calculate perimeter."""
        return 2 * (self.length + self.width)
    
    def is_square(self):
        """Check if rectangle is a square."""
        return self.length == self.width

rect = Rectangle(5, 3)
print(f"Rectangle: {rect.length} x {rect.width}")
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")
print(f"Is square: {rect.is_square()}")
