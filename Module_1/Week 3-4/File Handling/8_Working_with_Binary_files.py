# For images, videos, or any binary data, use 'b' mode.

with open(r"E:\PYTHONTRAINER\Module_1\Week 3-4\File Handling\cat_dog.jpg", "rb") as file:
    content = file.read()
    print(content[:20])  # Print the first 20 bytes

