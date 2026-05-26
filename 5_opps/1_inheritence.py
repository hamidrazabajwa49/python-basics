"""
OOP - Inheritance

Learn how to create new classes based on existing ones.

Inheritance allows code reuse and creates hierarchical relationships.
"""



print("Basic Inheritance\n")

class Animal:
    """Base class (parent)."""
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    """Derived class (child) - inherits from Animal."""
    
    def speak(self):
        """Override parent method."""
        print(f"{self.name} barks: Woof!")

class Cat(Animal):
    """Another derived class."""
    
    def speak(self):
        print(f"{self.name} meows: Meow!")

# Using inheritance
dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.speak()
cat.speak()




print("\nUsing super()\n")

class Person:
    """Base class."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    """Inherits from Person and adds student_id."""
    
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call parent constructor
        self.student_id = student_id
    
    def display(self):
        super().display()  # Call parent method
        print(f"Student ID: {self.student_id}")

student = Student("Ali", 20, "CS001")
student.display()





print("\nMultiple Levels\n")

class Vehicle:
    """Base class."""
    
    def __init__(self, brand):
        self.brand = brand
    
    def info(self):
        print(f"Brand: {self.brand}")

class Car(Vehicle):
    """Inherits from Vehicle."""
    
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    
    def info(self):
        super().info()
        print(f"Model: {self.model}")

class ElectricCar(Car):
    """Inherits from Car."""
    
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def info(self):
        super().info()
        print(f"Battery: {self.battery_size} kWh")

tesla = ElectricCar("Tesla", "Model 3", 75)
tesla.info()





print("\nChecking Inheritance\n")

print(f"isinstance(student, Student): {isinstance(student, Student)}")
print(f"isinstance(student, Person): {isinstance(student, Person)}")
print(f"issubclass(Student, Person): {issubclass(Student, Person)}")
print(f"isinstance(student, Student): {isinstance(student, Student)}")
print(f"isinstance(student, Person): {isinstance(student, Person)}")
print(f"issubclass(Student, Person): {issubclass(Student, Person)}")
