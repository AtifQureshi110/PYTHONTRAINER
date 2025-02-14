# Allows passing multiple keyword arguments as a dictionary.
# Useful for handling optional named arguments


def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
display_info(name="John", age=25, country="USA")
