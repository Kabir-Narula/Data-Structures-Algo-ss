from abc import ABC, abstractmethod

class Shape(ABC):
  
  @abstractmethod
  def area(self):
    pass

class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius
    
  def area(self):
    return 3.14 * (self.radius ** 2)

# Define a class for Square that inherits from Shape
class Square(Shape):
    def __init__(self, side):
        # Initialize the side length of the square
        self.side = side
    
    def area(self):
        # Calculate and return the area of the square
        return self.side ** 2

# Define a class for Triangle that inherits from Shape
class Triangle(Shape):
    def __init__(self, base, height):
        # Initialize the base and height of the triangle
        self.base = base
        self.height = height
    
    def area(self):
        # Calculate and return the area of the triangle
        return 0.5 * self.base * self.height

# Polymorphism in action:
# Create a list of different shapes with their dimensions
# Each shape is an instance of a different class (Circle, Square, Triangle)
shapes = [Circle(4), Square(5), Triangle(6, 7)]

# Iterate over each shape in the list and print its area
# This demonstrates polymorphism because each shape object
# calls its own version of the area() method, even though
# they are all accessed through the same interface (the Shape base class)
for shape in shapes:
    print(shape.area())
