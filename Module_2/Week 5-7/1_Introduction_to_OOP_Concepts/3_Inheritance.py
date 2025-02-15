# Theory:
# Inheritance allows a class (child) to inherit attributes and methods from another class (parent).
# It helps avoid code repetition and creates a hierarchy of classes.

class Animal:
    def __init__(self, name):
        self.name = name  # Public attribute
    
    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class constructor
        self.breed = breed  # New attribute specific to Dog class
    
    def speak(self):
        super().speak()  # Calling parent class method
        print(f"{self.name} barks.")

    def show_info(self):
        print(f"Name: {self.name}, Breed: {self.breed}")

# Creating objects
animal = Animal("Generic Animal")
dog = Dog("Buddy", "Golden Retriever")

# Calling methods
animal.speak()  
dog.speak() 
dog.show_info()  

# Dog class inherits from Animal and overrides the speak() method.
# The dog object calls the overridden speak() method, while animal uses the parent class method.
