try:
    file = open("non_existent_file.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    if 'file' in locals() and not file.closed:
        file.close()
