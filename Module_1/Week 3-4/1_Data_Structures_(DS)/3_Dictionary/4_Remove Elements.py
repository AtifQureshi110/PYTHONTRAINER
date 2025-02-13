person = {"name": "John", "age": 30, "city": "New York"}
print("Dictionary Original:\n", person)

# Remove a specific key
person.pop("age")
print("Dictionary after removing or poping the item from the dictionary:\n",person) 

# Remove the last inserted key (Python 3.7+)
person.popitem()
print("Dictionary after using the pop.item():\n",person)  

# Clear the dictionary
person.clear()
print("Dictionary after using clear()\n",person) 
