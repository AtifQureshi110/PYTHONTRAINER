person = {"name": "John", "age": 30, "city": "New York"}

# Iterate through keys
print("\nDictionary keys:")
for key in person:
    print(key)  # only keys of the dictionary will show in the output 

print("\nDictionary value") 
# Iterate through values
for value in person.values():
    print(value)  #  only values of the dictionary will show in the output 

# Iterate through key-value pairs
print("\nDictionary items")
for key, value in person.items():
    print(f"{key}: {value}") # all the item will show in the dictionary

