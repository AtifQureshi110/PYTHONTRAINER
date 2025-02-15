# Theory:
# Polymorphism allows objects of different classes to be treated the same way.
# It can be achieved through method overriding, where a child class provides its own version of a method.

class Cat:
    def sound(self):
        print("Cat meows")

class Dog:
    def sound(self):
        print("Dog barks")

# Polymorphism in action
def animal_sound(animal):
    animal.sound()

cat = Cat()
dog = Dog()

animal_sound(cat)
animal_sound(dog)

# Explanation:
# The function animal_sound() can take any object with a sound() method, regardless of the class.