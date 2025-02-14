# You specify the parameter name during the function call.
# The order doesn’t matter, but parameter names must match.

def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")
greet(age=25, name="John")  # Correct
