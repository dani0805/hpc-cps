"""
In this example, we define an abstract Shape class with an abstract area method.
We then create two specific shape classes, Circle and Rectangle, which both inherit from the Shape class and
implement the area method.

The ShapeFactory class is responsible for creating shape objects. It has a static method, create_shape,
which takes a shape_type string and additional arguments required to create the specific shape object.
Depending on the shape_type, the method creates and returns an instance of the appropriate shape class.

The Factory pattern allows you to create objects without specifying the exact class of the object that will be created.
This can make your code more flexible and maintainable, as new shape classes can be added without modifying the code
that uses the ShapeFactory.
"""
from abc import ABC, abstractmethod

# Define an abstract Shape class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Define specific shape classes
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Define the ShapeFactory class
class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, *args, **kwargs):
        if shape_type == "circle":
            return Circle(*args, **kwargs)
        elif shape_type == "rectangle":
            return Rectangle(*args, **kwargs)
        else:
            raise ValueError("Invalid shape type.")

# Test the Factory pattern
circle = ShapeFactory.create_shape("circle", radius=5)
print(f"Circle area: {circle.area()}")

rectangle = ShapeFactory.create_shape("rectangle", width=4, height=6)
print(f"Rectangle area: {rectangle.area()}")
