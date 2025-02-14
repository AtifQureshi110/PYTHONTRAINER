# *args (Non-keyword Arguments)

# Allows passing multiple arguments as a tuple.
# Useful when you don’t know how many arguments will be passed.

def add_numbers(*args):
    total = sum(args)
    print(f"Total: {total}")
add_numbers(5, 10, 15) 