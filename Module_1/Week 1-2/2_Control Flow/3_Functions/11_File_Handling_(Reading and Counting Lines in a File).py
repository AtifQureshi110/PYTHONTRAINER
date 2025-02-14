def count_lines_in_file(filename):
    """Counts the number of lines in the specified file."""
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        return "File not found."

# Real-world example:
file_name = "data.txt"
print("Number of lines:", count_lines_in_file(file_name))
