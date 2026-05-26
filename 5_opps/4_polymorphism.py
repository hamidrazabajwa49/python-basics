"""
OOP - Polymorphism

Learn about polymorphism: same interface, different implementations.

Polymorphism allows objects of different classes to be treated through
the same interface.
"""





print("Method Overriding\n")

class Animal:
    """Base class."""
    
    def speak(self):
        return "Some sound"

class Dog(Animal):
    """Override speak method."""
    
    def speak(self):
        return "Woof!"

class Cat(Animal):
    """Override speak method."""
    
    def speak(self):
        return "Meow!"

class Cow(Animal):
    """Override speak method."""
    
    def speak(self):
        return "Moo!"

# Polymorphism in action
animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(f"{animal.__class__.__name__}: {animal.speak()}")





print("\nPolymorphism with Functions\n")

def animal_sound(animal):
    """Works with any object that has speak() method."""
    print(animal.speak())

dog = Dog()
cat = Cat()

animal_sound(dog)
animal_sound(cat)





print("\nDuck Typing\n")

# "If it walks like a duck and quacks like a duck, it's a duck"

class Bird:
    def fly(self):
        return "Flying in the sky"

class Airplane:
    def fly(self):
        return "Flying with engines"

class Butterfly:
    def fly(self):
        return "Fluttering around"

def make_it_fly(flying_object):
    """Works with any object that has fly() method."""
    print(flying_object.fly())

# All different classes, but same interface
make_it_fly(Bird())
make_it_fly(Airplane())
make_it_fly(Butterfly())






print("\nOperator Overloading\n")

class Point:
    """2D point with operator overloading."""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Overload + operator."""
        return Point(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        """String representation."""
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2  # Uses __add__ method

print(f"{p1} + {p2} = {p3}")



# Practical Examples


# Payment System
print("\nPayment System\n")

class Payment:
    """Base payment class."""
    
    def process(self, amount):
        raise NotImplementedError("Subclass must implement process()")

class CreditCard(Payment):
    """Credit card payment."""
    
    def process(self, amount):
        return f"Processing ${amount} via Credit Card"

class PayPal(Payment):
    """PayPal payment."""
    
    def process(self, amount):
        return f"Processing ${amount} via PayPal"

class BankTransfer(Payment):
    """Bank transfer payment."""
    
    def process(self, amount):
        return f"Processing ${amount} via Bank Transfer"

def make_payment(payment_method, amount):
    """Process payment using any payment method."""
    print(payment_method.process(amount))

# Same function works with different payment methods
make_payment(CreditCard(), 100)
make_payment(PayPal(), 50)
make_payment(BankTransfer(), 200)





# Shape Calculator
print("\nShape Calculator\n")

class Shape:
    """Base shape class."""
    
    def area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

def print_area(shape):
    """Works with any shape."""
    print(f"{shape.__class__.__name__} area: {shape.area():.2f}")

shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]

for shape in shapes:
    print_area(shape)
