# seek(offset, from_what): Moves the file pointer to a specific position.
# from_what: 0 (start of the file), 1 (current position), 2 (end of the file).
# tell(): Returns the current file pointer position.

file = open(r"E:\PYTHONTRAINER\Module_1\Week 3-4\File Handling\1_example.txt", "r")
file.seek(5)  # Move to the 5th character
print(file.read())  # Read from the 5th character
print("File pointer is at:", file.tell()) # it will the total number of character in the file 
file.close()

