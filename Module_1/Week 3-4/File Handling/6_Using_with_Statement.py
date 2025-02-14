# Using the with statement is the recommended way to handle files. 
# It automatically closes the file, 
# even if an error occurs.

with open(r"E:\PYTHONTRAINER\Module_1\Week 3-4\File Handling\1_example.txt", "r") as file:
    content = file.read()
    print(content)

# No need to call file.close(). The file is automatically closed when the block ends.

