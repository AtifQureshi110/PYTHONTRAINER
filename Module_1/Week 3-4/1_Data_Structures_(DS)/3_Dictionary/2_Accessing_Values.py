person = {"name": "John", "age": 30, "city": "New York"}

print("name:", person["name"])  
print("age:",person["age"])  

# Using get() method (returns None if the key is not found)
print("city:",person.get("city")) 
print("country:",person.get("country"))  # Output: None B/c There is no items with key of country

