file = open(r"E:\PYTHONTRAINER\Module_1\Week 3-4\File Handling\1_example.txt", "r")
content = file.read(10)  # Reads the first 10 characters
print(content)
file.close()