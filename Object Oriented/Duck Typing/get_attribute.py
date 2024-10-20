class Animal:
    alive = True
  
class Dog(Animal):
    def speak(self):
        print("woof")

class Cat(Animal):
    def speak(self):
        print("meow")

class Car:
    def horn(self):
        print("beep beep")
    
    # Unique property: dynamically handle calls to undefined methods
    def __getattr__(self, name):
        if name == "speak":
            return self.horn
        raise AttributeError(f"'Car' object has no attribute '{name}'")

# Creating instances
animals = [Dog(), Cat(), Car()]

# Iterating over animals and calling speak
for animal in animals:
    animal.speak()
