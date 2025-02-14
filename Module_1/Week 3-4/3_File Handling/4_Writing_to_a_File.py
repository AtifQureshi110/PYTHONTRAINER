# Overwrites the file if it exists or creates a new file if it doesn’t.
file = open(r"E:\PYTHONTRAINER\Module_1\Week 3-4\File Handling\2_example.txt", "w")
file.write("Hello, World!\n")
file.write("Writing to a file in Python.")
file.close()
