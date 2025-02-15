# Theory:
# Abstraction hides implementation details and shows only the essential features.
# Achieved using abstract base classes (ABC) in Python.

class Animal:
    def sound(self):
        print("Some generic animal sound")

class Cat(Animal):  
    def sound(self):
        super().sound()  # Calling the parent class method (optional)
        print("Cat meows")

class Dog(Animal):
    def sound(self):
        super().sound()  # Calling the parent class method (optional)
        print("Dog barks")

# Polymorphism in action
def animal_sound(animal):
    animal.sound()

# Creating objects
cat = Cat()
dog = Dog()
generic_animal = Animal()

# Calling the function
animal_sound(generic_animal)  
animal_sound(cat) 
animal_sound(dog)  


# Explanation:
# Shape is an abstract class with an abstract method area().
# Circle class implements the area() method.
