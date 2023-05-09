"""
This example demonstrates the attribute resolution order for both instance and class variables.
The Animal class has a class attribute called sound and an instance attribute called name.
The Dog and Cat classes inherit from Animal and override the sound class attribute.
When calling the speak method, Python will follow the attribute resolution order to resolve the sound attribute.

After creating the instances dog and cat, the example shows the values of the instance and class attributes for each object.
It then calls the speak method for each object, which demonstrates the method resolution order using the sound attribute
from each class. Finally, it sets an instance attribute sound on the dog object and demonstrates that instance
attributes take precedence over class attributes during the attribute resolution process.
"""

class Animal:
    sound = "generic sound"

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} says {self.sound}")

class Dog(Animal):
    sound = "woof"

class Cat(Animal):
    sound = "meow"

# Create instances
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Demonstrate instance and class attributes
print(dog.name)  # Instance attribute from the Dog object
print(dog.sound)  # Class attribute from the Dog class
print(cat.name)  # Instance attribute from the Cat object
print(cat.sound)  # Class attribute from the Cat class

# Demonstrate method resolution order
dog.speak()  # Instance method speak(), using the Dog's class attribute 'sound'
cat.speak()  # Instance method speak(), using the Cat's class attribute 'sound'

# Show that instance attributes take precedence over class attributes
dog.sound = "bark"
print(dog.sound)  # Instance attribute from the Dog object
dog.speak()  # Instance method speak(), using the Dog's instance attribute 'sound'
