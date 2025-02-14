# You can assign default values to parameters in the function definition.
# If no argument is passed, the default value is used.

def greet(name="Guest"):
    print(f"Hello, {name}!")
greet()           # Output: Hello, Guest!
greet("John")     # Output: Hello, John!
