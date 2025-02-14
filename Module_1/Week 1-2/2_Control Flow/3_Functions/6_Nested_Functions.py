# A nested function is a function defined inside another function.
#  This allows the inner function to access variables of the outer function.

def outer_function(text):
    def inner_function():
        print(text)
    inner_function()

outer_function("Hello from the outer function!")
