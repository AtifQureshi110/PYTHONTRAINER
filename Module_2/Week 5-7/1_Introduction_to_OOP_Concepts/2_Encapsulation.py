# Theory:
# Encapsulation restricts direct access to certain attributes to protect the internal state of the object.
# Private attributes (with __ prefix) can only be accessed or modified through methods.

class Person:
    population = 0  # Public class variable (shared among all instances)

    def __init__(self, name, age, gender="Unknown"):
        self.name = name  # Public attribute
        self._gender = gender  # Protected attribute (not strictly private, but meant for subclass use)
        self.__age = age  # Private attribute
        self.__id = Person.population + 1  # Private unique ID
        Person.population += 1  # Increment total population

    # Public method
    def display_info(self):
        print(f"ID: {self.__id}, Name: {self.name}, Age: {self.__age}, Gender: {self._gender}")

    # Getter for private attributes
    def get_age(self):
        return self.__age

    def get_id(self):
        return self.__id

    # Setter for private attributes
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("❌ Age must be positive.")

# Creating an object
person1 = Person("Alice", 25, "Female")

# Accessing attributes and methods
person1.display_info()  # Public method
print("Accessing the private attribute through a method:", person1.get_age())  
person1.set_age(30)  # Updating private attribute
print("Updated age:", person1.get_age())  


# Private attribute: __age cannot be accessed directly.
# Access and modification are done through the get_age() and set_age() methods.