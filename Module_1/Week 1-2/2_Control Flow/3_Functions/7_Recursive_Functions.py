# A recursive function calls itself until a base condition is met. 
# It is useful for tasks like calculating factorials, Fibonacci numbers, or traversing trees.

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

result = factorial(9)
print(result)