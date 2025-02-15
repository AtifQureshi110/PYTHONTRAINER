# Theory:
# Class: A blueprint or template for creating objects. 
# It defines attributes (variables) and methods (functions) that the objects will have.
# Object: An instance of a class. It holds the actual data and 
# interacts with other objects through methods.

# Class definition
class Person:
    def __init__(self, name, age):
        self.name = name  # Public attribute
        self.age = age    # Public attribute
    
    def display_info(self): # public method
        print(f"Name: {self.name}, Age: {self.age}")

# Object creation
person1 = Person("John", 30)
person1.display_info()

# Explanation:
# Person is a class with attributes name and age and a method display_info().
# person1 is an object of the Person class with the values "John" and 30.