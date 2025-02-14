# String to Integer Conversion
x = "123"
print(type(x))
y = int(x)  #
print("string data type of x is Converted to integer 123\n")

# Float to Integer Conversion
x = 3.14
y = int(x)
print(f"Float {x} is converted to integer: {y}\n")  # 3

# Integer to String Conversion
x = 100
y = str(x)
print(f"Integer {x} is converted to string: '{y}'\n")  # '100'

# List to Set Conversion
x = [1, 2, 2, 3]
y = set(x)
print(f"List {x} is converted to set: {y}\n")  # {1, 2, 3}

# String to Float Conversion
x = "3.14159"
y = float(x)
print(f"String '{x}' is converted to float: {y}\n")  # 3.14159

# Boolean Conversion
x = 0  # or an empty string "", empty list [], etc.
y = bool(x)
print(f"The integer {x} is converted to boolean: {y}\n")  # False
